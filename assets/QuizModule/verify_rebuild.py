import re

BASE = r"C:\Users\kj anand\Downloads\Quiz DD (13) 6\Quiz DD"

# Verify utf-16 file
with open(BASE + r"\data_quiz_data.js", 'rb') as f:
    content = f.read().decode('utf-16')

start = content.find('"da_mock3":')
section = content[start:]
ids = re.findall(r'"id":\s*(\d+)', section)
# Stop at the next top-level key
end_marker = section.find('",', section.find(']'))
ids_int = [int(x) for x in ids if int(x) <= 44]

print(f"data_quiz_data.js - da_mock3 question count: {len(ids_int)}")
print(f"IDs: {ids_int}")

# Check Q1
q1_match = re.search(r'"id":\s*1,.*?"q":\s*"(.*?)"', section, re.DOTALL)
if q1_match:
    print(f"\nQ1 preview: {q1_match.group(1)[:80]}")

# Verify utf-8 file
with open(BASE + r"\data_quiz_data_utf8.js", 'r', encoding='utf-8') as f:
    content2 = f.read()

start2 = content2.find('"da_mock3":')
section2 = content2[start2:]
ids2 = re.findall(r'"id":\s*(\d+)', section2)
ids2_int = [int(x) for x in ids2 if int(x) <= 44]
print(f"\ndata_quiz_data_utf8.js - da_mock3 question count: {len(ids2_int)}")
print(f"IDs: {ids2_int}")
