import re
import os

p = r"c:\Users\kj anand\Downloads\Quiz DD (2) 7 (2)\Quiz DD (2) 6\Quiz DD (13) 6\Quiz DD\data_quiz_data.js"
with open(p, 'r', encoding='utf-8', errors='replace') as f:
    text = f.read()

# I will find the EXACT string indices for the mocks
m1_start_key = text.find('"da_mock1":')
m2_start_key = text.find('"da_mock2":')
m3_start_key = text.find('"da_mock3":')

if m1_start_key == -1 or m2_start_key == -1 or m3_start_key == -1:
    print(f"FAILED: Keys not found. M1:{m1_start_key} M2:{m2_start_key} M3:{m3_start_key}")
    exit(1)

# Find array bounds
m1_arr_start = text.find('[', m1_start_key)
m2_arr_start = text.find('[', m2_start_key)
m3_arr_start = text.find('[', m3_start_key)

def find_end(txt, start_idx):
    bc = 0
    for i in range(start_idx, len(txt)):
        if txt[i] == '[': bc += 1
        elif txt[i] == ']':
            bc -= 1
            if bc == 0: return i + 1
    return -1

m1_arr_end = find_end(text, m1_arr_start)
m2_arr_end = find_end(text, m2_arr_start)

m1_content = text[m1_arr_start:m1_arr_end]
m2_content = text[m2_arr_start:m2_arr_end]

def get_questions(s):
    # Regex for objects
    qs = []
    depth = 0
    start = -1
    for i in range(len(s)):
        if s[i] == '{':
            if depth == 0: start = i
            depth += 1
        elif s[i] == '}':
            depth -= 1
            if depth == 0 and start != -1:
                qs.append(s[start:i+1])
    return qs

q1 = get_questions(m1_content)
q2 = get_questions(m2_content)

print(f"Mock1: {len(q1)}, Mock2: {len(q2)}")

all_q = q1 + q2
new_q1 = all_q[:40]
new_q2 = all_q[40:80]

def fix_ids(objs):
    fixed = []
    for i, o in enumerate(objs):
        o = re.sub(r'("?id"?)\s*:\s*\d+', rf'\1: {i+1}', o)
        fixed.append(o)
    return fixed

new_q1_str = "[\n        " + ",\n        ".join(fix_ids(new_q1)) + "\n    ]"
new_q2_str = "[\n        " + ",\n        ".join(fix_ids(new_q2)) + "\n    ]"

# Reconstruct
if m1_start_key < m2_start_key:
    # M1 before M2
    new_text = text[:m1_arr_start] + new_q1_str + text[m1_arr_end:m2_arr_start] + '"da_mock2": ' + new_q2_str + text[m2_arr_end:]
else:
    # M2 before M1
    new_text = text[:m2_arr_start] + new_q2_str + text[m2_arr_end:m1_arr_start] + '"da_mock1": ' + new_q1_str + text[m1_arr_end:]

with open(p, 'w', encoding='utf-8') as f:
    f.write(new_text)
print("SUCCESSFULLY STANDARDIZED PRIMARY FILE.")
