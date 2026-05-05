import re
from collections import Counter

file_path = r'c:\Users\kj anand\Downloads\Quiz DD\data_quiz_data.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Match keys that look like top-level object keys (indented slightly)
pattern = re.compile(r'^\s*\"([a-zA-Z0-9_]+)\": \[', re.MULTILINE)
matches = pattern.findall(content)

counts = Counter(matches)
duplicates = [k for k, v in counts.items() if v > 1]

if duplicates:
    print("Found duplicate keys:")
    for d in duplicates:
        print(f" - {d}")
else:
    print("No duplicate keys found.")
