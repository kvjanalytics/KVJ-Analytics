function doGet(e) {
  var action = e.parameter.action;
  var callback = e.parameter.callback;

  try {
    var ss = SpreadsheetApp.getActiveSpreadsheet();
    var sheet = ss.getSheetByName("Login") || ss.getActiveSheet();
    var data = sheet.getDataRange().getValues();

    // 1. REGISTER ACTION
    if (action === "register" || action === "signup") {
      var name = e.parameter.name || "Unknown";
      var gmail = e.parameter.gmail || e.parameter.email || "Missing";
      var phone = e.parameter.phone || "";
      var code = e.parameter.classCode || e.parameter.code || "None";
      var pass = e.parameter.password || "";

      if (!phone) return finalize(callback, {success: false, error: "Phone number is required"});

      if (pass !== "") {
        // ACCOUNT CREATION (From login.html "Sign Up")
        // Put them in the Login sheet so they can log in later.
        var phoneExistsInLogin = false;
        for (var i = 1; i < data.length; i++) {
          if (data[i][1] && data[i][1].toString().trim() === phone.toString().trim()) {
            phoneExistsInLogin = true;
            break;
          }
        }
        if (!phoneExistsInLogin) {
          sheet.appendRow([name, phone, code, gmail, pass]);
        }
      } else {
        // COURSE REGISTRATION (From registration.html)
        // Check if they are already registered for this specific course in the Registration sheet
        var regSheet = ss.getSheetByName("Registration");
        if (regSheet) {
          var regData = regSheet.getDataRange().getValues();
          for (var j = 1; j < regData.length; j++) {
            var regPhone = regData[j][3] ? regData[j][3].toString().trim() : "";
            var regCourse = regData[j][5] ? regData[j][5].toString().trim() : "";
            if (regPhone === phone.toString().trim() && regCourse === code.toString().trim()) {
              return finalize(callback, {success: false, error: "Already registered for this course"});
            }
          }
          // Only show registration on the registration sheet
          var now = Utilities.formatDate(new Date(), "GMT+5:30", "yyyy-MM-dd HH:mm:ss");
          var branch = e.parameter.branch || "General";
          regSheet.appendRow([now, name, gmail, phone, branch, code]);
        }
      }
      
      return finalize(callback, {
        success: true, 
        message: "Registration Successful"
      });
    }

    // 2. LOGIN ACTION
    if (action === "login") {
      var phone = e.parameter.phone || "";
      var pass = e.parameter.password || "";
      var found = false;
      var userName = "";
      var userGmail = "";
      var enrollments = [];

      // First check Login sheet
      for (var i = 1; i < data.length; i++) {
        var rowPhone = data[i][1] ? data[i][1].toString().trim() : "";
        var rowPass = data[i][4] ? data[i][4].toString().trim() : "";
        var rowCourse = data[i][2] ? data[i][2].toString().trim() : "";
        
        if (rowPhone === phone.toString().trim()) {
          if (pass === "BYPASS_SYNC" || rowPass === pass.toString().trim()) {
            found = true;
            if (!userName) userName = data[i][0];
            if (!userGmail) userGmail = data[i][3] || "";
            if (rowCourse && enrollments.indexOf(rowCourse) === -1) enrollments.push(rowCourse);
          }
        }
      }

      // If BYPASS_SYNC, we allow finding user from Registration sheet even if they aren't in Login sheet
      if (pass === "BYPASS_SYNC") found = true;

      // Always scan Registration sheet for courses belonging to this phone number
      if (found) {
        var regSheet = ss.getSheetByName("Registration");
        if (regSheet) {
          var regData = regSheet.getDataRange().getValues();
          for (var j = 1; j < regData.length; j++) {
            var regPhone = regData[j][3] ? regData[j][3].toString().trim() : "";
            var regCourse = regData[j][5] ? regData[j][5].toString().trim() : "";
            if (regPhone === phone.toString().trim()) {
              if (!userName && regData[j][1]) userName = regData[j][1]; // Get name from reg sheet if missing
              if (!userGmail && regData[j][2]) userGmail = regData[j][2]; // Get email from reg sheet if missing
              if (regCourse && enrollments.indexOf(regCourse) === -1) {
                enrollments.push(regCourse);
              }
            }
          }
        }

        // Only return success if we actually found them in Login sheet OR if BYPASS_SYNC found courses
        if (pass === "BYPASS_SYNC" && enrollments.length === 0 && !userName) {
            return finalize(callback, {exists: false, success: false, error: "Not found"});
        }

        return finalize(callback, {
          exists: true, 
          success: true, 
          name: userName || "Student",
          gmail: userGmail,
          classCode: enrollments.length > 0 ? enrollments[0] : "", // backward compatibility
          enrollments: enrollments
        });
      }
      return finalize(callback, {exists: false, success: false, error: "Incorrect Phone or Password"});
    }

    // 3. RECOVER ACTION
    if (action === "recover") {
      var phone = e.parameter.phone || "";
      for (var i = 1; i < data.length; i++) {
        var rowPhone = data[i][1] ? data[i][1].toString().trim() : "";
        if (rowPhone === phone.toString().trim()) {
          return finalize(callback, {recovered: true, success: true});
        }
      }
      return finalize(callback, {recovered: false, success: false, error: "Phone not found"});
    }

    // 4. RESET ACTION
    if (action === "reset") {
      var phone = e.parameter.phone || "";
      var newPass = e.parameter.password || "";
      for (var i = 1; i < data.length; i++) {
        var rowPhone = data[i][1] ? data[i][1].toString().trim() : "";
        if (rowPhone === phone.toString().trim()) {
          sheet.getRange(i + 1, 5).setValue(newPass);
          return finalize(callback, {success: true});
        }
      }
      return finalize(callback, {success: false, error: "Reset failed"});
    }

    // 5. COURSE REGISTER ACTION (Access Code Validation)
    if (action === "courseRegister") {
      var name = e.parameter.name || "Unknown";
      var gmail = e.parameter.email || "Missing";
      var phone = e.parameter.phone || "";
      var course = e.parameter.course || "";
      var accessCode = e.parameter.accessCode || "";

      if (!phone || !accessCode || !course) {
        return finalize(callback, {success: false, error: "Phone, Course, and Access Code are required"});
      }

      // Read Access Code Sheet
      var accessSheet = ss.getSheetByName("Access Code");
      if (!accessSheet) {
        return finalize(callback, {success: false, error: "Configuration Error: Access Code sheet missing"});
      }
      
      var accessData = accessSheet.getDataRange().getValues();
      var codeValid = false;
      var codeFound = false;

      // Loop rows (assuming Row 1 is header: Course Name, Access Code, Expiry Date)
      for (var i = 1; i < accessData.length; i++) {
        var rowCourse = accessData[i][0] ? accessData[i][0].toString().trim() : "";
        var rowCode = accessData[i][1] ? accessData[i][1].toString().trim() : "";
        var rowExpiry = accessData[i][2]; // Date object or string

        if (rowCode === accessCode.toString().trim()) {
          codeFound = true;
          
          // Check Course Match
          if (rowCourse !== course.toString().trim()) {
            return finalize(callback, {success: false, error: "Access Code is not valid for this course"});
          }

          // Check Expiry
          if (rowExpiry) {
            var expiryDate = new Date(rowExpiry);
            var now = new Date();
            // Optional: reset time to midnight for pure date comparison, or compare strictly
            if (now > expiryDate) {
              return finalize(callback, {success: false, error: "Access Code has expired"});
            }
          }

          // If we reach here, it's valid
          codeValid = true;
          break;
        }
      }

      if (!codeFound) {
        return finalize(callback, {success: false, error: "Invalid Access Code"});
      }

      if (codeValid) {
        // Record registration in the Login sheet
        var loginSheet = ss.getSheetByName("Login") || ss.getActiveSheet();
        loginSheet.appendRow([name, phone, course, gmail, ""]); // Leaving password blank or generic
        
        return finalize(callback, {success: true, message: "Registration successful"});
      }
    }

    // 6. SUBMIT SCORE ACTION
    if (action === "submitScore") {
      var phone = e.parameter.phone || "";
      var name = e.parameter.name || "Unknown";
      var score = e.parameter.score || "0";
      var moduleID = e.parameter.moduleID || ""; 
      var classCode = e.parameter.classCode || "";
      var gmail = e.parameter.gmail || "";
      var startTime = e.parameter.startTime || null;
      
      if (!phone) return finalize(callback, {success: false, error: "Phone required"});

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
      var timeValue = Utilities.formatDate(now, "GMT+5:30", "yyyy-MM-dd HH:mm:ss"); // Default to timestamp if no startTime
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
        else return finalize(callback, {success: false, error: "Invalid Mock ID"});
      } else {
        var num = parseInt(moduleID);
        if (!isNaN(num) && num >= 1 && num <= 6) {
          scoreCol = (num - 1) * 2 + 5;
          timeCol = (num - 1) * 2 + 6;
        } else {
          return finalize(callback, {success: false, error: "Invalid Module ID"});
        }
      }

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

      return finalize(callback, {success: true, message: "Score and time updated for " + moduleID});
    }

    // 7. LOG QUIZ ACTION (For detailed logging)
    if (action === "logQuiz") {
      var phone = e.parameter.phone || "";
      var name = e.parameter.name || "Unknown";
      var moduleName = e.parameter.module || "";
      var mark = e.parameter.mark || "0";
      var maxMark = e.parameter.maxMark || "0";
      
      if (!phone) return finalize(callback, {success: false, error: "Phone required"});
      
      var logSheet = ss.getSheetByName("Results data analytics");
      if (!logSheet) {
        logSheet = ss.insertSheet("Results data analytics");
        logSheet.appendRow(["Time Stamp", "Phone Number", "Name", "Module", "Mark", "Maximum Mark"]);
      }
      
      var now = new Date();
      var timeStamp = Utilities.formatDate(now, "GMT+5:30", "yyyy-MM-dd HH:mm:ss");
      
      logSheet.appendRow([timeStamp, phone, name, moduleName, mark, maxMark]);
      
      return finalize(callback, {success: true, message: "Logged to Results data analytics"});
    }

    // 5. GET SCORES ACTION (For syncing progress)
    if (action === "getScores") {
      var phone = e.parameter.phone || "";
      if (!phone) return finalize(callback, {success: false, error: "Phone required"});

      var logSheet = ss.getSheetByName("Results data analytics");
      var scores = {};

      if (logSheet) {
        var logData = logSheet.getDataRange().getValues();
        for (var i = 1; i < logData.length; i++) {
          var rowPhone = logData[i][1] ? logData[i][1].toString().trim() : "";
          if (rowPhone === phone.toString().trim()) {
            var moduleName = logData[i][3] || ""; // e.g. "M1 Assessment"
            var mark = parseFloat(logData[i][4]) || 0;
            var maxMark = parseFloat(logData[i][5]) || 1;
            var percentage = (mark / maxMark) * 100;

            // Map "M1 Assessment" -> "1", "Mock Test 1" -> "mock1" etc.
            var key = "";
            if (moduleName.includes("Mock")) {
               key = "mock" + moduleName.replace(/[^0-9]/g, "");
               if (moduleName.toLowerCase().includes("data")) key = "da_" + key;
            } else {
               key = moduleName.replace(/[^0-9]/g, ""); // "M1 Assessment" -> "1"
               // Handle data analytics prefix if needed
               if (moduleName.toLowerCase().includes("data")) key = "data" + key;
            }

            if (!scores[key] || percentage > scores[key]) {
              scores[key] = percentage;
            }
          }
        }
      }
      return finalize(callback, {success: true, scores: scores});
    }
    
    return finalize(callback, {success: false, error: "Invalid Action"});

  } catch (err) {
    return finalize(callback, {success: false, error: "Script Error: " + err.message});
  }
}

function finalize(callback, data) {
  var out = JSON.stringify(data);
  if (callback) {
    return ContentService.createTextOutput(callback + "(" + out + ")").setMimeType(ContentService.MimeType.JAVASCRIPT);
  }
  return ContentService.createTextOutput(out).setMimeType(ContentService.MimeType.JSON);
}
