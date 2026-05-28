const fs = require('fs');

function addQuestionsToFile(filename, isUtf16) {
    let input = fs.readFileSync(filename, isUtf16 ? 'utf16le' : 'utf8');
    let moduleFormat = input.replace(/(const|var|let)\s+[a-zA-Z0-9_]+\s*=/, 'module.exports =');
    fs.writeFileSync('temp_add_q910.js', moduleFormat, 'utf8');
    delete require.cache[require.resolve('./temp_add_q910.js')];
    const quizData = require('./temp_add_q910.js');

    const q9 = {
        id: 9,
        type: "MCQ",
        q: "You create the column chart below, which shows sales for different years. Management asks for a way to see demographic information associated with the individual sales records for each year.<br><br>You decide to create tables for each year that show the demographic information for the sales in that year. When someone clicks, the associated table will open.<br><br>Which reporting technique does this represent?",
        img: "sales_by_year_column.png",
        options: [
            "Disaggregating",
            "Unpivoting",
            "Pivoting",
            "Distributing"
        ],
        a: 0,
        marks: 1
    };

    const q10 = {
        id: 10,
        type: "MTF",
        q: "Match the type of data analysis on the left to the analysis question it answers on the right. You may use each item once or not at all.<br><br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct response.</span>",
        options: [
            "What happened?",
            "Why did it happen?",
            "What should we do next?",
            "Is there enough evidence to draw conclusin?"
        ],
        labels: [
            "Descriptive analysis",
            "Diagnostic analysis",
            "Predictive analysis",
            "Prescriptive analysis",
            "Hypothesis Testing"
        ],
        a: {
            "What happened?": "Descriptive analysis",
            "Why did it happen?": "Diagnostic analysis",
            "What should we do next?": "Prescriptive analysis",
            "Is there enough evidence to draw conclusin?": "Hypothesis Testing"
        },
        marks: 2
    };

    if (!quizData.da_mock3) quizData.da_mock3 = [];
    quizData.da_mock3 = quizData.da_mock3.filter(q => q.id !== 9 && q.id !== 10);
    quizData.da_mock3.push(q9, q10);
    quizData.da_mock3.sort((a, b) => a.id - b.id);

    let finalJson = JSON.stringify(quizData, null, 4);
    let varName = input.includes("var dataQuizData") ? "dataQuizData" : "quizData";
    let finalJs = (varName === "dataQuizData" ? "var dataQuizData = " : "const quizData = ") + finalJson + ";\n";
    fs.writeFileSync(filename, finalJs, isUtf16 ? 'utf16le' : 'utf8');
}

addQuestionsToFile('quiz_data.js', false);
addQuestionsToFile('data_quiz_data.js', true);
addQuestionsToFile('data_quiz_data_utf8.js', false);
console.log("Successfully added Q9 and Q10!");
