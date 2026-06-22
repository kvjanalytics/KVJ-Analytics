import re

with open('data_quiz_data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Find data_mod4 section start
mod4_start = content.index('"data_mod4"')

# Find where data_mod4 section ends (next top-level key)
# After "data_mod4": [...] there should be another key or end of object
# Find the next key at the same level
remaining = content[mod4_start:]

# Find the matching closing bracket for data_mod4's array
depth = 0
in_string = False
escape_next = False
array_started = False
array_end = 0

for i, ch in enumerate(remaining):
    if escape_next:
        escape_next = False
        continue
    if ch == '\\' and in_string:
        escape_next = True
        continue
    if ch == '"' and not escape_next:
        in_string = not in_string
        continue
    if in_string:
        continue
    if ch == '[':
        depth += 1
        array_started = True
    elif ch == ']':
        depth -= 1
        if array_started and depth == 0:
            array_end = i + 1
            break

# Extract just the array content of data_mod4
mod4_array = remaining[:array_end]
# This is: "data_mod4": [ ... ]
# We want just the [ ... ] part
bracket_start = mod4_array.index('[')
mod4_questions = mod4_array[bracket_start:array_end]

print(f"Extracted data_mod4 array: {len(mod4_questions)} chars")
print(f"Preview: {mod4_questions[:100]}")

# Count questions
q_count = len(re.findall(r'"type":', mod4_questions))
print(f"Question count: {q_count}")

# Now replace "data4": [] with "data4": [<questions>]
old = '"data4": [\r\n    ]'
if old not in content:
    old = '"data4": [\n    ]'
if old not in content:
    old = '"data4": []'
if old not in content:
    # Try flexible match
    old_match = re.search(r'"data4"\s*:\s*\[\s*\]', content)
    if old_match:
        old = old_match.group(0)
    else:
        print("ERROR: Could not find empty data4 definition!")
        exit(1)

new = f'"data4": {mod4_questions}'
content = content.replace(old, new, 1)

with open('data_quiz_data.js', 'w', encoding='utf-8') as f:
    f.write(content)

print("\ndata4 has been populated with data_mod4 questions!")

# Verify
with open('data_quiz_data.js', 'r', encoding='utf-8') as f:
    verify = f.read()

d4_start = verify.index('"data4"')
d4_next = verify.index('"data_mod4"', d4_start)
d4_section = verify[d4_start:d4_next]
count = len(re.findall(r'"type":', d4_section))
print(f"Verified data4 now has {count} questions.")
