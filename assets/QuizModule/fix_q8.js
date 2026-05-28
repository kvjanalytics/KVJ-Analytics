const fs = require('fs');

function fixQ8(filename, isUtf16) {
    let input = fs.readFileSync(filename, isUtf16 ? 'utf16le' : 'utf8');
    let moduleFormat = input.replace(/(const|var|let)\s+[a-zA-Z0-9_]+\s*=/, 'module.exports =');
    fs.writeFileSync('temp_fix_q8.js', moduleFormat, 'utf8');
    delete require.cache[require.resolve('./temp_fix_q8.js')];
    const quizData = require('./temp_fix_q8.js');

    const q8 = quizData.da_mock3.find(q => q.id === 8);
    if (q8) {
        q8.optionImages = ["v3_q11_opt1.png", "v3_q11_opt2.png", "v3_q11_opt3.png", "v3_q11_opt4.png"];
        q8.a = 3;
    }

    let finalJson = JSON.stringify(quizData, null, 4);
    let varName = input.includes("var dataQuizData") ? "dataQuizData" : "quizData";
    let finalJs = (varName === "dataQuizData" ? "var dataQuizData = " : "const quizData = ") + finalJson + ";\n";
    fs.writeFileSync(filename, finalJs, isUtf16 ? 'utf16le' : 'utf8');
}

fixQ8('quiz_data.js', false);
fixQ8('data_quiz_data.js', true);
fixQ8('data_quiz_data_utf8.js', false);
console.log("Fixed Q8 image references!");
