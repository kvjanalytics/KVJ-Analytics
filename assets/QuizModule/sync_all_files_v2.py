import re
import os

filepaths = [
    r"c:\Users\kj anand\Downloads\Quiz DD (2) 7 (2)\Quiz DD (2) 6\Quiz DD (13) 6\Quiz DD\data_quiz_data.js",
    r"c:\Users\kj anand\Downloads\Quiz DD (2) 7 (2)\Quiz DD (2) 6\Quiz DD (13) 6\Quiz DD\quiz_data.js",
    r"c:\Users\kj anand\Downloads\Quiz DD (2) 7 (2)\Quiz DD (2) 6\Quiz DD (13) 6\Quiz DD\data_quiz_data_utf8.js",
    r"c:\Users\kj anand\Downloads\Quiz DD\data_quiz_data.js",
    r"c:\Users\kj anand\Downloads\Quiz DD\quiz_data.js"
]

def find_array_range(content, key):
    # Search for the key as a property or variable
    # Match: "key": [, 'key': [, key: [, var key = [, etc.
    patterns = [
        rf'"{key}"\s*:\s*\[',
        rf"'{key}'\s*:\s*\[",
        rf'\b{key}\b\s*:\s*\[',
        rf'var\s+{key}\s*=\s*\[',
        rf'let\s+{key}\s*=\s*\[',
        rf'const\s+{key}\s*=\s*\[',
        rf'\.{key}\s*=\s*\['
    ]
    
    match = None
    for p in patterns:
        match = re.search(p, content)
        if match: break
        
    if not match: return None
    
    start_idx = match.start()
    # The array actually starts at the '['
    array_open_idx = content.find('[', match.start())
    
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
                    return (start_idx, i + 1)
    return None

def get_objects(array_str):
    objs = []
    bracket_count = 0
    in_string = False
    quote_char = None
    escape = False
    start = -1
    
    for i in range(len(array_str)):
        char = array_str[i]
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
            if char == '{':
                if bracket_count == 0:
                    start = i
                bracket_count += 1
            elif char == '}':
                bracket_count -= 1
                if bracket_count == 0 and start != -1:
                    objs.append(array_str[start:i+1])
    return objs

def reindex(objs):
    new_objs = []
    for i, obj in enumerate(objs):
        # Substitute the id field
        # Use regex that handles quotes or lack thereof
        new_obj = re.sub(r'(["\'`]?id["\'`]?)\s*:\s*\d+', rf'\1: {i+1}', obj)
        new_objs.append(new_obj)
    return new_objs

for filepath in filepaths:
    if not os.path.exists(filepath):
        continue
        
    print(f"Processing {filepath}...")
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    
    r1 = find_array_range(content, "da_mock1")
    r2 = find_array_range(content, "da_mock2")
    
    if not r1 or not r2:
        print(f"  Missing ranges: r1={r1}, r2={r2}")
        continue
        
    mock1_str = content[r1[0]:r1[1]]
    mock2_str = content[r2[0]:r2[1]]
    
    mock1_objs = get_objects(mock1_str)
    mock2_objs = get_objects(mock2_str)
    
    print(f"  Initial counts: Mock1={len(mock1_objs)}, Mock2={len(mock2_objs)}")
    
    # 1. Normalize Mock1 to 40
    if len(mock1_objs) > 40:
        # Move extras to Mock2 if Mock2 is short
        while len(mock1_objs) > 40:
            obj = mock1_objs.pop() # Take from end
            if len(mock2_objs) < 40:
                mock2_objs.append(obj)
    
    # 2. Re-index
    mock1_objs = reindex(mock1_objs)
    mock2_objs = reindex(mock2_objs)
    
    # 3. Reconstruct strings
    # Try to preserve the original key/prefix
    prefix1 = mock1_str[:mock1_str.find('[')+1]
    prefix2 = mock2_str[:mock2_str.find('[')+1]
    
    new_mock1_str = prefix1 + '\n        ' + ',\n        '.join(mock1_objs) + '\n    ]'
    new_mock2_str = prefix2 + '\n        ' + ',\n        '.join(mock2_objs) + '\n    ]'

    # 4. Apply replacements (later one first)
    if r1[0] > r2[0]:
        content = content[:r1[0]] + new_mock1_str + content[r1[1]:]
        content = content[:r2[0]] + new_mock2_str + content[r2[1]:]
    else:
        content = content[:r2[0]] + new_mock2_str + content[r2[1]:]
        content = content[:r1[0]] + new_mock1_str + content[r1[1]:]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  Final counts: Mock1={len(mock1_objs)}, Mock2={len(mock2_objs)}")

print("\nDone.")
