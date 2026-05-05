import re

file_path = r'c:\Users\kj anand\Downloads\Quiz DD\data_quiz_data.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find all keys
key_pattern = re.compile(r'\"([a-zA-Z0-9_]+)\": \[', re.MULTILINE)
matches = list(key_pattern.finditer(content))

for i in range(len(matches)):
    key = matches[i].group(1)
    start = matches[i].start()
    if i + 1 < len(matches):
        end = matches[i+1].start()
    else:
        end = content.rfind(']') + 1
    
    segment = content[start:end]
    # Count occurrences of "id":
    count = len(re.findall(r'\"id\":\s+\d+|id:\s+\d+', segment))
    print(f"{key}: {count} questions")
