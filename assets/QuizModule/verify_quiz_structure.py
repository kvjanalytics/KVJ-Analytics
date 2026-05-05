import re

path = r"c:\Users\kj anand\Downloads\Quiz DD\data_quiz_data.js"
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

keys = re.findall(r'"(data\w+|da_mock\d+)":\s*\[', content)
print("Keys found:", keys)
print()

for i, key in enumerate(keys):
    start_marker = '"' + key + '":'
    pos = content.find(start_marker)
    if i + 1 < len(keys):
        next_key = '"' + keys[i+1] + '":'
        end_pos = content.find(next_key, pos)
        if end_pos == -1:
            end_pos = len(content)
    else:
        end_pos = len(content)
    block = content[pos:end_pos]
    count = len(re.findall(r'["\s]id["\s]*:\s*\d+', block))
    print("  " + key + ": " + str(count) + " questions")
