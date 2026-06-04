import re
import os

filepaths = [
    r"c:\Users\kj anand\Downloads\Quiz DD (2) 7 (2)\Quiz DD (2) 6\Quiz DD (13) 6\Quiz DD\data_quiz_data.js",
    r"c:\Users\kj anand\Downloads\Quiz DD (2) 7 (2)\Quiz DD (2) 6\Quiz DD (13) 6\Quiz DD\data_quiz_data (2).js",
    r"c:\Users\kj anand\Downloads\Quiz DD (2) 7 (2)\Quiz DD (2) 6\Quiz DD (13) 6\Quiz DD\quiz_data.js",
    r"c:\Users\kj anand\Downloads\Quiz DD (2) 7 (2)\Quiz DD (2) 6\Quiz DD (13) 6\Quiz DD\data_quiz_data_utf8.js",
    r"c:\Users\kj anand\Downloads\Quiz DD\data_quiz_data.js",
    r"c:\Users\kj anand\Downloads\Quiz DD\quiz_data.js"
]

def find_mock(content, key):
    # Regex to find the key followed by optional spaces/quotes and then : [
    patterns = [
        rf'"{key}"\s*:\s*\[',
        rf"'{key}'\s*:\s*\[",
        rf'\b{key}\b\s*:\s*\['
    ]
    match = None
    for pattern in patterns:
        match = re.search(pattern, content)
        if match: break
        
    if not match: return None, None
        
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

def reindex(objs):
    new = []
    for i, o in enumerate(objs):
        o_re = re.sub(r'("?id"?)\s*:\s*\d+', rf'\1: {i+1}', o)
        new.append(o_re)
    return new

for filepath in filepaths:
    if not os.path.exists(filepath): continue
    print(f"File: {filepath}")
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()

    m1_str, m1_range = find_mock(content, "da_mock1")
    m2_str, m2_range = find_mock(content, "da_mock2")

    if not m1_str or not m2_str:
        print(f"  FAILED to find mocks in {filepath}")
        continue

    objs1 = get_objs(m1_str)
    objs2 = get_objs(m2_str)

    print(f"  Initial: Mock1={len(objs1)}, Mock2={len(objs2)}")

    # Standardize to 40
    # Move from 1 to 2 if 1 is long and 2 is short
    while len(objs1) > 40:
        obj = objs1.pop()
        if len(objs2) < 40:
            objs2.append(obj)
            
    # If Mock1 is still short, pad it (shouldn't happen with user data usually, but anyway)
    while len(objs1) < 40 and len(objs1) > 0:
        objs1.append(objs1[-1])
        
    # If Mock2 is long, trim it
    while len(objs2) > 40:
        objs2.pop()
        
    # If Mock2 is short, pad it
    while len(objs2) < 40 and len(objs2) > 0:
        objs2.append(objs2[-1])

    objs1 = reindex(objs1)
    objs2 = reindex(objs2)

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
    print(f"  SUCCESS: Standardized to 40/40.")

print("\nAll files processed successfully.")
