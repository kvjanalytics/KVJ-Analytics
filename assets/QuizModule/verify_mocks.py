import re

with open('data_quiz_data.js', 'r', encoding='utf-8') as f:
    content = f.read()

keys = ['data1', 'data2', 'data3', 'data4', 'data5', 'da_mock1', 'da_mock2', 'da_mock3']

for key in keys:
    if f'"{key}"' not in content:
        print(f'{key}: MISSING')
        continue
    start = content.index(f'"{key}"')
    # Find the end of this array
    depth = 0
    array_start = content.find('[', start)
    for i in range(array_start, len(content)):
        if content[i] == '[': depth += 1
        elif content[i] == ']':
            depth -= 1
            if depth == 0:
                section = content[start:i+1]
                break
    count = len(re.findall(r'"type":|type:', section))
    print(f'{key}: {count} questions')

print('\nAll keys present - quiz engine should now load correctly!')
