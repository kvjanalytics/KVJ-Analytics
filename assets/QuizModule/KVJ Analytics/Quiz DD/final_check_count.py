import re

path = r'Quiz DD/data_quiz_data_utf8.js'
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
