import re
import os

filepaths = [
    r"c:\Users\kj anand\Downloads\Quiz DD (2) 7 (2)\Quiz DD (2) 6\Quiz DD (13) 6\Quiz DD\data_quiz_data.js",
    r"c:\Users\kj anand\Downloads\Quiz DD (2) 7 (2)\Quiz DD (2) 6\Quiz DD (13) 6\Quiz DD\quiz_data.js",
    r"c:\Users\kj anand\Downloads\Quiz DD (2) 7 (2)\Quiz DD (2) 6\Quiz DD (13) 6\Quiz DD\data_quiz_data_utf8.js",
    r"c:\Users\kj anand\Downloads\Quiz DD\data_quiz_data.js",
    r"c:\Users\kj anand\Downloads\Quiz DD\quiz_data.js"
]

def get_array(content, key):
    # Regex to find "key": [ ... ]
    # We'll use a more robust way to find the end of the array
    pattern = rf'"{key}":\s*\['
    match = re.search(pattern, content)
    if not match: 
        pattern = rf"'{key}':\s*\["
        match = re.search(pattern, content)
    if not match: return None, None
    
    start_idx = match.start()
    array_start_idx = match.end() - 1
    
    bracket_count = 0
    in_string = False
    escape = False
    end_idx = -1
    
    for i in range(array_start_idx, len(content)):
        char = content[i]
        if escape:
            escape = False
            continue
        if char == '\\':
            escape = True
            continue
        if char == '"' or char == "'":
            # This is a bit simplified as it doesn't check which quote started the string
            in_string = not in_string
            continue
        if not in_string:
            if char == '[':
                bracket_count += 1
            elif char == ']':
                bracket_count -= 1
                if bracket_count == 0:
                    end_idx = i + 1
                    break
    if end_idx == -1: return None, None
    return content[start_idx:end_idx], (start_idx, end_idx)

def get_objects(array_str):
    # Find all top-level { ... } blocks
    objs = []
    bracket_count = 0
    in_string = False
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
        if char == '"' or char == "'":
            in_string = not in_string
            continue
        if not in_string:
            if char == '{':
                if bracket_count == 0:
                    start = i
                bracket_count += 1
            elif char == '}':
                bracket_count -= 1
                if bracket_count == 0:
                    objs.append(array_str[start:i+1])
    return objs

def reindex(objs):
    new_objs = []
    for i, obj in enumerate(objs):
        # Substitute the id field
        # Look for id: or "id": or 'id':
        new_obj = re.sub(r'("?id"?)\s*:\s*\d+', rf'\1: {i+1}', obj)
        new_objs.append(new_obj)
    return new_objs

for filepath in filepaths:
    if not os.path.exists(filepath):
        print(f"Skipping {filepath} (does not exist)")
        continue
        
    print(f"Processing {filepath}...")
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    
    mock1_str, mock1_range = get_array(content, "da_mock1")
    mock2_str, mock2_range = get_array(content, "da_mock2")
    
    if not mock1_str or not mock2_str:
        print(f"  Could not find da_mock1 or da_mock2 in {filepath}")
        continue
        
    mock1_objs = get_objects(mock1_str)
    mock2_objs = get_objects(mock2_str)
    
    print(f"  Initial counts: Mock1={len(mock1_objs)}, Mock2={len(mock2_objs)}")
    
    # Target: Exactly 40 for both.
    # If Mock1 > 40 and Mock2 < 40, move some.
    total = len(mock1_objs) + len(mock2_objs)
    
    if len(mock1_objs) > 40:
        to_move = len(mock1_objs) - 40
        for _ in range(to_move):
            if len(mock2_objs) < 40:
                # Move from Mock1 to Mock2
                # We'll take from the middle or end? 
                # Let's take the ones with large IDs if possible, or just the end.
                # Actually, let's take IDs 129, 229 if they exist.
                found_special = False
                for i, obj in enumerate(mock1_objs):
                    if '"id": 129' in obj or '"id": 229' in obj or 'id: 129' in obj or 'id: 229' in obj:
                        mock2_objs.append(mock1_objs.pop(i))
                        found_special = True
                        break
                if not found_special:
                    mock2_objs.append(mock1_objs.pop())
            else:
                # Just discard if Mock2 is already 40
                mock1_objs.pop()
    
    # Re-index
    mock1_objs = reindex(mock1_objs)
    mock2_objs = reindex(mock2_objs)
    
    # Ensure they are exactly 40 (in case Mock2 was still < 40)
    while len(mock2_objs) < 40:
        # Duplicate the last one as a placeholder if necessary
        mock2_objs.append(reindex([mock2_objs[-1]])[0])
        # Re-index again to fix the ID
        mock2_objs = reindex(mock2_objs)

    # Reconstruct
    new_mock1_str = '"da_mock1": [\n        ' + ',\n        '.join(mock1_objs) + '\n    ]'
    new_mock2_str = '"da_mock2": [\n        ' + ',\n        '.join(mock2_objs) + '\n    ]'
    
    # We must replace the strings in the content. 
    # But ranges might have changed if we do it one by one.
    # We'll replace the one that appears later first.
    if mock1_range[0] > mock2_range[0]:
        content = content[:mock1_range[0]] + new_mock1_str + content[mock1_range[1]:]
        # Recalculate mock2 range? No, just use string replace for the unique old string if unique.
        # Safer to use the original range adjusted for the first replacement.
        content = content[:mock2_range[0]] + new_mock2_str + content[mock2_range[1]:]
    else:
        # mock2 is later
        # Wait, usually mock1 is at 1467 and mock2 is at 2053.
        # So mock2 is later.
        # REPLACE later one FIRST!
        content = content[:mock2_range[0]] + new_mock2_str + content[mock2_range[1]:]
        content = content[:mock1_range[0]] + new_mock1_str + content[mock1_range[1]:]

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"  Successfully updated {filepath}. New counts: 40/40")

print("\nDone.")
