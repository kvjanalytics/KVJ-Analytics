/**
 * Google Apps Script to record registration data from the frontend.
 * 
 * Instructions:
 * 1. Open your Google Sheet: https://docs.google.com/spreadsheets/d/15TTEIqr7-uoURgVZXxQtGc7S5nzJT6TGvBreIugevt0/edit
 * 2. Go to 'Extensions' -> 'Apps Script'.
 * 3. Delete any code in the editor and paste this code.
 * 4. Click 'Deploy' -> 'New deployment'.
 * 5. Select type: 'Web app'.
 * 6. Set 'Execute as': 'Me'.
 * 7. Set 'Who has access': 'Anyone'.
 * 8. Deploy and copy the 'Web app URL'.
 * 9. Paste the URL into 'registration.html' in the 'SCRIPT_URL' variable.
 */

function doPost(e) {
  try {
    const sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
    const data = JSON.parse(e.postData.contents);
    
    // Check if sheet has data
    const lastRow = sheet.getLastRow();
    
    if (lastRow > 0) {
      const range = sheet.getRange(1, 1, lastRow, 6);
      const values = range.getValues();
      
      const emailCol = 2; // Column C (0-indexed is 2)
      const phoneCol = 3; // Column D (0-indexed is 3)
      const courseCol = 5; // Column F (0-indexed is 5)
      
      for (let i = 1; i < values.length; i++) {
        const isSameStudent = (values[i][emailCol] === data.email || values[i][phoneCol] === data.phone);
        const isSameCourse = (values[i][courseCol] === data.course);

        if (isSameStudent && isSameCourse) {
          return ContentService.createTextOutput(JSON.stringify({ 
            status: "duplicate", 
            message: "You are already registered for the " + data.course + " course." 
          }))
          .setMimeType(ContentService.MimeType.JSON);
        }
      }
    } else {
      // Add headers if sheet is empty
      sheet.appendRow(["Timestamp", "Full Name", "Email Address", "Phone Number", "Branch / Specialization", "Selected Course"]);
    }
    
    // Append the registration data
    sheet.appendRow([
      data.timestamp,
      data.fullName,
      data.email,
      data.phone,
      data.branch,
      data.course
    ]);
    
    return ContentService.createTextOutput(JSON.stringify({ status: "success" }))
      .setMimeType(ContentService.MimeType.JSON);
      
  } catch (error) {
    return ContentService.createTextOutput(JSON.stringify({ status: "error", message: error.toString() }))
      .setMimeType(ContentService.MimeType.JSON);
  }
}
