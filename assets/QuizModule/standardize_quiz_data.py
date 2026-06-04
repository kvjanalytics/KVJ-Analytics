import re
import os

filepath = r"c:\Users\kj anand\Downloads\Quiz DD (2) 7 (2)\Quiz DD (2) 6\Quiz DD (13) 6\Quiz DD\quiz_data.js"
with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

def find_mock(content, key):
    # Regex to find the key followed by optional spaces/quotes and then : [
    pattern = rf'"{key}"\s*:\s*\['
    match = re.search(pattern, content)
    if not match:
        pattern = rf"'{key}'\s*:\s*\["
        match = re.search(pattern, content)
    if not match:
        pattern = rf'\b{key}\b\s*:\s*\['
        match = re.search(pattern, content)
        
    if not match:
        print(f"Could not find {key} using regex patterns.")
        # Try a direct find
        idx = content.find(key)
        if idx != -1:
            print(f"Found '{key}' at index {idx}. Context: {repr(content[idx:idx+50])}")
        return None, None
        
    start_idx = match.start()
    array_open_idx = content.find('[', start_idx)
    
    bracket_count = 0
    in_string = False
    quote_char = None
    escape = False
    
    for i in range(array_open_idx, len(content)):
        char = content[i]
        if escape:
            escape = False
            continue
        if char == '\\':
            escape = True
            continue
        if char in ['"', "'", '`']:
            if not in_string:
                in_string = True
                quote_char = char
            elif char == quote_char:
                in_string = False
                quote_char = None
            continue
        if not in_string:
            if char == '[':
                bracket_count += 1
            elif char == ']':
                bracket_count -= 1
                if bracket_count == 0:
                    return content[start_idx:i+1], (start_idx, i+1)
    return None, None

m1_str, m1_range = find_mock(content, "da_mock1")
m2_str, m2_range = find_mock(content, "da_mock2")

if not m1_str or not m2_str:
    print("Failed to extract mock strings.")
    exit(1)

def get_objs(s):
    objs = []
    start = -1
    bc = 0
    in_s = False
    q_c = None
    esc = False
    for i in range(len(s)):
        char = s[i]
        if esc:
            esc = False
            continue
        if char == '\\':
            esc = True
            continue
        if char in ['"', "'", '`']:
            if not in_s:
                in_s = True
                q_c = char
            elif char == q_c:
                in_s = False
                q_c = None
            continue
        if not in_s:
            if char == '{':
                if bc == 0: start = i
                bc += 1
            elif char == '}':
                bc -= 1
                if bc == 0 and start != -1: objs.append(s[start:i+1])
    return objs

objs1 = get_objs(m1_str)
objs2 = get_objs(m2_str)

print(f"Mock1 questions found: {len(objs1)}")
print(f"Mock2 questions found: {len(objs2)}")

# standardized to 40
while len(objs1) > 40:
    obj = objs1.pop()
    if len(objs2) < 40:
        objs2.append(obj)
        
while len(objs2) > 40:
    objs2.pop() # Just discard extra in Mock2

# Ensure Mock2 is padded if still < 40 (duplicate last one)
while len(objs2) < 40 and len(objs2) > 0:
    objs2.append(objs2[-1])

def reindex(objs):
    new = []
    for i, o in enumerate(objs):
        # Handle "id":10, id: 10, 'id':10
        o_re = re.sub(r'("?id"?)\s*:\s*\d+', rf'\1: {i+1}', o)
        new.append(o_re)
    return new

objs1 = reindex(objs1)
objs2 = reindex(objs2)

# Preserve the original key/prefix
prefix1 = m1_str[:m1_str.find('[')+1]
prefix2 = m2_str[:m2_str.find('[')+1]

new_m1 = prefix1 + '\n        ' + ',\n        '.join(objs1) + '\n    ]'
new_m2 = prefix2 + '\n        ' + ',\n        '.join(objs2) + '\n    ]'

if m1_range[0] > m2_range[0]:
    content = content[:m1_range[0]] + new_m1 + content[m1_range[1]:]
    content = content[:m2_range[0]] + new_m2 + content[m2_range[1]:]
else:
    content = content[:m2_range[0]] + new_m2 + content[m2_range[1]:]
    content = content[:m1_range[0]] + new_m1 + content[m1_range[1]:]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Standardized quiz_data.js to 40/40.")
