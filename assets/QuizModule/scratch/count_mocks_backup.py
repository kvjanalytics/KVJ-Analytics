import re

file_path = r'c:\Users\kj anand\Downloads\Quiz DD\quiz_data.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern for keys like "da_mock1": [
pattern = re.compile(r'\"(da_mock[0-9])\": \[', re.MULTILINE)
matches = list(pattern.finditer(content))

for i in range(len(matches)):
    key = matches[i].group(1)
    start = matches[i].start()
    if i + 1 < len(matches):
        end = matches[i+1].start()
    else:
        end = content.rfind(']') + 1
    
    segment = content[start:end]
    count = len(re.findall(r'\"id\":\s+\d+|id:\s+\d+', segment))
    print(f"{key}: {count} questions")
