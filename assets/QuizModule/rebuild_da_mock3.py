import re, json

BASE = r"C:\Users\kj anand\Downloads\Quiz DD (13) 6\Quiz DD"

# ─── Step 1: Extract Questions 1-29 from quiz_data.js ─────────────────────────
with open(BASE + r"\quiz_data.js", 'r', encoding='utf-8') as f:
    qd_content = f.read()

start_idx = qd_content.find('"da_mock3":')
if start_idx == -1:
    raise ValueError("da_mock3 not found in quiz_data.js")

arr_start = qd_content.find('[', start_idx)

depth = 0
i = arr_start
while i < len(qd_content):
    ch = qd_content[i]
    if ch == '[':
        depth += 1
    elif ch == ']':
        depth -= 1
        if depth == 0:
            arr_end = i
            break
    i += 1

da_mock3_raw = qd_content[arr_start:arr_end+1]
da_mock3_list = json.loads(da_mock3_raw)

q1_29 = [q for q in da_mock3_list if isinstance(q.get('id'), int) and 1 <= q['id'] <= 29]
print(f"Questions 1-29 found: {[q['id'] for q in q1_29]}")

# ─── Step 2: Extract Questions 30-33, 34-44 from current data_quiz_data_utf8.js
with open(BASE + r"\data_quiz_data_utf8.js", 'r', encoding='utf-8') as f:
    dq_content = f.read()

start_idx2 = dq_content.find('"da_mock3":')
arr_start2 = dq_content.find('[', start_idx2)

depth = 0
i = arr_start2
while i < len(dq_content):
    ch = dq_content[i]
    if ch == '[':
        depth += 1
    elif ch == ']':
        depth -= 1
        if depth == 0:
            arr_end2 = i
            break
    i += 1

da_mock3_current = json.loads(dq_content[arr_start2:arr_end2+1])

q30_33 = [q for q in da_mock3_current if isinstance(q.get('id'), int) and 30 <= q['id'] <= 33]
q34_44 = [q for q in da_mock3_current if isinstance(q.get('id'), int) and 34 <= q['id'] <= 44]
print(f"Questions 30-33 found: {[q['id'] for q in q30_33]}")
print(f"Questions 34-44 found: {[q['id'] for q in q34_44]}")

# ─── Step 3: Combine and sort ─────────────────────────────────────────────────
full_da_mock3 = sorted(q1_29 + q30_33 + q34_44, key=lambda x: x['id'])
print(f"\nAll IDs: {[q['id'] for q in full_da_mock3]}")
print(f"Total: {len(full_da_mock3)}")

# ─── Step 4: Serialize ────────────────────────────────────────────────────────
new_array_json = json.dumps(full_da_mock3, indent=4, ensure_ascii=False)

# ─── Step 5: Replace da_mock3 in data_quiz_data.js (utf-16le) ─────────────────
with open(BASE + r"\data_quiz_data.js", 'rb') as f:
    main_content = f.read().decode('utf-16')

start_k = main_content.find('"da_mock3":')
arr_s = main_content.find('[', start_k)

depth = 0
i = arr_s
while i < len(main_content):
    ch = main_content[i]
    if ch == '[':
        depth += 1
    elif ch == ']':
        depth -= 1
        if depth == 0:
            arr_e = i
            break
    i += 1

new_content = main_content[:arr_s] + new_array_json + main_content[arr_e+1:]

with open(BASE + r"\data_quiz_data.js", 'wb') as f:
    f.write(new_content.encode('utf-16'))

with open(BASE + r"\data_quiz_data_utf8.js", 'w', encoding='utf-8') as f:
    f.write(new_content)

print("\n✅ Restoration complete!")
print("   data_quiz_data.js and data_quiz_data_utf8.js updated.")
