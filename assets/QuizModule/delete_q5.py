import sys

file_path = 'c:/Users/kj anand/Downloads/Quiz DD (2) 7 (2)/Quiz DD (2) 6/Quiz DD (13) 6/Quiz DD/data_quiz_data_utf8.js'
with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
    lines = f.readlines()

# Remove lines 1522 to 1532 (0-indexed: 1521 to 1531)
# Checking content to be safe
if '"id": 5,' in lines[1521]:
    new_lines = lines[:1521] + lines[1532:]
    with open(file_path, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print("Successfully removed Question ID 5")
else:
    print(f"Error: Line 1522 does not contain id: 5. Actual content: {lines[1521].strip()}")
