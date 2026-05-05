import re

file_path = r'c:\Users\kj anand\Downloads\Quiz DD\quiz_data.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find "da_mock3": [
match = re.search(r'\"da_mock3\": \[(.*?)^\s+\],', content, re.DOTALL | re.MULTILINE)

if match:
    with open(r'c:\Users\kj anand\Downloads\Quiz DD\scratch\da_mock3_fixed.txt', 'w', encoding='utf-8') as f:
        f.write(match.group(1))
    print("Extracted 28 questions of da_mock3.")
else:
    print("Could not find da_mock3.")
