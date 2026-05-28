const fs = require('fs');

function addQuestionsToFile(filename, isUtf16) {
    let input = fs.readFileSync(filename, isUtf16 ? 'utf16le' : 'utf8');
    
    let moduleFormat = input.replace(/(const|var|let)\s+[a-zA-Z0-9_]+\s*=/, 'module.exports =');
    fs.writeFileSync('temp_add_q45.js', moduleFormat, 'utf8');
    
    delete require.cache[require.resolve('./temp_add_q45.js')];
    const quizData = require('./temp_add_q45.js');
    
    const q4 = {
        id: 4,
        type: "TF",
        q: "For each statement about data organization, select True or False<br><br><span style='font-size: 15px; font-style: italic;'>Note : You will receive partial credit for each correct selection</span>",
        options: [
            "Slicer can be used to filter the data",
            "Sorts can be used to display a subset of data",
            "Filter can be used to display a subset of data"
        ],
        a: [true, false, true],
        marks: 2
    };

    const q5 = {
        id: 5,
        type: "MCQ2",
        q: "Which two chart types should you use to rank values in ascending or descending order ? (choose 2)<br><br><span style='font-size: 15px; font-style: italic;'>Note : You will receive partial credit for each correct selection</span>",
        options: [
            "Bar chart",
            "Column chart",
            "Line chart",
            "Bubble chart"
        ],
        a: [0, 1],
        marks: 2
    };

    if (!quizData.da_mock3) quizData.da_mock3 = [];
    quizData.da_mock3 = quizData.da_mock3.filter(q => q.id !== 4 && q.id !== 5);
    
    quizData.da_mock3.push(q4);
    quizData.da_mock3.push(q5);
    
    quizData.da_mock3.sort((a, b) => a.id - b.id);

    let finalJson = JSON.stringify(quizData, null, 4);
    
    let varName = "quizData";
    if (input.includes("var dataQuizData")) {
        varName = "dataQuizData";
    }
    
    let finalJs = (varName === "dataQuizData" ? "var dataQuizData = " : "const quizData = ") + finalJson + ";\n";
    fs.writeFileSync(filename, finalJs, isUtf16 ? 'utf16le' : 'utf8');
}

addQuestionsToFile('quiz_data.js', false);
addQuestionsToFile('data_quiz_data.js', true);
addQuestionsToFile('data_quiz_data_utf8.js', false);
console.log("Successfully added Q4 and Q5!");
