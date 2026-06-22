import re

filepath = r"c:\Users\kj anand\Downloads\Quiz DD (2) 7 (2)\Quiz DD (2) 6\Quiz DD (13) 6\Quiz DD\quiz_data.js"
with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

def get_array_content(content, key):
    pattern = rf'"{key}":\s*\['
    match = re.search(pattern, content)
    if not match: return None, None
    start = match.start()
    array_start = match.end() - 1
    bracket_count = 0
    in_string = False
    for i in range(array_start, len(content)):
        if content[i] == '"': in_string = not in_string
        if not in_string:
            if content[i] == '[': bracket_count += 1
            elif content[i] == ']':
                bracket_count -= 1
                if bracket_count == 0:
                    return content[start:i+1], (start, i+1)
    return None, None

m1_str, m1_range = get_array_content(content, "da_mock1")
m2_str, m2_range = get_array_content(content, "da_mock2")

def get_objs(s):
    objs = []
    start = -1
    bc = 0
    in_s = False
    for i in range(len(s)):
        if s[i] == '"': in_s = not in_s
        if not in_s:
            if s[i] == '{':
                if bc == 0: start = i
                bc += 1
            elif s[i] == '}':
                bc -= 1
                if bc == 0: objs.append(s[start:i+1])
    return objs

objs1 = get_objs(m1_str)
objs2 = get_objs(m2_str)

print(f"Quiz Data Mock1 count: {len(objs1)}")
print(f"Quiz Data Mock2 count: {len(objs2)}")

# Balance to 40
if len(objs1) > 40:
    while len(objs1) > 40:
        o = objs1.pop()
        if len(objs2) < 40:
            objs2.append(o)

def reindex(objs):
    new = []
    for i, o in enumerate(objs):
        new.append(re.sub(r'"id":\s*\d+', f'"id": {i+1}', o))
    return new

objs1 = reindex(objs1)
objs2 = reindex(objs2)

new_m1 = '"da_mock1": [\n        ' + ',\n        '.join(objs1) + '\n    ]'
new_m2 = '"da_mock2": [\n        ' + ',\n        '.join(objs2) + '\n    ]'

if m1_range[0] > m2_range[0]:
    content = content[:m1_range[0]] + new_m1 + content[m1_range[1]:]
    content = content[:m2_range[0]] + new_m2 + content[m2_range[1]:]
else:
    content = content[:m2_range[0]] + new_m2 + content[m2_range[1]:]
    content = content[:m1_range[0]] + new_m1 + content[m1_range[1]:]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated quiz_data.js successfully.")
