import re
import os

def repair_and_fix(file_path):
    if not os.path.exists(file_path):
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    # Pattern to find broken q: lines or correct ones
    # Case 1: q: Question... (1 Mark)", (Broken - missing opening quote)
    # Case 2: "q": "(1 Mark) Question..." (Needs fix)
    # Case 3: q: "(1 Mark) Question..." (Needs fix)
    
    # We'll use a regex that matches the key and the content
    for line in lines:
        # Match broken line: q: Text (X Mark)",
        broken_match = re.search(r'(\s*q?:\s*)([^"].*? \(\d+ Marks?\)",?\n)', line)
        if broken_match:
            key_part = broken_match.group(1)
            content_part = broken_match.group(2)
            # Add the quote back
            new_lines.append(f'{key_part}"{content_part}')
            continue
            
        # Match "q": "(X Mark) Text",
        fix_match = re.search(r'(\s*"?q"?:\s*")\((\d+ Marks?)\)\s*(.*?)(",?\n)', line)
        if fix_match:
            key_part = fix_match.group(1)
            mark_text = fix_match.group(2)
            question_content = fix_match.group(3)
            suffix = fix_match.group(4)
            # Move mark to end if not already there
            if f"({mark_text})" not in question_content:
                new_lines.append(f'{key_part}{question_content} ({mark_text}){suffix}')
            else:
                new_lines.append(line)
            continue
            
        new_lines.append(line)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)

repair_and_fix(r"c:\Users\kj anand\Downloads\Quiz DD\data_quiz_data.js")
repair_and_fix(r"c:\Users\kj anand\Downloads\Quiz DD\quiz_data.js")
print("Repair and fix complete.")
