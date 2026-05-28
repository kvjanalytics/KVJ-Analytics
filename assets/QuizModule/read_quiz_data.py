import re

path = r'Quiz DD/quiz_data.js'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Try to find da_mock3
match = re.search(r'["\']da_mock3["\']\s*:\s*\[(.*?)(?=\s*\]\s*[,}])', content, re.DOTALL)
if match:
    section_content = match.group(1)
    print("Found da_mock3 in quiz_data.js. First 500 chars:")
    print(section_content[:500])
else:
    print("da_mock3 NOT found in quiz_data.js.")
