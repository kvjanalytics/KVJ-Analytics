const fs = require('fs');

function addQuestionsToFile(filename, isUtf16) {
    let input = fs.readFileSync(filename, isUtf16 ? 'utf16le' : 'utf8');
    let moduleFormat = input.replace(/(const|var|let)\s+[a-zA-Z0-9_]+\s*=/, 'module.exports =');
    fs.writeFileSync('temp_add_q1116.js', moduleFormat, 'utf8');
    delete require.cache[require.resolve('./temp_add_q1116.js')];
    const quizData = require('./temp_add_q1116.js');

    const newQs = [
        {
            id: 11,
            type: "MCQ",
            q: "Which data type results from processing conditional statement?",
            options: ["Boolean", "Integer", "character", "String"],
            a: 0,
            marks: 2
        },
        {
            id: 12,
            type: "MCQ",
            q: "What type of data is too complex to be sorted in traditional data base management system (DBMS)?",
            options: ["Imputed data", "Metadata", "Qualitative data", "Big data"],
            a: 3,
            marks: 2
        },
        {
            id: 13,
            type: "MCQ",
            q: "Which data type is appropriate for a phone number using the format (###) ### - ###-####?",
            options: ["Numeric", "String", "Boolean", "Binary"],
            a: 1,
            marks: 2
        },
        {
            id: 14,
            type: "MCQ2",
            q: "In the United state and Europe which two data points are considered non-sensitive PII(personal identifiable information)? (choose 2)<br><br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>",
            options: ["Bank account number", "Medical records", "Date of birth", "Job title"],
            a: [2, 3],
            marks: 2
        },
        {
            id: 15,
            type: "MCQ",
            q: "What is an example of machine learning in predictive analysis?",
            options: [
                "Your thermostat adjusts to a higher temperature because you programmed it based on the time of day",
                "Your streaming service suggests a category Of movies based on the last ten movies you watched.",
                "Your vehicle turns on a warning sensor because one of its components requires maintenance.",
                "Your computer automatically goes into sleep mode because the battery has less than ten pecent power."
            ],
            a: 1,
            marks: 2
        },
        {
            id: 16,
            type: "MCQ",
            q: "How is an unstructured data set different from structured data set",
            options: [
                "An unstructured data set can be quickly searched without manipulation.",
                "The data organization of an unstructured data set is explicitly defined",
                "An unstructured data set has a predefined data model.",
                "An unstructured data set can store large amounts of unrelated data."
            ],
            a: 3,
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
console.log("Successfully added Q11-Q16!");
