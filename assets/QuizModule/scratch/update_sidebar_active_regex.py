import os
import re

files = [
    r"c:\Users\kj anand\Downloads\Quiz DD\Data-Module-1.html",
    r"c:\Users\kj anand\Downloads\Quiz DD\Data-Module-2.html",
    r"c:\Users\kj anand\Downloads\Quiz DD\Data-Module-3.html",
    r"c:\Users\kj anand\Downloads\Quiz DD\Data-Module-4.html",
    r"c:\Users\kj anand\Downloads\Quiz DD\Data-Module-5.html"
]

# Regex to match the .sidebar a.active block regardless of whitespace/newlines
pattern = re.compile(r"\.sidebar a\.active\s*\{[^}]+\}", re.DOTALL)

replacement = """.sidebar a.active {
            color: white; font-weight: 800;
            background: var(--primary-blue); border-radius: 20px;
            box-shadow: 0 4px 12px rgba(30, 58, 95, 0.2);
        }"""

for file_path in files:
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if pattern.search(content):
            new_content = pattern.sub(replacement, content)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {file_path}")
        else:
            print(f"Pattern not found in {file_path}")
    else:
        print(f"File not found: {file_path}")
