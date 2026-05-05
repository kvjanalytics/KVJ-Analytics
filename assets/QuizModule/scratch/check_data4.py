import re

file_path = r'c:\Users\kj anand\Downloads\Quiz DD\quiz_data.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'\"data4\": \[(.*?)^\s+\],', content, re.DOTALL | re.MULTILINE)
if match:
    count = len(re.findall(r'\"id\":\s+\d+|id:\s+\d+', match.group(1)))
    print(f"data4 has {count} questions in quiz_data.js")
else:
    print("data4 not found in quiz_data.js")
