import re

filepath = r"c:\Users\kj anand\Downloads\Quiz DD (2) 7 (2)\Quiz DD (2) 6\Quiz DD (13) 6\Quiz DD\data_quiz_data.js"
with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

def get_array(content, key):
    pattern = rf'"{key}":\s*\['
    match = re.search(pattern, content)
    if not match: return None
    start = match.start()
    bracket_count = 0
    in_string = False
    for i in range(match.end() - 1, len(content)):
        char = content[i]
        if char == '"': in_string = not in_string
        if not in_string:
            if char == '[': bracket_count += 1
            elif char == ']':
                bracket_count -= 1
                if bracket_count == 0:
                    return content[start:i+1]
    return None

m1 = get_array(content, "da_mock1")
ids = re.findall(r'"id":\s*(\d+)', m1)
print(f"Mock1 total questions: {len(ids)}")
print(f"Mock1 IDs: {ids}")

m2 = get_array(content, "da_mock2")
ids2 = re.findall(r'"id":\s*(\d+)', m2)
print(f"Mock2 total questions: {len(ids2)}")
print(f"Mock2 IDs: {ids2}")
