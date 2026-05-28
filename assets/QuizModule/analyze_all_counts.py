import os
import re

path = r'C:/Users/kj anand/Downloads/Quiz DD (13) 6/Quiz DD/data_quiz_data_utf8.js'

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract the da_mock3 block
# Find "da_mock3": [
start_match = re.search(r'\"da_mock3\"\s*:\s*\[', content)
if start_match:
    start_pos = start_match.end()
    # Find the closing ] for this block
    # Simple brackets counting
    depth = 1
    end_pos = start_pos
    i = start_pos
    while i < len(content) and depth > 0:
        if content[i] == '[':
            depth += 1
        elif content[i] == ']':
            depth -= 1
        i += 1
    end_pos = i
    
    da_mock3_sub = content[start_pos:end_pos]
    ids = re.findall(r'\"id\"\s*:\s*(\d+)', da_mock3_sub)
    print(f'da_mock3 contains {len(ids)} questions. Max ID: {max(map(int, ids)) if ids else "N/A"}')
    print(f'Unique IDs: {sorted(list(set(map(int, ids))))}')
else:
    print('da_mock3 not found')

# Also check for other keys with many questions
matches = re.finditer(r'[\"\']?([a-zA-Z0-9_]+)[\"\']?\s*:\s*\[', content)
for m in matches:
    key = m.group(1)
    if key in ["options", "a", "labels", "rows", "cols", "optionImages"]: continue
    
    p = m.end()
    d = 1
    j = p
    while j < len(content) and d > 0:
        if content[j] == '[': d += 1
        elif content[j] == ']': d -= 1
        j += 1
    sub = content[p:j]
    q_count = len(re.findall(r'\"id\"\s*:\s*\d+', sub))
    if q_count > 30:
        print(f'Assessment {key} has {q_count} questions')
