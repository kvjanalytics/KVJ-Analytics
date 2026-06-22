import re, shutil, os

filepath = r"c:\Users\kj anand\Downloads\Quiz DD (2) 7 (2)\Quiz DD (2) 6\Quiz DD (13) 6\Quiz DD\data_quiz_data.js"

shutil.copy(filepath, filepath + '.bak2')

with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
    content = f.read()

# This file has da_mock2 starting around line 2053 and da_mock3 at line 2660
# In this file, da_mock2 ends at the closing ], before "da_mock3"
mock2_idx = content.rfind('"da_mock2"')
mock3_idx = content.find('"da_mock3"', mock2_idx)

mock2_section = content[mock2_idx:mock3_idx]
print(f"da_mock2 section length: {len(mock2_section)}")

# Count IDs in da_mock2
ids = re.findall(r'"id"\s*:\s*(\d+)', mock2_section)
print(f"IDs found in da_mock2: {ids}")

# Remove question objects with id 41 and 42
# Pattern matches: ,\n        {\n            "id": 41, ... last closing brace before next question
def remove_question_by_id(section, qid):
    # Match a comma, then a JSON object containing the given id
    pattern = r',\s*\{(?=[^{}]*?"id"\s*:\s*' + str(qid) + r'\b)[^{}]*(?:\{[^{}]*\}[^{}]*)?\}'
    result = re.sub(pattern, '', section, flags=re.DOTALL)
    if result == section:
        print(f"WARNING: id {qid} not removed — pattern not matched")
    else:
        print(f"OK: Removed question id={qid}")
    return result

mock2_new = remove_question_by_id(mock2_section, 41)
mock2_new = remove_question_by_id(mock2_new, 42)

ids_after = re.findall(r'"id"\s*:\s*(\d+)', mock2_new)
print(f"IDs after removal: {ids_after}")

new_content = content[:mock2_idx] + mock2_new + content[mock3_idx:]
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_content)
print("Done.")
