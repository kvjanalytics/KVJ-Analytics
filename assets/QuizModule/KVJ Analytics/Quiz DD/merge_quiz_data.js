const fs = require('fs');

try {
    const oldCode = fs.readFileSync('quiz_data_test.js', 'utf-8');
    const newCode = fs.readFileSync('quiz_data.js', 'utf-8');

    // Extract the object part
    const oldObjString = oldCode.replace('var quizData = ', '').replace(/;$/, '');
    const newObjString = newCode.replace('var quizData = ', '').replace(/;$/, '');

    // Evaluate them
    const oldData = eval('(' + oldObjString + ')');
    const newData = eval('(' + newObjString + ')');

    // Merge: Keep all newData (Data Analytics), and add back missing keys from oldData (Python)
    // We also map oldData's 'mock1' to 'py_mock1' if we want to keep both, or we just overwrite.
    // Wait, let's keep all keys.
    Object.keys(oldData).forEach(key => {
        if (!newData[key]) {
            newData[key] = oldData[key];
        } else if (key === 'mock1') {
             // If there's a conflict (e.g., Python mock1 and Data mock1),
             // let's rename the old Python mock1 to 'py_mock1' just in case.
             newData['py_mock1'] = oldData[key];
             console.log("Renamed old mock1 to py_mock1 to avoid conflict.");
        }
    });

    // Write back
    const mergedCode = 'var quizData = ' + JSON.stringify(newData, null, 4) + ';';
    fs.writeFileSync('quiz_data.js', mergedCode, 'utf-8');
    console.log("Successfully merged. Total keys now:", Object.keys(newData).join(', '));
} catch (e) {
    console.error(e);
}
