import json
import os
import re

filepath = r"c:\Users\kj anand\Downloads\Quiz DD (2) 7 (2)\Quiz DD (2) 6\Quiz DD (13) 6\Quiz DD\data_quiz_data.js"

with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

# Parse the JS file roughly
# We find da_mock1 and da_mock2 arrays
def get_array(content, key):
    start_pattern = f'"{key}": ['
    start_idx = content.find(start_pattern)
    if start_idx == -1: return None
    
    # Simple bracket counting to find the end of the array
    end_idx = -1
    bracket_count = 0
    in_string = False
    escape = False
    
    for i in range(start_idx + len(start_pattern) - 1, len(content)):
        char = content[i]
        if escape:
            escape = False
            continue
        if char == '\\':
            escape = True
            continue
        if char == '"':
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
    return content[start_idx:end_idx]

da_mock1_str = get_array(content, "da_mock1")
da_mock2_str = get_array(content, "da_mock2")

# We need to extract the objects. Since it's nearly JSON but not quite (js comments, etc.), 
# we can use a regex to find all { ... } blocks in the array.
def get_objects(array_str):
    # This is tricky because objects can contain nested objects.
    # We'll use id as a marker.
    return re.findall(r'\{[^{}]*(?:\{[^{}]*\}[^{}]*)*\}', array_str, re.DOTALL)

mock1_objs = get_objects(da_mock1_str)
mock2_objs = get_objects(da_mock2_str)

print(f"Initial counts: Mock1={len(mock1_objs)}, Mock2={len(mock2_objs)}")

# Find indices of 129 and 229 in Mock1
idx_129 = -1
idx_229 = -1
for i, obj in enumerate(mock1_objs):
    if '"id": 129' in obj or '"id": 129' in obj:
        idx_129 = i
    if '"id": 229' in obj or '"id": 229' in obj:
        idx_229 = i

if idx_129 != -1 and idx_229 != -1:
    # Remove from mock1
    # Sort indices descending to not affect the other index when removing
    indices = sorted([idx_129, idx_229], reverse=True)
    obj_229 = mock1_objs.pop(indices[0])
    obj_129 = mock1_objs.pop(indices[1])
    
    # Add to mock2
    mock2_objs.append(obj_129)
    mock2_objs.append(obj_229)
    
    print(f"Moved 2 questions. New counts: Mock1={len(mock1_objs)}, Mock2={len(mock2_objs)}")
    
    # Re-index
    def reindex(objs):
        new_objs = []
        for i, obj in enumerate(objs):
            # Replace ID
            new_obj = re.sub(r'"id":\s*\d+', f'"id": {i+1}', obj)
            new_objs.append(new_obj)
        return new_objs

    mock1_objs = reindex(mock1_objs)
    mock2_objs = reindex(mock2_objs)
    
    # Construct new strings
    new_mock1_str = '"da_mock1": [\n        ' + ',\n        '.join(mock1_objs) + '\n    ]'
    new_mock2_str = '"da_mock2": [\n        ' + ',\n        '.join(mock2_objs) + '\n    ]'
    
    new_content = content.replace(da_mock1_str, new_mock1_str)
    new_content = new_content.replace(da_mock2_str, new_mock2_str)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Successfully updated data_quiz_data.js")
else:
    print(f"Could not find IDs 129 and 229. Indices: 129={idx_129}, 229={idx_229}")
