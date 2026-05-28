import os
import re

path = r'C:/Users/kj anand/Downloads/Quiz DD (13) 6/Quiz DD/data_quiz_data_utf8.js'

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Look for patterns like "key": [ or key: [ at the start of a line or after a comma
matches = re.finditer(r'[\"\']?([a-zA-Z0-9_]+)[\"\']?\s*:\s*\[', content)

results = []
for m in matches:
    key = m.group(1)
    pos = m.start()
    # Find line number
    line_no = content.count('\n', 0, pos) + 1
    results.append((key, line_no, pos))

for i in range(len(results)):
    key, line, pos = results[i]
    # find end of this block (start of next block)
    if i < len(results) - 1:
        end_pos = results[i+1][2]
    else:
        end_pos = len(content)
    
    sub = content[pos:end_pos]
    q_count = sub.count('"id":') + sub.count("'id':") + sub.count("id:")
    print(f'Key: {key}, Line: {line}, Questions: {q_count}')
