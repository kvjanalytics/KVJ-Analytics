import re

with open('quiz_data.js', 'r', encoding='utf-8') as f:
    content = f.read()

keys = ['mock1', 'mock2', 'mock3']

for key in keys:
    if f'"{key}"' not in content:
        print(f'{key}: MISSING')
        continue
    start = content.index(f'"{key}"')
    # Find where next key starts
    next_key_pos = None
    all_keys = ['mock1', 'mock2', 'mock3', 'da_mock1']
    for k in all_keys:
        if k == key:
            continue
        idx = content.find(f'"{k}"', start + 1)
        if idx > start and (next_key_pos is None or idx < next_key_pos):
            next_key_pos = idx
    section = content[start:next_key_pos] if next_key_pos else content[start:]
    count = len(re.findall(r'"type":|type:', section))
    print(f'{key}: {count} questions')
