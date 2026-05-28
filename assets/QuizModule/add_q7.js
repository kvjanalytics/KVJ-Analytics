const fs = require('fs');

function addQuestionsToFile(filename, isUtf16) {
    let input = fs.readFileSync(filename, isUtf16 ? 'utf16le' : 'utf8');
    let moduleFormat = input.replace(/(const|var|let)\s+[a-zA-Z0-9_]+\s*=/, 'module.exports =');
    fs.writeFileSync('temp_add_q7.js', moduleFormat, 'utf8');
    delete require.cache[require.resolve('./temp_add_q7.js')];
    const quizData = require('./temp_add_q7.js');
    
    const q7 = {
        id: 7,
        type: "MTF",
        q: "Your marketing department attends a variety of events each year and distributes promotional items to event participants. The table below shows the quantity distributed of each promotional item.<br><br><table style='width:100%; border-collapse: collapse; margin: 15px 0; font-size: 13px; text-align: center;'><thead><tr style='background: #f1f5f9;'><th style='padding: 8px; border: 1px solid #cbd5e1;'>Promotional item</th><th style='padding: 8px; border: 1px solid #cbd5e1;'>Quantity Distributed</th></tr></thead><tbody><tr><td style='padding:6px; border:1px solid #cbd5e1;'>T-shirt</td><td style='padding:6px; border:1px solid #cbd5e1;'>600</td></tr><tr><td style='padding:6px; border:1px solid #cbd5e1;'>Shuffled Animal</td><td style='padding:6px; border:1px solid #cbd5e1;'>425</td></tr><tr><td style='padding:6px; border:1px solid #cbd5e1;'>Drinkware</td><td style='padding:6px; border:1px solid #cbd5e1;'>550</td></tr><tr><td style='padding:6px; border:1px solid #cbd5e1;'>Backpacks</td><td style='padding:6px; border:1px solid #cbd5e1;'>100</td></tr><tr><td style='padding:6px; border:1px solid #cbd5e1;'>Blankets</td><td style='padding:6px; border:1px solid #cbd5e1;'>55</td></tr><tr><td style='padding:6px; border:1px solid #cbd5e1;'>Magnets</td><td style='padding:6px; border:1px solid #cbd5e1;'>250</td></tr><tr><td style='padding:6px; border:1px solid #cbd5e1;'>Gift cards</td><td style='padding:6px; border:1px solid #cbd5e1;'>50</td></tr><tr><td style='padding:6px; border:1px solid #cbd5e1;'>Candy</td><td style='padding:6px; border:1px solid #cbd5e1;'>500</td></tr><tr><td style='padding:6px; border:1px solid #cbd5e1;'>Notebooks</td><td style='padding:6px; border:1px solid #cbd5e1;'>450</td></tr></tbody></table><br>You are performing analysis on the data. Complete the sentence about the data organization by selecting the correct option from each drop-down list.<br><span style='font-size: 15px; font-style: italic;'>Note: You will receive partial credit for each correct selection.</span>",
        options: [
            "Can arrange distributed items from highest to lowest",
            "Can limit the display of distributed items to greater than 500",
            "Can limit the display of promotional items to shuffled animals and T-shirt"
        ],
        labels: ["Appending", "Filtering", "Sorting", "Truncating", "Transporting", "Slicing"],
        a: {
            "Can arrange distributed items from highest to lowest": "Sorting",
            "Can limit the display of distributed items to greater than 500": "Filtering",
            "Can limit the display of promotional items to shuffled animals and T-shirt": "Slicing"
        },
        marks: 2
    };

    if (!quizData.da_mock3) quizData.da_mock3 = [];
    quizData.da_mock3 = quizData.da_mock3.filter(q => q.id !== 7);
    quizData.da_mock3.push(q7);
    quizData.da_mock3.sort((a, b) => a.id - b.id);

    let finalJson = JSON.stringify(quizData, null, 4);
    let varName = input.includes("var dataQuizData") ? "dataQuizData" : "quizData";
    let finalJs = (varName === "dataQuizData" ? "var dataQuizData = " : "const quizData = ") + finalJson + ";\n";
    fs.writeFileSync(filename, finalJs, isUtf16 ? 'utf16le' : 'utf8');
}

addQuestionsToFile('quiz_data.js', false);
addQuestionsToFile('data_quiz_data.js', true);
addQuestionsToFile('data_quiz_data_utf8.js', false);
console.log("Successfully added Q7!");
