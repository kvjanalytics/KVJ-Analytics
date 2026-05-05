import re
import os

def final_fix(file_path):
    if not os.path.exists(file_path):
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Step 1: Repair the mess I made (missing opening quotes and :" ")
    # Replace :" " with "q": "
    content = content.replace(':" "', '"q": "')
    # Replace q: (without quote) followed by question text and (X Mark)"
    # Pattern: \s*q?:\s*([A-Z].*? \(\d+ Marks?\)",?\n)
    # We want to insert the quote back: \s*q: "
    content = re.sub(r'(\s*q:\s*)([A-Z].*? \(\d+ Marks?\)",?\n)', r'\1"\2', content)

    # Step 2: Move marks from beginning to end
    # We target both "q": "(X Mark) ..." and q: "(X Mark) ..."
    # Regex Breakdown:
    # Group 1: key part (\s*"?q"?:\s*")
    # Group 2: mark part (\(\d+ Marks?\))
    # Group 3: space after mark (\s*)
    # Group 4: question content until " or <br> (if it's already at the end)
    # Actually, let's just match the start and move it.
    
    pattern = re.compile(r'(\s*"?q"?:\s*")\((\d+ Marks?)\)\s*(.*?)(",?\n)', re.DOTALL)
    
    def move_mark(match):
        key_part = match.group(1)
        mark_full = match.group(2)
        question_content = match.group(3)
        suffix = match.group(4)
        
        # If the mark is already at the end, don't move it again
        if f"({mark_full})" in question_content:
            return match.group(0)
            
        return f'{key_part}{question_content} ({mark_full}){suffix}'

    new_content = pattern.sub(move_mark, content)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Processed {file_path}")

final_fix(r"c:\Users\kj anand\Downloads\Quiz DD\data_quiz_data.js")
final_fix(r"c:\Users\kj anand\Downloads\Quiz DD\quiz_data.js")
print("Final fix complete.")
