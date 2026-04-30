import json
import re

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

mock3_text, _, _ = get_array_block("mock3", text)
mock3_list = json.loads(mock3_text)

q21_40 = mock3_list[20:40]

with open("c:/Users/kj anand/Downloads/Quiz DD/mock3_21_40.json", "w", encoding="utf-8") as f:
    json.dump(q21_40, f, indent=4)
    
print("Extracted", len(q21_40), "questions.")
