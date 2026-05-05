import re
import sys

file_path = sys.argv[1]

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Match top-level keys
pattern = re.compile(r'^\s*\"([a-zA-Z0-9_]+)\": \[', re.MULTILINE)
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
