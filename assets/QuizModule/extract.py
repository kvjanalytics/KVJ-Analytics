import json
import re

with open('quiz_data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Using a simpler approach: extract everything from '"mock3": [' to the end, then parse manually or using regex
start_idx = content.find('"mock3": [')
if start_idx != -1:
    # Extract just the mock3 block
    # We know it ends with '],' followed by '"da_mock1"' or something
    end_idx = content.find('],', start_idx)
    while end_idx != -1:
        block = content[start_idx:end_idx+1]
        # try to parse as list by adding {
        try:
            # this might not work if it contains unquoted keys or trailing commas or js functions
            pass
        except Exception:
            pass
        end_idx = content.find('],', end_idx + 1)
        
    # Let's just find all questions by searching for 'id: ' or '"id": ' inside mock3
    mock3_part = content[start_idx:content.find('"da_mock1"', start_idx)]
    questions = re.split(r'\},\s*\{', mock3_part)
    print(f"Total questions found in mock3 split: {len(questions)}")
    if len(questions) >= 29:
        print("--- 29th question (index 28) ---")
        print("{" + questions[28] + "}")
    if len(questions) >= 30:
        print("--- 30th question (index 29) ---")
        print("{" + questions[29] + "}")
