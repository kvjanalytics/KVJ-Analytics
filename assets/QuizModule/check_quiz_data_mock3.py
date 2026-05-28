import re

path = r'Quiz DD/quiz_data.js'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

start = content.find('"da_mock3":')
if start == -1:
    print("da_mock3 not found")
else:
    section = content[start:]
    ids = re.findall(r'"id":\s*(\d+)', section)
    print(f"Count: {len(ids)}")
    print(f"IDs: {ids}")
    
    # Check if 21-33 are there
    if '21' in ids and '33' in ids and '44' in ids:
        print("Required IDs found.")
    else:
        print("Missing some IDs.")
        
    # Check ID 1 content
    match = re.search(r'"id":\s*1,.*?"q":\s*"(.*?)"', section, re.DOTALL)
    if match:
        print(f"ID 1 Question: {match.group(1)}")
