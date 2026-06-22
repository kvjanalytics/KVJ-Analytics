import json
import re

try:
    with open('quiz_data_test.js', 'r', encoding='utf-8') as f:
        old_data = f.read()
    with open('quiz_data.js', 'r', encoding='utf-8') as f:
        new_data = f.read()

    # We need to extract the parts.
    # The new data starts with: var quizData = {  and ends with }
    # old_data also starts similarly. 
    # Since I just need to prepend the missing keys from old_data:
    
    # Let's extract "1" through "6" from old_data manually.
    match = re.search(r'var quizData = \{([\s\S]*? \t"2":[\s\S]*?) \t"data1": \[', old_data) 
    if match:
        python_chunk = match.group(1)
    else:
        # If "data1" is not directly after, let's just grab everything before "data1"
        match2 = re.search(r'var quizData = \{([\s\S]*?)    "data1": \[', old_data)
        if match2:
            python_chunk = match2.group(1)
            print("Found python chunks before data1")
        else:
            print("Could not find the cutoff in old_data")
            python_chunk = ""

    if python_chunk:
        # We replace "var quizData = {\n" in new_data with "var quizData = {\n" + python_chunk + ",\n"
        # Wait, python_chunk might already have the trailing comma? 
        # Let's clean it up.
        new_data = re.sub(r'var quizData = \{', 'var quizData = {\n' + python_chunk, new_data)
        
        with open('quiz_data.js', 'w', encoding='utf-8') as f:
            f.write(new_data)
        print("Merged python chunk into quiz_data.js")
    
except Exception as e:
    print("Error:", e)
