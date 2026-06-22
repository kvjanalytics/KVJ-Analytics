import codecs
import re

path = r"C:\Users\kj anand\Downloads\Quiz DD\quiz_data.js"
with codecs.open(path, 'r', 'utf-8') as f:
    text = f.read()

matches = re.finditer(r'"(\w+)":\s*\[', text)

lines = text.split('\n')
def get_line_num(pos):
    return text.count('\n', 0, pos) + 1

for match in matches:
    key = match.group(1)
    start_idx = match.end()
    line_num = get_line_num(match.start())
    
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
    
    print(f"Line {line_num}: Key {key}, Question Count: {count}")
