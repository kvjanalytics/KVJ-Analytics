import codecs
import re

path = r"C:\Users\kj anand\Downloads\Quiz DD\quiz_data.js"
with codecs.open(path, 'r', 'utf-8') as f:
    text = f.read()

# Simple regex to find "key": [ ... ]
# This is tricky because of nested brackets, but we can do a basic count of objects inside brackets
matches = re.finditer(r'"(\w+)":\s*\[', text)

for match in matches:
    key = match.group(1)
    start_idx = match.end()
    
    # Count objects { ... } at the top level of this array
    count = 0
    bracket_level = 1
    i = start_idx
    while i < len(text) and bracket_level > 0:
        if text[i] == '[':
            bracket_level += 1
        elif text[i] == ']':
            bracket_level -= 1
        elif text[i] == '{' and bracket_level == 1:
            count += 1
        i += 1
    
    print(f"Key: {key}, Question Count: {count}")
