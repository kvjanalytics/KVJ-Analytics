const fs = require('fs');

function addQuestionsToFile(filename, isUtf16) {
    let input = fs.readFileSync(filename, isUtf16 ? 'utf16le' : 'utf8');
    
    let moduleFormat = input.replace(/(const|var|let)\s+[a-zA-Z0-9_]+\s*=/, 'module.exports =');
    fs.writeFileSync('temp_add_q23.js', moduleFormat, 'utf8');
    
    delete require.cache[require.resolve('./temp_add_q23.js')];
    const quizData = require('./temp_add_q23.js');
    
    const q2 = {
        id: 2,
        type: "MCQ",
        q: "You have been given a large data set that includes location , income , and age. why should you disaggregate the data ?",
        options: [
            "To hide difference among subgroups",
            "To combine data sets and present a summary of your findings",
            "To form generalization about the entire data set",
            "To analyze income within different age groups or locations"
        ],
        a: 3,
        marks: 2
    };

    const q3 = {
        id: 3,
        type: "MCQ",
        q: "For which scenario should you use a line chart to represent the data",
        options: [
            "The weekly average stock price during a one-year period",
            "The proportion of yes and no answer to a survey question",
            "The binned distribution for the height of different students",
            "The maximum, minimum, and average value for a set of data"
        ],
        a: 0,
        marks: 2
    };

    if (!quizData.da_mock3) quizData.da_mock3 = [];
    
    // Check if they exist
    quizData.da_mock3 = quizData.da_mock3.filter(q => q.id !== 2 && q.id !== 3);
    
    quizData.da_mock3.push(q2);
    quizData.da_mock3.push(q3);
    
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

console.log("Successfully added Q2 and Q3 to da_mock3");
