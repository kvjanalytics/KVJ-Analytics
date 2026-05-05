import re

file_path = r'c:\Users\kj anand\Downloads\Quiz DD\data_quiz_data.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find all top-level keys like "data1": [ ... ]
# We use a non-greedy match for the content, but we need to handle nested brackets.
# This is tricky in regex.
# Instead, let's find the START of each key.

key_pattern = re.compile(r'^\s*\"([a-zA-Z0-9_]+)\": \[', re.MULTILINE)
matches = list(key_pattern.finditer(content))

if not matches:
    print("No keys found!")
    exit()

# Extract segments
segments = {}
for i in range(len(matches)):
    key = matches[i].group(1)
    start = matches[i].start()
    if i + 1 < len(matches):
        end = matches[i+1].start()
    else:
        # Find the last closing ];
        end = content.rfind(']') + 1
        if end == 0: end = len(content)
    
    # The content of the array
    # We want to strip the key part and the trailing comma
    segment_content = content[matches[i].end():end].strip()
    if segment_content.endswith(','):
        segment_content = segment_content[:-1].strip()
    
    if key not in segments:
        segments[key] = []
    segments[key].append(segment_content)

# Now we have segments grouped by key.
# For data1, we merge them.
# For others, we take the FIRST one (as they were probably duplicated by the messy script).

new_body = ""
for key, contents in segments.items():
    if key == "data1":
        # Merge all contents
        # We need to be careful about renumbering
        all_items = []
        for c in contents:
            # Each c is a string of objects like { ... }, { ... }
            # Split by }, {
            # This is also tricky.
            all_items.append(c)
        
        merged_c = ",\n".join(all_items)
        new_body += f'    "{key}": [\n{merged_c}\n    ],\n'
    else:
        # Take the FIRST one
        new_body += f'    "{key}": [\n{contents[0]}\n    ],\n'

# Reconstruct the file
final_output = "var dataQuizData = {\n" + new_body.rstrip(',\n') + "\n};"

with open(file_path, 'w', encoding='utf-8') as f:
    f.write(final_output)

print("Cleaned up and merged data_quiz_data.js.")
