import re
import os

filepath = 'data_quiz_data.js'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

def find_block(text, key):
    match = re.search(f'"{key}"\\s*:\\s*\\[', text)
    if not match: return None, None
    start = match.start()
    array_start = match.end() - 1
    depth = 0
    in_string = False
    escape = False
    for i in range(array_start, len(text)):
        char = text[i]
        if escape:
            escape = False
            continue
        if char == '\\': escape = True
        elif char == '"': in_string = not in_string
        elif not in_string:
            if char == '[': depth += 1
            elif char == ']':
                depth -= 1
                if depth == 0:
                    return start, i + 1
    return None, None

# 1. Extract data4
s, e = find_block(content, 'data4')
if s is not None:
    data4_block = content[s:e]
    print(f"Extracted data4 block ({len(data4_block)} chars)")
else:
    print("data4 not found!")
    # Try to find data_mod4 instead as source
    s, e = find_block(content, 'data_mod4')
    if s is not None:
        data4_block = content[s:e].replace('data_mod4', 'data4', 1)
        print(f"Extracted data_mod4 block and renamed to data4")
    else:
        print("data_mod4 also not found!")
        exit(1)

# 2. Remove all data_mod4 and data4 occurrences to clean up
while True:
    s_mod, e_mod = find_block(content, 'data_mod4')
    if s_mod is not None:
        if e_mod < len(content) and content[e_mod] == ',': e_mod += 1
        content = content[:s_mod] + content[e_mod:]
        continue
    s_d4, e_d4 = find_block(content, 'data4')
    if s_d4 is not None:
        if e_d4 < len(content) and content[e_d4] == ',': e_d4 += 1
        content = content[:s_d4] + content[e_d4:]
        continue
    break

# 3. Insert data4 back at a safe place (before da_mock1 or at end)
insert_pos = content.find('"da_mock1"')
if insert_pos == -1:
    insert_pos = content.rfind('};')
    if insert_pos == -1: insert_pos = content.rfind('}')

prefix = content[:insert_pos].rstrip()
if prefix.endswith(','):
    prefix = prefix[:-1].rstrip()

new_content = prefix + ',\n    ' + data4_block + ',\n' + content[insert_pos:]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("data_quiz_data.js cleaned and data4 restored.")
