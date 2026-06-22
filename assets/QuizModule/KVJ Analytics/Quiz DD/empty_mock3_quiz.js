const fs = require('fs');

let input = fs.readFileSync('quiz_data.js', 'utf8');
// The file probably uses `const quizData =`
input = input.replace(/(const|var|let)\s+quizData\s*=/, 'module.exports =');
fs.writeFileSync('temp_quiz_empty.js', input);

const quizData = require('./temp_quiz_empty.js');
if (quizData.da_mock3) {
    quizData.da_mock3 = []; // Empty out the questions
}

let finalJson = JSON.stringify(quizData, null, 4);
let finalJs = "const quizData = " + finalJson + ";\n";

fs.writeFileSync('quiz_data.js', finalJs, 'utf8');

console.log("Completely removed all questions from da_mock3 in quiz_data.js");
