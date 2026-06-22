const fs = require('fs');

function addQuestionsToFile(filename, isUtf16) {
    let input = fs.readFileSync(filename, isUtf16 ? 'utf16le' : 'utf8');
    let moduleFormat = input.replace(/(const|var|let)\s+[a-zA-Z0-9_]+\s*=/, 'module.exports =');
    fs.writeFileSync('temp_add_q22.js', moduleFormat, 'utf8');
    delete require.cache[require.resolve('./temp_add_q22.js')];
    const quizData = require('./temp_add_q22.js');

    const q22 = {
        id: 22,
        type: "MCQ",
        q: "Which sentence most accurately describes the relationship between data and statistics?",
        options: [
            "All statistics are data, but not all data are statistics",
            "All data are statistics but not all statistics are data",
            "Data and statistics are both purely quantitative in nature",
            "Data and statistics are both purely qualitative in nature"
        ],
        a: 0,
        marks: 2
    };

    if (!quizData.da_mock3) quizData.da_mock3 = [];
    quizData.da_mock3 = quizData.da_mock3.filter(q => q.id !== 22);
    quizData.da_mock3.push(q22);
    quizData.da_mock3.sort((a, b) => a.id - b.id);

    let finalJson = JSON.stringify(quizData, null, 4);
    let varName = input.includes("var dataQuizData") ? "dataQuizData" : "quizData";
    let finalJs = (varName === "dataQuizData" ? "var dataQuizData = " : "const quizData = ") + finalJson + ";\n";
    fs.writeFileSync(filename, finalJs, isUtf16 ? 'utf16le' : 'utf8');
}

addQuestionsToFile('quiz_data.js', false);
addQuestionsToFile('data_quiz_data.js', true);
addQuestionsToFile('data_quiz_data_utf8.js', false);
console.log("Successfully added Q22!");
