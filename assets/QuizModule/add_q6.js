const fs = require('fs');

function addQuestionsToFile(filename, isUtf16) {
    let input = fs.readFileSync(filename, isUtf16 ? 'utf16le' : 'utf8');
    let moduleFormat = input.replace(/(const|var|let)\s+[a-zA-Z0-9_]+\s*=/, 'module.exports =');
    fs.writeFileSync('temp_add_q6.js', moduleFormat, 'utf8');
    delete require.cache[require.resolve('./temp_add_q6.js')];
    const quizData = require('./temp_add_q6.js');
    
    const q6 = {
        id: 6,
        type: "TF",
        q: "You have a data set of 100,000 rows. The data values fall within a standard range. The data has been cleaned to remove outliers. Approximately 100 rows of the data set contain NULL values in a numeric data column. You need to determine a best practice for handling the NULL values.<br><br>For each statement about handling NULL, select <strong>Yes</strong> if it is a best practice or <strong>No</strong> if it is not.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>",
        options: [
            "Remove the row that contains Null values",
            "Remove each Null value with a random value",
            "Use a statistic such as average to account for the Null values"
        ],
        a: [false, false, true],
        marks: 2
    };

    if (!quizData.da_mock3) quizData.da_mock3 = [];
    quizData.da_mock3 = quizData.da_mock3.filter(q => q.id !== 6);
    quizData.da_mock3.push(q6);
    quizData.da_mock3.sort((a, b) => a.id - b.id);

    let finalJson = JSON.stringify(quizData, null, 4);
    let varName = input.includes("var dataQuizData") ? "dataQuizData" : "quizData";
    let finalJs = (varName === "dataQuizData" ? "var dataQuizData = " : "const quizData = ") + finalJson + ";\n";
    fs.writeFileSync(filename, finalJs, isUtf16 ? 'utf16le' : 'utf8');
}

addQuestionsToFile('quiz_data.js', false);
addQuestionsToFile('data_quiz_data.js', true);
addQuestionsToFile('data_quiz_data_utf8.js', false);
console.log("Successfully added Q6!");
