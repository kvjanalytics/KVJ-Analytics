const fs = require('fs');

let input = fs.readFileSync('data_quiz_data_utf8.js', 'utf8');
input = input.replace(/(const|var|let)\s+[a-zA-Z0-9_]+\s*=/, 'module.exports =');
fs.writeFileSync('temp_data_empty.js', input);

const quizData = require('./temp_data_empty.js');
quizData.da_mock3 = []; // Empty out the questions

let finalJson = JSON.stringify(quizData, null, 4);
let finalJs = "var dataQuizData = " + finalJson + ";\n";

fs.writeFileSync('data_quiz_data_utf8.js', finalJs, 'utf8');
fs.writeFileSync('data_quiz_data.js', Buffer.from(finalJs, 'utf16le'));

console.log("Completely removed all questions from da_mock3");
