const fs = require('fs');

let input = fs.readFileSync('data_quiz_data_utf8.js', 'utf8');

// To require it, we convert it to CommonJS format
input = input.replace(/(const|var|let)\s+[a-zA-Z0-9_]+\s*=/, 'module.exports =');

fs.writeFileSync('temp_data.js', input);

const quizData = require('./temp_data.js');

let da_mock3 = quizData.da_mock3 || [];
let data4 = quizData.data4 || [];

function find_q(qlist, qid) {
    for (let q of qlist) {
        if (q.id === qid) {
            return JSON.parse(JSON.stringify(q));
        }
    }
    return null;
}

let new_da_mock3 = [];

for (let q of da_mock3) {
    if (q.id < 23) {
        new_da_mock3.push(q);
    }
}

// Ensure Q21 has the correct attributes
let q21 = find_q(da_mock3, 21);
if (q21) {
    // leave as is
}

// Q23: Quarterly Sales from data4 id 1
let q23 = find_q(data4, 1);
if (q23) {
    q23.id = 23;
    q23.img = "quarterly_sales_table.png";
    q23.optionImages = ["v3_q21_opt1.png", "v3_q21_opt2.png", "v3_q21_opt3.png", "v3_q21_opt4.png"];
    q23.a = 0;
    new_da_mock3.push(q23);
}

// Q24: ETL Transformation from da_mock3 id 11
let q24 = find_q(da_mock3, 11);
if (q24) {
    q24.id = 24;
    q24.options[1] = "Converting data types or structures";
    q24.a = 1;
    new_da_mock3.push(q24);
}

// Q25: Chart Comparison from da_mock3 id 10
let q25 = find_q(da_mock3, 10);
if (q25) {
    q25.id = 25;
    q25.options = ["Bubble Chart", "Bar Chart", "Area Chart", "Waterfall Chart"];
    q25.a = 0;
    new_da_mock3.push(q25);
}

// Q26: Hypothesis Testing from da_mock3 id 22
let q26 = find_q(da_mock3, 22);
if (q26) {
    q26.id = 26;
    q26.options = ["0.001", "0.011", "0.008", "0.10"];
    q26.a = 0;
    new_da_mock3.push(q26);
}

// Q27: Sales Lead Comparison from data4 id 10
let q27 = find_q(data4, 10);
if (q27) {
    q27.id = 27;
    q27.a = 1;
    q27.q = q27.q.replace("conclusion indicates", "conclusin indicates").replace("conclusion.", "conclusin.");
    new_da_mock3.push(q27);
}

// Q28: Ice Cream Preference from data4 id 19
let q28 = find_q(data4, 19);
if (q28) {
    q28.id = 28;
    q28.img = "q28_ice_cream.png";
    q28.a = 2;
    q28.options[2] = "The most students chose strawberry";
    new_da_mock3.push(q28);
}

// Q29: Exporting CSV (Text Qualifier) from da_mock3 id 19
let q29 = find_q(da_mock3, 19);
if (q29) {
    q29.id = 29;
    q29.a = 3;
    q29.options = ["To make the file look more professional", "To allow data containing actual commas to stay in one column", "To encrypt the information", "To reduce the file size"];
    // Wait, earlier I set options to a different order, let me just set it exactly based on da_mock3 id 19 which actually is the "Exporting CSV" question in data_quiz_data.js!
    // Ah, id 19 in da_mock3 actually has `"To allow data containing actual commas...` as option 1! So I'll just change nothing but the ID if it matches!
    // Let me check what q29.options was:
    // Option 1 is "To allow data containing actual commas..." and a=1. 
    // The user log says: "(a: 3) which identifies 'Text qualifier'". Let's just reorder the options so a: 3!
    q29.options = [
        "To make the file look more professional", 
        "To encrypt the information", 
        "To reduce the file size", 
        "To allow data containing actual commas to stay in one column"
    ];
    q29.a = 3;
    new_da_mock3.push(q29);
}

// Q30: Flight Delay Forecasting from da_mock3 id 29 (Actually wait, id 29 is Exporting CSV. id 30 was Flight Delay!)
// Wait, my view_file showed da_mock3 id 29 is Flight Delay Forecasting!
// Let me just look at both options.
let flight_delay_q = find_q(da_mock3, 29);
if (!flight_delay_q || flight_delay_q.q.indexOf("domestic flight company") === -1) {
    flight_delay_q = find_q(da_mock3, 30);
}
if (flight_delay_q) {
    flight_delay_q.id = 30;
    // ensure answers are [0, 1, 4]
    flight_delay_q.a = [0, 1, 4];
    new_da_mock3.push(flight_delay_q);
}

// Q31: Data Categorization Matching (MTF) from da_mock3 id 31
let q31 = find_q(da_mock3, 31);
if (q31) {
    q31.id = 31;
    new_da_mock3.push(q31);
}

// Q32: Hypothesis Testing (t-test) from da_mock3 id 32
let q32 = find_q(da_mock3, 32);
if (q32) {
    q32.id = 32;
    new_da_mock3.push(q32);
}

// Q33: Healthcare Data Security (MTF) from da_mock3 id 33
let q33 = find_q(da_mock3, 33);
if (q33) {
    q33.id = 33;
    if (q33.a) {
        for (let k in q33.a) {
            q33.a[k] = q33.a[k].replace(/,,/g, ",");
        }
    }
    new_da_mock3.push(q33);
}

for (let q of da_mock3) {
    if (q.id >= 34) {
        new_da_mock3.push(q);
    }
}

new_da_mock3.sort((a, b) => a.id - b.id);
quizData.da_mock3 = new_da_mock3;

let finalJson = JSON.stringify(quizData, null, 4);
let finalJs = "var dataQuizData = " + finalJson + ";\n";

fs.writeFileSync('data_quiz_data_utf8.js', finalJs, 'utf8');
fs.writeFileSync('data_quiz_data.js', Buffer.from(finalJs, 'utf16le'));

console.log("Successfully rebuilt Q23-Q33!");
