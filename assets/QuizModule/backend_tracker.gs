// backend_tracker.gs

// REQUIRED STEPS TO CONNECT YOUR SPREADSHEET:
// 1. Open your Google Sheet: https://docs.google.com/spreadsheets/d/1AFJMPJW4wOGa1WgQIbTSlhBBqaHnBcY5HRpfROTBQqg/edit
// 2. Click "Extensions" > "Apps Script" inside the Google Sheet menu.
// 3. Delete any code there, and PASTE everything in this file into the editor.
// 4. Click the "Save" icon (disk).
// 5. Click the "Deploy" button at the top right > "New deployment".
//    - Select type: "Web app"
//    - Description: "Score Tracker"
//    - Execute as: "Me"
//    - Who has access: "Anyone"
// 6. Click "Deploy". You might have to authorize permissions to edit your sheet.
// 7. COPY the "Web app URL" it gives you! 
// 8. Paste that URL into the SCRIPT_URL variable in the assessment HTML files.

function doPost(e) {
  return handleRequest(e);
}

function doGet(e) {
  return handleRequest(e);
}

function handleRequest(e) {
  try {
    // 1. Get the Active Sheet
    var sheet = SpreadsheetApp.getActiveSpreadsheet().getActiveSheet();
    
    // 2. Extract parameters from the incoming request
    var phone = e.parameter.phone || "N/A";
    var name = e.parameter.name || "N/A";
    var module = e.parameter.module || "Unknown Module";
    var mark = e.parameter.mark || "0";
    var maximum = e.parameter.maximum || "0";
    
    // 3. Generate Timestamp
    var timestamp = new Date();
    
    // 4. Append the row: Time Stamp, Phone Number, Name, Module, Mark, Maximum Mark
    sheet.appendRow([timestamp, phone, name, module, mark, maximum]);
    
    // 5. Return success JSON
    var output = ContentService.createTextOutput(JSON.stringify({"success": true}));
    output.setMimeType(ContentService.MimeType.JSON);
    
    return output;
  } catch (error) {
    var errOutput = ContentService.createTextOutput(JSON.stringify({"success": false, "error": error.toString()}));
    errOutput.setMimeType(ContentService.MimeType.JSON);
    return errOutput;
  }
}
