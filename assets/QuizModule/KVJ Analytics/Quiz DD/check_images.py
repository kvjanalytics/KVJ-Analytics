import re, json, os

BASE = r"C:\Users\kj anand\Downloads\Quiz DD (13) 6\Quiz DD"

with open(BASE + r"\data_quiz_data_utf8.js", 'r', encoding='utf-8') as f:
    content = f.read()

start = content.find('"da_mock3":')
arr_start = content.find('[', start)

depth = 0
i = arr_start
while i < len(content):
    ch = content[i]
    if ch == '[': depth += 1
    elif ch == ']':
        depth -= 1
        if depth == 0:
            arr_end = i
            break
    i += 1

da_mock3 = json.loads(content[arr_start:arr_end+1])

# Collect all referenced images
referenced = []
for q in da_mock3:
    if 'img' in q:
        referenced.append((q['id'], 'img', q['img']))
    if 'optionImages' in q:
        for img in q['optionImages']:
            referenced.append((q['id'], 'optionImage', img))

print("All referenced images in da_mock3:")
for qid, kind, fname in referenced:
    exists = os.path.isfile(os.path.join(BASE, fname))
    status = "OK" if exists else "MISSING"
    print(f"  Q{qid} [{kind}]: {fname} -> {status}")
