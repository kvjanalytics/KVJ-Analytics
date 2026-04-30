const fs = require('fs');

try {
    const filename = 'c:/Users/kj anand/Downloads/Quiz DD/quiz_data.js';
    let content = fs.readFileSync(filename, 'utf8');

    // Parse quizData
    let jsonStr = content.replace(/^var quizData = /, '').trim();
    if (jsonStr.endsWith(';')) jsonStr = jsonStr.slice(0, -1);
    let quizData = new Function('return ' + jsonStr)();

    // Make copies
    let mock3 = JSON.parse(JSON.stringify(quizData.mock3));
    let mock1 = JSON.parse(JSON.stringify(quizData.mock1));
    let mock2 = JSON.parse(JSON.stringify(quizData.mock2));

    console.log(`Original lengths - mock1: ${mock1.length}, mock2: ${mock2.length}, mock3: ${mock3.length}`);

    // 1. "take first 20 questions from mock-3 and replace on mock-1 first 20 questions"
    mock1.splice(0, 20, ...mock3.slice(0, 20));
    // Re-assign IDs for mock1
    mock1.forEach((q, index) => { q.id = index + 1; });

    // 2. "take last 20 from mock-3 and add on mock-2 first 20 questions"
    // mock3.slice(-20) gets the last 20 elements
    mock2.splice(0, 20, ...mock3.slice(-20));
    // Re-assign IDs for mock2
    mock2.forEach((q, index) => { q.id = index + 1; });

    console.log(`New lengths - mock1: ${mock1.length}, mock2: ${mock2.length}`);

    // Stringify with 4 spaces
    let mock1Str = JSON.stringify(mock1, null, 4);
    let mock2Str = JSON.stringify(mock2, null, 4);
    
    // Add 4 spaces of indentation to each line of the stringified array to match the original file format
    mock1Str = mock1Str.split('\n').map((line, i) => i === 0 ? line : '    ' + line).join('\n');
    mock2Str = mock2Str.split('\n').map((line, i) => i === 0 ? line : '    ' + line).join('\n');

    // Replace mock1 in the text
    content = content.replace(/"mock1"\s*:\s*\[[\s\S]*?\],\s*"mock2"\s*:/, `"mock1": ${mock1Str},\n    "mock2":`);

    // Replace mock2 in the text
    content = content.replace(/"mock2"\s*:\s*\[[\s\S]*?\],\s*"mock3"\s*:/, `"mock2": ${mock2Str},\n    "mock3":`);

    fs.writeFileSync(filename, content, 'utf8');
    console.log("Successfully updated mock1 and mock2.");
} catch (e) {
    console.error(e);
}
