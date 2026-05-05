import re
import os

def fix_marks(file_path):
    if not os.path.exists(file_path):
        print(f"File {file_path} not found.")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to find "(X Mark) Question content"
    # Group 1: The whole mark string e.g. "1 Mark" or "3 Marks"
    # Group 2: The rest of the question
    # We look for "q": "(X Mark) ... "
    pattern = re.compile(r'("q":\s*")\((\d+ Marks?)\)\s*(.*?)(",?\n)', re.DOTALL)
    
    def replacement(match):
        mark_text = match.group(2)
        question_content = match.group(3)
        suffix = match.group(4)
        # Ensure we don't duplicate marks if they are already at the end
        if f"({mark_text})" in question_content:
            return match.group(0)
        return f'"q": "{question_content} ({mark_text}){suffix}'

    new_content = pattern.sub(replacement, content)

    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed marks in {file_path}")
    else:
        print(f"No marks to fix in {file_path}")

# Run for both files
fix_marks(r"c:\Users\kj anand\Downloads\Quiz DD\data_quiz_data.js")
fix_marks(r"c:\Users\kj anand\Downloads\Quiz DD\quiz_data.js")
