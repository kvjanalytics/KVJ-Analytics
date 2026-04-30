import re
import json

with open("c:/Users/kj anand/Downloads/Quiz DD/quiz_data.js", "r", encoding="utf-8") as f:
    text = f.read()

def get_array_block(key, text):
    start_match = re.search(r'"' + key + r'"\s*:\s*\[', text)
    if not start_match: return None, -1, -1
    start_idx = start_match.end() - 1
    bracket_count = 0
    in_string = False
    escape = False
    for i in range(start_idx, len(text)):
        char = text[i]
        if escape:
            escape = False
            continue
        if char == '\\':
            escape = True
            continue
        if char == '"' and not in_string:
            in_string = True
            continue
        elif char == '"' and in_string:
            in_string = False
            continue
        if not in_string:
            if char == '[':
                bracket_count += 1
            elif char == ']':
                bracket_count -= 1
                if bracket_count == 0:
                    return text[start_idx:i+1], start_idx, i+1
    return None, -1, -1

# 1. Extract mock3 array and parse it
mock3_text, _, _ = get_array_block("mock3", text)
mock3_list = json.loads(mock3_text)

first_20_m3 = mock3_list[:20]
last_20_m3 = mock3_list[-20:]

for i, q in enumerate(first_20_m3):
    q["id"] = i + 1
for i, q in enumerate(last_20_m3):
    q["id"] = i + 1

# 2. Update mock1
mock1_text, m1_start, m1_end = get_array_block("mock1", text)
mock1_inner = mock1_text[1:-1]
mock1_lines = mock1_inner.strip().split('\n')
q_lines = [l for l in mock1_lines if '{' in l]
remaining_m1 = "\n".join(q_lines[20:])

new_m1_first20 = json.dumps(first_20_m3, indent=4)
new_m1_first20_inner = new_m1_first20.strip()[1:-1].strip()

new_mock1_inner = new_m1_first20_inner + ",\n" + remaining_m1
# Fix indentation for new_mock1_text to align perfectly
new_mock1_text = "[\n" + "\n".join("    " + line if line.strip() else line for line in new_mock1_inner.split("\n")) + "\n    ]"

text = text[:m1_start] + new_mock1_text + text[m1_end:]

# 3. Update mock2
mock2_text, m2_start, m2_end = get_array_block("mock2", text)
mock2_list = json.loads(mock2_text)

mock2_list[:20] = last_20_m3
for i, q in enumerate(mock2_list):
    q["id"] = i + 1

new_mock2_text = json.dumps(mock2_list, indent=4)
lines = new_mock2_text.split('\n')
new_mock2_text = lines[0] + '\n' + '\n'.join('    ' + l for l in lines[1:])

text = text[:m2_start] + new_mock2_text + text[m2_end:]

with open("c:/Users/kj anand/Downloads/Quiz DD/quiz_data.js", "w", encoding="utf-8") as f:
    f.write(text)

print("Successfully updated mock1 and mock2!")
