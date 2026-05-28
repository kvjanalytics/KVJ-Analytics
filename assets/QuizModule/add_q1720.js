const fs = require('fs');

function addQuestionsToFile(filename, isUtf16) {
    let input = fs.readFileSync(filename, isUtf16 ? 'utf16le' : 'utf8');
    let moduleFormat = input.replace(/(const|var|let)\s+[a-zA-Z0-9_]+\s*=/, 'module.exports =');
    fs.writeFileSync('temp_add_q1720.js', moduleFormat, 'utf8');
    delete require.cache[require.resolve('./temp_add_q1720.js')];
    const quizData = require('./temp_add_q1720.js');

    const newQs = [
        {
            id: 17,
            type: "MCQ3",
            q: "You are tasked with completing a data analysis project for a large organization. During the project, you must handle personally identifiable information (PII)<br><br>Throughout the project which three principle should you follow? (Choose 3)<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>",
            options: [
                "Limit your handling of the PII to only what is necessary for the current analysis.",
                "Remove all PII from your computer after the analysis is complete",
                "Retain only the PII that you might need for future analysis.",
                "Request all data from the database that contains the POI.",
                "Keep track of the PII that you have during the analysis."
            ],
            a: [0, 1, 4],
            marks: 2
        },
        {
            id: 18,
            type: "MCQ",
            q: "You will be analyzing sales and determining trends based on a very large dataset that includes the following columns:<br><ul><li>CustomerName</li><li>CustomerEmail</li><li>Birthdate</li><li>FirstPurchaseDate</li><li>MostRecentPurchaseDate</li><li>TotalQuantityPurchased</li><li>TotalsalesAmount</li></ul>You need to validate the data before you start analysis.<br>What should you do?",
            options: [
                "Analyze firstPurchaseDates to determine purchasing trends",
                "Calculate statistics TotalQuantityPurchased",
                "Verify date ranges and value for all dates column",
                "Create aggregation of all new column"
            ],
            a: 2,
            marks: 2
        },
        {
            id: 19,
            type: "MCQ",
            q: "Which concept most comprehensively describe the general meaning of data in the context of data analytics?",
            options: [
                "Unprocessed data",
                "Interpreted evidence",
                "Meaningful statistics",
                "Analyzed details"
            ],
            a: 0,
            marks: 2
        },
        {
            id: 20,
            type: "MCQ",
            q: "A data scientist at your company creates a machine learning model to help the hiring manager select candidates from thousands of job applicants. Which statement best describes how machine learning is used in this scenario?",
            options: [
                "A machine learning model defines the qualifications necessary for a given job or role",
                "The machine learning model uses historical data and algorithm to predict future applicant performance",
                "The machine learning system coverts applicant information into a common format",
                "The hiring manager queries the machine learning database for qualified applicant"
            ],
            a: 1,
            marks: 2
        }
    ];

    if (!quizData.da_mock3) quizData.da_mock3 = [];
    const ids = newQs.map(q => q.id);
    quizData.da_mock3 = quizData.da_mock3.filter(q => !ids.includes(q.id));
    quizData.da_mock3.push(...newQs);
    quizData.da_mock3.sort((a, b) => a.id - b.id);

    let finalJson = JSON.stringify(quizData, null, 4);
    let varName = input.includes("var dataQuizData") ? "dataQuizData" : "quizData";
    let finalJs = (varName === "dataQuizData" ? "var dataQuizData = " : "const quizData = ") + finalJson + ";\n";
    fs.writeFileSync(filename, finalJs, isUtf16 ? 'utf16le' : 'utf8');
}

addQuestionsToFile('quiz_data.js', false);
addQuestionsToFile('data_quiz_data.js', true);
addQuestionsToFile('data_quiz_data_utf8.js', false);
console.log("Successfully added Q17-Q20!");
