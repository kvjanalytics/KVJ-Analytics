import re
import os

def fix_marks(file_path):
    if not os.path.exists(file_path):
        print(f"File {file_path} not found.")
        return

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to handle both "q": "(1 Mark)" and q: "(1 Mark)"
    # Group 1: The key part (e.g. '"q": ' or 'q: ')
    # Group 2: Quote char (usually ")
    # Group 3: The whole mark string (e.g. "1 Mark")
    # Group 4: The question content
    # Group 5: The closing quote and optional comma/newline
    pattern = re.compile(r'("?q"?:\s*")\((\d+ Marks?)\)\s*(.*?)(",?\n)', re.DOTALL)
    
    def replacement(match):
        key_part = match.group(0).split('"(')[0] if '"(' in match.group(0) else match.group(0).split('(')[0]
        mark_text = match.group(2)
        question_content = match.group(3)
        suffix = match.group(4)
        
        # Avoid duplicate marks
        if f"({mark_text})" in question_content:
            return match.group(0)
            
        return f'{key_part}{question_content} ({mark_text}){suffix}'

    new_content = pattern.sub(replacement, content)

    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed marks in {file_path}")
    else:
        print(f"No more marks to fix in {file_path}")

fix_marks(r"c:\Users\kj anand\Downloads\Quiz DD\data_quiz_data.js")
fix_marks(r"c:\Users\kj anand\Downloads\Quiz DD\quiz_data.js")
