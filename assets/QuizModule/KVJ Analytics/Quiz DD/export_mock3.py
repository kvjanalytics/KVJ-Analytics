import os
import re
import json

path = r'C:/Users/kj anand/Downloads/Quiz DD (13) 6/Quiz DD/data_quiz_data_utf8.js'
output_path = r'C:/Users/kj anand/Downloads/Quiz DD (13) 6/Quiz DD/da_mock3_dump.json'

with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Extract the da_mock3 block
match = re.search(r'\"da_mock3\"\s*:\s*\[', content)
if match:
    start_pos = match.end() - 1 # Include the [
    depth = 0
    i = start_pos
    while i < len(content):
        if content[i] == '[': depth += 1
        elif content[i] == ']': depth -= 1
        if depth == 0:
            break
        i += 1
    
    da_mock3_str = content[start_pos:i+1]
    # Try to clean it up to be valid JSON (it might have trailing commas or keys without quotes)
    # But usually it's close.
    print(f'Length of extracted string: {len(da_mock3_str)}')
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(da_mock3_str)
    print(f'Exported to {output_path}')
else:
    print('da_mock3 not found')
