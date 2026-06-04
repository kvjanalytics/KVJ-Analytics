import json
import re
import os

files = [
    r"c:\Users\kj anand\Downloads\Quiz DD (2) 7 (2)\Quiz DD (2) 6\Quiz DD (13) 6\Quiz DD\data_quiz_data.js",
    r"c:\Users\kj anand\Downloads\Quiz DD (2) 7 (2)\Quiz DD (2) 6\Quiz DD (13) 6\Quiz DD\quiz_data.js",
    r"c:\Users\kj anand\Downloads\Quiz DD (2) 7 (2)\Quiz DD (2) 6\Quiz DD (13) 6\Quiz DD\data_quiz_data_utf8.js",
    r"c:\Users\kj anand\Downloads\Quiz DD\data_quiz_data.js",
    r"c:\Users\kj anand\Downloads\Quiz DD\quiz_data.js"
]

def count_questions(file_path):
    if not os.path.exists(file_path):
        return None
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    results = {}
    for key in ['da_mock1', 'da_mock2', 'da_mock3']:
        # Find the start of the array
        start_pattern = f'"{key}":\\s*\\['
        match = re.search(start_pattern, content)
        if match:
            start_idx = match.end()
            # Count the number of { } blocks at the top level of this array
            # A simple way is to find all { that are not inside another }
            # but we can also just count occurrences of "id":
            count = content.count('"id":', start_idx, content.find('],', start_idx) if content.find('],', start_idx) != -1 else len(content))
            # Some files use id: without quotes
            if count == 0:
                count = content.count('id:', start_idx, content.find('],', start_idx) if content.find('],', start_idx) != -1 else len(content))
            results[key] = count
        else:
            results[key] = "Not found"
    return results

for f in files:
    print(f"File: {f}")
    print(count_questions(f))
    print("-" * 20)
