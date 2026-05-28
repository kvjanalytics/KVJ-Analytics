const fs = require('fs');

function addQuestionToFile(filename, isUtf16) {
    let input = fs.readFileSync(filename, isUtf16 ? 'utf16le' : 'utf8');
    
    // Convert to module for required
    let moduleFormat = input.replace(/(const|var|let)\s+[a-zA-Z0-9_]+\s*=/, 'module.exports =');
    fs.writeFileSync('temp_add_q1.js', moduleFormat, 'utf8');
    
    // Clear node require cache to reload properly
    delete require.cache[require.resolve('./temp_add_q1.js')];
    const quizData = require('./temp_add_q1.js');
    
    const newQuestion = {
        id: 1,
        type: "TF",
        q: "For each statement about data mining, select True or False.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>",
        options: [
            "Data mining is used to find anomalies",
            "Data mining is used to summarize raw data from large data sets",
            "Data mining is used to review underlying details in a given table"
        ],
        a: [true, true, false],
        marks: 2
    };

    quizData.da_mock3 = [newQuestion];

    let finalJson = JSON.stringify(quizData, null, 4);
    
    // Detect var name used originally
    let varName = "quizData";
    if (input.includes("var dataQuizData")) {
        varName = "dataQuizData";
    }
    
    let finalJs = (varName === "dataQuizData" ? "var dataQuizData = " : "const quizData = ") + finalJson + ";\n";
    fs.writeFileSync(filename, finalJs, isUtf16 ? 'utf16le' : 'utf8');
}

addQuestionToFile('quiz_data.js', false);
addQuestionToFile('data_quiz_data.js', true);
addQuestionToFile('data_quiz_data_utf8.js', false);

console.log("Successfully added the new Question 1 to da_mock3");
