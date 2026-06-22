import re

with open('data_quiz_data.js', 'r', encoding='utf-8') as f:
    content = f.read()

data3_start = content.index('"data3"')
before = content[:data3_start]
after_data3 = content[data3_start:]

count = len(re.findall(r'marks: [34]', after_data3))
fixed = re.sub(r'marks: [34]', 'marks: 2', after_data3)

with open('data_quiz_data.js', 'w', encoding='utf-8') as f:
    f.write(before + fixed)

print(f'Fixed {count} marks values -> all now set to 2')
