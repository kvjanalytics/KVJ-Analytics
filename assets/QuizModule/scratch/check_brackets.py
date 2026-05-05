import sys

file_path = r'c:\Users\kj anand\Downloads\Quiz DD\data_quiz_data.js'

with open(file_path, 'r', encoding='utf-8') as f:
    text = f.read()

# simple bracket matching
stack = []
lines = text.split('\n')
for i, line in enumerate(lines):
    for j, char in enumerate(line):
        if char in '{[':
            stack.append((char, i+1, j+1))
        elif char in '}]':
            if not stack:
                print(f"Error: Unmatched {char} at line {i+1}, col {j+1}")
                sys.exit(1)
            
            last_char, last_i, last_j = stack.pop()
            if (char == '}' and last_char != '{') or (char == ']' and last_char != '['):
                print(f"Error: Mismatched {char} at line {i+1}, col {j+1}. Expected match for {last_char} at line {last_i}, col {last_j}")
                sys.exit(1)

if stack:
    print(f"Error: Unclosed brackets remaining: {stack}")
else:
    print("All brackets match perfectly!")
