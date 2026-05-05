import re

file_path = r'c:\Users\kj anand\Downloads\Quiz DD\data_quiz_data.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern for keys like "data1": [
pattern = re.compile(r'\"([a-zA-Z0-9_]+)\": \[')

matches = pattern.findall(content)
for i, match in enumerate(matches):
    print(f"{i}: {match}")
