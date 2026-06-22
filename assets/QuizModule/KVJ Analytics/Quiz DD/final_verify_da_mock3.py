import re
import json

path = r'Quiz DD/data_quiz_data_utf8.js'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract da_mock3
match = re.search(r'["\']da_mock3["\']\s*:\s*\[(.*?)(?=\s*\]\s*[,}])', content, re.DOTALL)
if match:
    section_content = match.group(1)
    ids = re.findall(r'["\']?id["\']?:\s*(\d+)', section_content)
    print(f"Total questions in da_mock3: {len(ids)}")
    print(f"IDs: {ids}")
    
    # Check if 21-33 are there
    if '21' in ids and '33' in ids and '44' in ids:
        print("Required IDs found.")
    else:
        print("Missing some IDs.")
else:
    print("da_mock3 section not found.")
