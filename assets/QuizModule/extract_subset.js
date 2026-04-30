const fs = require('fs');

// Read the file content
const content = fs.readFileSync('quiz_data.js', 'utf-8');

// Use an eval-like approach to safely parse the window.quizData
// We'll wrap it in a function
const script = content.replace('window.quizData =', 'return');
const extractData = new Function(script);

try {
    const quizData = extractData();
    const mock3_q21_40 = quizData.mock3.slice(20, 40); // 0-indexed, so 20 is 21st, 40 is up to 40th
    fs.writeFileSync('mock3_subset.json', JSON.stringify(mock3_q21_40, null, 2));
    console.log("Successfully extracted " + mock3_q21_40.length + " questions.");
} catch (e) {
    console.error("Error parsing JS:", e);
}
