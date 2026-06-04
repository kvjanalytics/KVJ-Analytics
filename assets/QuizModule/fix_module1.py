import os
import re

# File paths
p_data = r"c:\Users\kj anand\Downloads\Quiz DD (2) 7 (2)\Quiz DD (2) 6\Quiz DD (13) 6\Quiz DD\data_quiz_data.js"
p_quiz = r"c:\Users\kj anand\Downloads\Quiz DD (2) 7 (2)\Quiz DD (2) 6\Quiz DD (13) 6\Quiz DD\quiz_data.js"

# 1. Fix Syntax in data_quiz_data.js
if os.path.exists(p_data):
    with open(p_data, 'r', encoding='utf-8', errors='replace') as f:
        text = f.read()
    
    # Use regex to find the problematic line and fix it
    # Pattern looks for "q": "What data structure describes the following data?<br><strong>[" then any sequence that looks like unescaped lists
    text = re.sub(r'("q":\s*".*?<br><strong>\[)".*?"\s*,\s*".*?"\s*,\s*".*?"(\s*\]</strong>")', r"\1'Aabid', 'Jesenia', 'Mark'\2", text)
    
    with open(p_data, 'w', encoding='utf-8') as f:
        f.write(text)
    print("Fixed data_quiz_data.js syntax.")

# 2. Remove Question 5 from data1 in quiz_data.js
if os.path.exists(p_quiz):
    with open(p_quiz, 'r', encoding='utf-8', errors='replace') as f:
        text = f.read()
    
    # Find the data1 array block
    # We want to remove the block starting at 4459 and ending at 4469 roughly
    # Question 5 is the last one in data1
    # We can match the specific question text and its surrounding braces
    question_pattern = r',\s*{\s*"id": 5,\s*"type": "TF",\s*"q": "For each statement below, select True or False.",\s*"options": \[\s*"Summarizing a large spreadsheet of sales figures into a monthly growth chart is an example of creating knowledge."\s*\],\s*"a": \[\s*false\s*\]\s*}'
    
    new_text = re.sub(question_pattern, "", text)
    
    if new_text != text:
        with open(p_quiz, 'w', encoding='utf-8') as f:
            f.write(new_text)
        print("Removed Question 5 from quiz_data.js.")
    else:
        print("Could not find Question 5 in quiz_data.js using regex.")
