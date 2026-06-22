const fs = require('fs');

function addQuestionsToFile(filename, isUtf16) {
    let input = fs.readFileSync(filename, isUtf16 ? 'utf16le' : 'utf8');
    let moduleFormat = input.replace(/(const|var|let)\s+[a-zA-Z0-9_]+\s*=/, 'module.exports =');
    fs.writeFileSync('temp_add_q8.js', moduleFormat, 'utf8');
    delete require.cache[require.resolve('./temp_add_q8.js')];
    const quizData = require('./temp_add_q8.js');
    
    const q8 = {
        id: 8,
        type: "MCQ",
        q: "You are given a data set displaying the time of day and number of minutes customers waited in line for service. You need to remove bias from the results eliminating outliers.<br><br>Which visualization illustrates outliers in your dataset?<br>Select the correct Visualization in the answer area.",
        options: ["Option 1", "Option 2", "Option 3", "Option 4"],
        optionImages: ["q44_opt1.png", "q44_opt2.png", "q44_opt3.png", "q44_opt4.png"],
        a: 3,
        marks: 1
    };

    if (!quizData.da_mock3) quizData.da_mock3 = [];
    quizData.da_mock3 = quizData.da_mock3.filter(q => q.id !== 8);
    quizData.da_mock3.push(q8);
    quizData.da_mock3.sort((a, b) => a.id - b.id);

    let finalJson = JSON.stringify(quizData, null, 4);
    let varName = input.includes("var dataQuizData") ? "dataQuizData" : "quizData";
    let finalJs = (varName === "dataQuizData" ? "var dataQuizData = " : "const quizData = ") + finalJson + ";\n";
    fs.writeFileSync(filename, finalJs, isUtf16 ? 'utf16le' : 'utf8');
}

addQuestionsToFile('quiz_data.js', false);
addQuestionsToFile('data_quiz_data.js', true);
addQuestionsToFile('data_quiz_data_utf8.js', false);
console.log("Successfully added Q8!");
