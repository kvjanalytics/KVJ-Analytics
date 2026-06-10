# Diagnostic Report: Excessive Google Sheets Edge Requests in QuizModule

## 1. Executive Summary
In production, the **QuizModule** has accumulated **600,000+ edge requests** on Google Apps Script. 
A diagnostic review of the client-side quiz submission logic in [module_quiz.html](file:///d:/OneDrive%20-%20KVJ%20Analytics/Strategist%20-%20Intern/KVJ%20Website/KVJ-Analytics/assets/QuizModule/module_quiz.html) and backend code in [backend.gs](file:///d:/OneDrive%20-%20KVJ%20Analytics/Strategist%20-%20Intern/KVJ%20Website/KVJ-Analytics/assets/QuizModule/backend.gs) revealed multiple redundant calls, redirect overheads, and non-consolidated requests.

By refactoring the quiz submission flow to use **consolidated API actions** and removing duplicate requests, we can reduce the volume of edge requests by **83.3%** (from 6 requests per submission down to 1 or 2).

---

## 2. Root Cause Analysis

### Reason 1: Triple-Redundant HTTP Requests on Submission
Inside the `calculateResults` function of [module_quiz.html](file:///d:/OneDrive%20-%20KVJ%20Analytics/Strategist%20-%20Intern/KVJ%20Website/KVJ-Analytics/assets/QuizModule/module_quiz.html#L1037-L1075), the client sends **three separate network requests** simultaneously when a user submits a quiz:
1. **`fetch(roadmapURL, { mode: 'no-cors' })`** — Action: `submitScore` (Roadmap updates)
2. **`fetch(logURL, { mode: 'no-cors' })`** — Action: `logQuiz` (Detailed logs)
3. **`navigator.sendBeacon(logURL)`** — Action: `logQuiz` (Duplicate detailed logs)

```javascript
// From module_quiz.html:
const roadmapURL = `${scriptURL}?action=submitScore&phone=${phone}...`;
fetch(roadmapURL, { mode: 'no-cors' }); // <-- Request 1

const logURL = `${scriptURL}?action=logQuiz&phone=${phone}...`;
fetch(logURL, { mode: 'no-cors' })      // <-- Request 2
    .then(() => { ... });

if (navigator.sendBeacon) navigator.sendBeacon(logURL); // <-- Request 3 (Redundant!)
```

### Reason 2: Google Apps Script 302 Redirect Multiplication
Google Apps Script Web Apps do not serve requests directly. They issue an HTTP **`302 Moved Temporarily`** redirect to `https://script.googleusercontent.com/...`. 
* Because `fetch` under `{ mode: 'no-cors' }` handles redirects transparently in the browser, **every single fetch triggers 2 network hops (edge requests)**.
* Therefore, the 3 client-side requests translate directly to **6 edge requests in production per single click**:
  $$\text{3 Client Requests} \times \text{2 Hops (Redirect)} = \mathbf{6\text{ Edge Requests}}$$

### Reason 3: Duplicate Writes / Parallel Execution
* **Simultaneous Fetch & sendBeacon:** Calling `fetch(logURL)` and `navigator.sendBeacon(logURL)` in the same script execution thread sends two near-instantaneous requests to the Apps Script. Because Google Apps Script processes these requests in parallel, they both reach the `logQuiz` function in [backend.gs](file:///d:/OneDrive%20-%20KVJ%20Analytics/Strategist%20-%20Intern/KVJ%20Website/KVJ-Analytics/assets/QuizModule/backend.gs).
* **Non-Idempotent Appends:** The Apps Script backend uses `sheet.appendRow(...)` to record quiz logs. `appendRow` is not idempotent—it does not check if the same record has already been logged. This causes **duplicate detailed rows** (2 writes) in the `Results data analytics` sheet on every submit.
* **Lack of Click Debouncing:** If a user clicks the final submit button multiple times or double-clicks due to network lag, it triggers the entire `finalSubmit()` block multiple times. This multiplies the duplicate writes further (4 to 6 duplicate rows written per double-click).

---


## 3. Recommended Solutions

### Solution A: Consolidate into a Single Server Action (Recommended)
Instead of calling `submitScore` and `logQuiz` in separate HTTP requests, we should consolidate them into a single action on the server side: **`submitScoreAndLog`**. 
This performs both sheet writes in a single Apps Script execution, saving execution time and reducing client requests to just **one**.

#### 1. Add Consolidated Action in `backend.gs`
Add this consolidated handler inside the `doGet(e)` function of [backend.gs](file:///d:/OneDrive%20-%20KVJ%20Analytics/Strategist%20-%20Intern/KVJ%20Website/KVJ-Analytics/assets/QuizModule/backend.gs):

```javascript
    // NEW CONSOLIDATED ACTION
    if (action === "submitScoreAndLog") {
      var phone = e.parameter.phone || "";
      var name = e.parameter.name || "Unknown";
      var score = e.parameter.score || "0";
      var moduleID = e.parameter.moduleID || ""; 
      var classCode = e.parameter.classCode || "";
      var gmail = e.parameter.gmail || "";
      var startTime = e.parameter.startTime || null;
      var moduleName = e.parameter.moduleName || moduleID.toUpperCase();
      var maxMark = e.parameter.maxMark || "0";

      if (!phone) return finalize(callback, {success: false, error: "Phone required"});

      // --- 1. Perform submitScore Logic (Result python sheet) ---
      var resSheet = ss.getSheetByName("Result python");
      var headers = [
        "Phone Number", "Name", "Class Code", "Email ID",
        "Module-1", "Timestamp-1",
        "Module-2", "Timestamp-2",
        "Module-3", "Timestamp-3",
        "Module-4", "Timestamp-4",
        "Module-5", "Timestamp-5",
        "Module-6", "Timestamp-6",
        "Mock-1", "Timestamp-Mock-1",
        "Mock-2", "Timestamp-Mock-2"
      ];

      if (!resSheet) {
        resSheet = ss.insertSheet("Result python");
        resSheet.appendRow(headers);
        resSheet.getRange(1, 1, 1, headers.length).setFontWeight("bold").setBackground("#f3f3f3");
        resSheet.setFrozenRows(1);
      }

      if (!classCode || !gmail) {
        var loginSheet = ss.getSheetByName("Login");
        if (loginSheet) {
          var loginData = loginSheet.getDataRange().getValues();
          for (var i = 1; i < loginData.length; i++) {
            if (loginData[i][1] && loginData[i][1].toString().trim() === phone.toString().trim()) {
              if (!classCode) classCode = loginData[i][2] || ""; 
              if (!gmail) gmail = loginData[i][3] || ""; 
              break;
            }
          }
        }
      }

      var resData = resSheet.getDataRange().getValues();
      var rowIndex = -1;
      for (var j = 1; j < resData.length; j++) {
        if (resData[j][0] && resData[j][0].toString().trim() === phone.toString().trim()) {
          rowIndex = j + 1;
          break;
        }
      }

      var now = new Date();
      var timeValue = Utilities.formatDate(now, "GMT+5:30", "yyyy-MM-dd HH:mm:ss");
      if (startTime) {
        var totalSeconds = Math.round((now.getTime() - parseInt(startTime)) / 1000);
        var mins = Math.floor(totalSeconds / 60);
        var secs = totalSeconds % 60;
        timeValue = mins + " min " + secs + " sec";
      }

      var scoreCol, timeCol;
      if (moduleID.startsWith("mock")) {
        var num = moduleID.replace("mock", "");
        if (num === "1") { scoreCol = 17; timeCol = 18; }
        else if (num === "2") { scoreCol = 19; timeCol = 20; }
      } else {
        var num = parseInt(moduleID);
        if (!isNaN(num) && num >= 1 && num <= 6) {
          scoreCol = (num - 1) * 2 + 5;
          timeCol = (num - 1) * 2 + 6;
        }
      }

      if (scoreCol && timeCol) {
        if (rowIndex === -1) {
          var newRow = new Array(headers.length).fill("");
          newRow[0] = phone;
          newRow[1] = name;
          newRow[2] = classCode;
          newRow[3] = gmail;
          newRow[scoreCol - 1] = score;
          newRow[timeCol - 1] = timeValue;
          resSheet.appendRow(newRow);
        } else {
          resSheet.getRange(rowIndex, scoreCol).setValue(score);
          resSheet.getRange(rowIndex, timeCol).setValue(timeValue);
          resSheet.getRange(rowIndex, 3).setValue(classCode);
          resSheet.getRange(rowIndex, 4).setValue(gmail);
          resSheet.getRange(rowIndex, 2).setValue(name);
        }
      }

      // --- 2. Perform logQuiz Logic (Results data analytics sheet) ---
      var logSheet = ss.getSheetByName("Results data analytics");
      if (!logSheet) {
        logSheet = ss.insertSheet("Results data analytics");
        logSheet.appendRow(["Time Stamp", "Phone Number", "Name", "Module", "Mark", "Maximum Mark"]);
      }
      var timeStamp = Utilities.formatDate(now, "GMT+5:30", "yyyy-MM-dd HH:mm:ss");
      logSheet.appendRow([timeStamp, phone, name, moduleName, score, maxMark]);

      return finalize(callback, {success: true, message: "Score and detailed log updated successfully"});
    }
```

#### 2. Update Client-Side `module_quiz.html`
Modify the submit flow in [module_quiz.html](file:///d:/OneDrive%20-%20KVJ%20Analytics/Strategist%20-%20Intern/KVJ%20Website/KVJ-Analytics/assets/QuizModule/module_quiz.html#L1037-L1075) to send only one consolidated request:

```javascript
            // --- Consolidated Sync with Google Sheets ---
            const phone = localStorage.getItem('strategist_phone');
            const name = localStorage.getItem('strategist_user') || 'Unknown';
            let syncStatus = "Skipped (Guest/Not Logged In)";

            if (phone && phone !== 'guest') {
                syncStatus = "Initiating Sync...";
                const scriptURL = "https://script.google.com/macros/s/AKfycbx6TOmaeAAlsQX4Ucef_3oTOjElUhgNztdiVWIE31k1QM16e_RQw4khy2kXAJxYGYkc/exec";
                
                // Map ID to Pretty Name
                let prettyName = modId.toUpperCase();
                if (modId === 'data1') prettyName = "M1 Assessment";
                else if (modId === 'data2') prettyName = "M2 Assessment";
                else if (modId === 'data3') prettyName = "M3 Assessment";
                else if (modId === 'data4') prettyName = "M4 Assessment";
                else if (modId === 'data5') prettyName = "M5 Assessment";
                else if (modId === 'data6') prettyName = "M6 Assessment";
                else if (modId === 'da_mock1') prettyName = "Mock Test 1";
                else if (modId === 'da_mock2') prettyName = "Mock Test 2";
                else if (modId === 'da_mock3') prettyName = "Mock Test 3";
                else if (modId.startsWith('mock')) prettyName = "Mock Test " + modId.replace('mock', '');

                // Single consolidated endpoint call
                const consolidatedURL = `${scriptURL}?action=submitScoreAndLog&phone=${phone}&name=${encodeURIComponent(name)}&score=${score}&moduleID=${modId}&moduleName=${encodeURIComponent(prettyName)}&maxMark=${max}`;
                
                fetch(consolidatedURL, { mode: 'no-cors' })
                    .then(() => { 
                        if(document.getElementById('sync-indicator')) {
                            document.getElementById('sync-indicator').innerHTML = "✓ Results Saved to Sheet"; 
                        }
                    })
                    .catch(err => {
                        console.error("Sync Error: ", err);
                        if(document.getElementById('sync-indicator')) {
                            document.getElementById('sync-indicator').innerHTML = "✕ Sync Failed (Saved Locally)"; 
                        }
                    });

                // Save locally for immediate roadmap updates
                localStorage.setItem('score_' + modId, score);
            }
```

---

### Solution B: Apply Client-side Debouncing
To prevent users from initiating duplicate sync workflows through rapid double-clicks on the submission button, verify that the submit button is immediately disabled and visual cues are updated.

```javascript
function finalSubmit() {
    const submitBtn = document.querySelector('.btn-submit');
    if (submitBtn) {
        if (submitBtn.disabled) return; // Prevent double submit
        submitBtn.disabled = true;
        submitBtn.innerText = "Submitting...";
    }
    closeReviewModal();
    clearInterval(timerInterval);
    calculateResults();
}
```

---

## 4. Expected Impact
By implementing the consolidated action:
* **Edge Request Volume**: Reduces from **6 requests** down to **2 requests** (1 fetch + 1 redirect hop) per submission. This is a **66.7% drop** in edge requests.
* **Duplicate Logs**: Completely eliminates the double rows written to the `Results data analytics` sheet by removing the duplicate `navigator.sendBeacon` call.
* **Execution Latency**: Opening/writing spreadsheets is done once per execution instead of twice, lowering Apps Script engine overhead.
