import re

# Verify secondary workspace fix
with open(r'c:\Users\kj anand\Downloads\Quiz DD\data_quiz_data.js', 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

m2_start = content.rfind('"da_mock2"')
m3_start = content.find('"da_mock3"', m2_start)
m2_section = content[m2_start:m3_start]
ids = re.findall(r'["\']?id["\']?\s*:\s*(\d+)', m2_section)
print(f'Secondary workspace - da_mock2 question count: {len(ids)}')
print(f'IDs: {ids}')

# Verify primary workspace
with open(r'c:\Users\kj anand\Downloads\Quiz DD (2) 7 (2)\Quiz DD (2) 6\Quiz DD (13) 6\Quiz DD\data_quiz_data.js', 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

m2_start = content.rfind('"da_mock2"')
m3_start = content.find('"da_mock3"', m2_start)
m2_section = content[m2_start:m3_start]
ids = re.findall(r'["\']?id["\']?\s*:\s*(\d+)', m2_section)
print(f'Primary workspace - da_mock2 question count: {len(ids)}')
print(f'IDs: {ids}')
