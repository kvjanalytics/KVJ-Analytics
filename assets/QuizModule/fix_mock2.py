import re
import os
import shutil

# Files to fix - remove questions 41 and 42 from da_mock2
files_to_fix = [
    r"c:\Users\kj anand\Downloads\Quiz DD (2) 7 (2)\Quiz DD (2) 6\Quiz DD (13) 6\Quiz DD\data_quiz_data.js",
    r"c:\Users\kj anand\Downloads\Quiz DD\data_quiz_data.js",
]

for filepath in files_to_fix:
    if not os.path.exists(filepath):
        print(f"SKIPPED (not found): {filepath}")
        continue

    # Read file
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    # Backup
    shutil.copy(filepath, filepath + '.bak')

    # Find the da_mock2 section
    mock2_start = content.find('"da_mock2"')
    if mock2_start == -1:
        mock2_start = content.find("'da_mock2'")
    if mock2_start == -1:
        print(f"da_mock2 not found in {filepath}")
        continue

    # Find da_mock3 section (or end of file) to limit scope
    mock3_start = content.find('"da_mock3"', mock2_start)
    if mock3_start == -1:
        mock3_start = len(content)

    mock2_section = content[mock2_start:mock3_start]

    # Find and remove question 41 block
    # Pattern: comma + whitespace + { ... "id": 41 ... }
    # We need to find the block containing id: 41 and id: 42

    # Strategy: find the last two question objects in mock2 that have id 41 and 42
    # and remove them along with the preceding comma

    # Remove id: 41 block
    # Match: ,\n        {\n                "id": 41, ... }\n
    pattern_41 = r',\s*\{[^{}]*?"id"\s*:\s*41\b.*?\}'
    pattern_42 = r',\s*\{[^{}]*?"id"\s*:\s*42\b.*?\}'

    # Use DOTALL so . matches newlines
    new_mock2_section = re.sub(pattern_41, '', mock2_section, flags=re.DOTALL)
    new_mock2_section = re.sub(pattern_42, '', new_mock2_section, flags=re.DOTALL)

    if new_mock2_section == mock2_section:
        # Try without quotes around id
        pattern_41b = r',\s*\{[^{}]*?\bid\s*:\s*41\b.*?\}'
        pattern_42b = r',\s*\{[^{}]*?\bid\s*:\s*42\b.*?\}'
        new_mock2_section = re.sub(pattern_41b, '', mock2_section, flags=re.DOTALL)
        new_mock2_section = re.sub(pattern_42b, '', new_mock2_section, flags=re.DOTALL)

    if new_mock2_section == mock2_section:
        print(f"WARNING: No changes made to {filepath} - pattern not matched")
    else:
        new_content = content[:mock2_start] + new_mock2_section + content[mock3_start:]
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"OK: Removed questions 41 and 42 from {filepath}")

print("Done.")
