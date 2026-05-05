import os

file_path = r'c:\Users\kj anand\Downloads\Quiz DD\data_quiz_data.js'
mock3_path = r'c:\Users\kj anand\Downloads\Quiz DD\scratch\da_mock3_exact.txt'

with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# find where da_mock2 ends and da_mock3 starts
# Line 1593 is }, 1594 is ]
# We want to replace everything from 1595 onwards.

with open(mock3_path, 'r', encoding='utf-8') as f:
    mock3_content = f.read()

# Lines are 0-indexed in list
# lines[1593] is line 1594
new_lines = lines[:1594]
new_lines.append('    ],\n')
new_lines.append('    "da_mock3": [\n')
new_lines.append(mock3_content)
new_lines.append('\n};')

with open(file_path, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print("Restored da_mock3 in data_quiz_data.js.")
