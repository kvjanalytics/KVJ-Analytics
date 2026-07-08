import json
import os
import re

files_to_check = ['quiz_data.js', 'data_quiz_data.js', 'data_quiz_data_utf8.js']

for filename in files_to_check:
    filepath = os.path.join(r'd:\OneDrive - KVJ Analytics\Strategist - Intern\KVJ Website\KVJ-Analytics\assets\QuizModule', filename)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # The goal is to find the question "Which visualization type is commonly used to display the distribution..."
    # Then within that JSON object block, replace the "options" array with the correct one
    # and "a": <something> with "a": 2.
    
    # Let's define a function that replaces the options array within a block
    def fix_block(match):
        block = match.group(0)
        # Find the options array
        options_pattern = r'"options"\s*:\s*\[[\s\S]*?\]'
        correct_options = '"options": [\n                "Option A: Column Chart",\n                "Option B: Bar Chart",\n                "Option C: Histogram",\n                "Option D: Line Chart"\n            ]'
        block = re.sub(options_pattern, correct_options, block)
        
        # Fix the answer index
        answer_pattern = r'"a"\s*:\s*\d+'
        correct_answer = '"a": 2'
        block = re.sub(answer_pattern, correct_answer, block)
        return block

    # We match from the "q": "Which visualization... to the "a": \d+
    # But wait, sometimes "a" is before "options", sometimes after.
    # We can match the entire block between { and } that contains the question.
    
    pattern = r'\{[^{}]*"q"\s*:\s*"Which visualization type is commonly used to display the distribution[^}]+\}'
    new_content = re.sub(pattern, fix_block, content)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed {filename}")
    else:
        print(f"No changes in {filename}")
