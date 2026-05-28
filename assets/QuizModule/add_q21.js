const fs = require('fs');

function addQuestionsToFile(filename, isUtf16) {
    let input = fs.readFileSync(filename, isUtf16 ? 'utf16le' : 'utf8');
    let moduleFormat = input.replace(/(const|var|let)\s+[a-zA-Z0-9_]+\s*=/, 'module.exports =');
    fs.writeFileSync('temp_add_q21.js', moduleFormat, 'utf8');
    delete require.cache[require.resolve('./temp_add_q21.js')];
    const quizData = require('./temp_add_q21.js');

    const q21 = {
        id: 21,
        type: "MCQ",
        q: "You want to know whether there is significant difference between the average test scores of male and female students in the same class. You check that the data is approximately normally distributed for each group has similar variance.<br><br>How would you decide whether the difference in the test score between male and female students is significant?",
        options: [
            "Perform a t-test using the means and variance for male and female students and if p-value is greater than 0.05 decide that the difference is significant.",
            "Perform a t-test using the medians and variance for male and female students and if p-value is less than 0.05 decide that the difference is significant.",
            "Perform a t-test using the medians and variance for male and female students and if p-value is greater than 0.05 decide that the difference is significant.",
            "Perform a t-test using the means and variance for male and female students and if p-value is less than 0.05 decide that the difference is significant."
        ],
        a: 3,
        marks: 2
    };

    if (!quizData.da_mock3) quizData.da_mock3 = [];
    quizData.da_mock3 = quizData.da_mock3.filter(q => q.id !== 21);
    quizData.da_mock3.push(q21);
    quizData.da_mock3.sort((a, b) => a.id - b.id);

    let finalJson = JSON.stringify(quizData, null, 4);
    let varName = input.includes("var dataQuizData") ? "dataQuizData" : "quizData";
    let finalJs = (varName === "dataQuizData" ? "var dataQuizData = " : "const quizData = ") + finalJson + ";\n";
    fs.writeFileSync(filename, finalJs, isUtf16 ? 'utf16le' : 'utf8');
}

addQuestionsToFile('quiz_data.js', false);
addQuestionsToFile('data_quiz_data.js', true);
addQuestionsToFile('data_quiz_data_utf8.js', false);
console.log("Successfully added Q21!");
