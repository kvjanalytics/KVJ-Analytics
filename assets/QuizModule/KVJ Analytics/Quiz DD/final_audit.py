import re
import os

filepaths = [
    r"c:\Users\kj anand\Downloads\Quiz DD (2) 7 (2)\Quiz DD (2) 6\Quiz DD (13) 6\Quiz DD\data_quiz_data.js",
    r"c:\Users\kj anand\Downloads\Quiz DD (2) 7 (2)\Quiz DD (2) 6\Quiz DD (13) 6\Quiz DD\data_quiz_data (2).js",
    r"c:\Users\kj anand\Downloads\Quiz DD (2) 7 (2)\Quiz DD (2) 6\Quiz DD (13) 6\Quiz DD\quiz_data.js",
    r"c:\Users\kj anand\Downloads\Quiz DD (2) 7 (2)\Quiz DD (2) 6\Quiz DD (13) 6\Quiz DD\data_quiz_data_utf8.js",
    r"c:\Users\kj anand\Downloads\Quiz DD\data_quiz_data.js",
    r"c:\Users\kj anand\Downloads\Quiz DD\quiz_data.js"
]

def find_mock_bounds(content, key):
    pattern = rf'"{key}"\s*:\s*\['
    match = re.search(pattern, content)
    if not match: 
        pattern = rf"'{key}'\s*:\s*\["
        match = re.search(pattern, content)
    if not match: 
        pattern = rf'\b{key}\b\s*:\s*\['
        match = re.search(pattern, content)
    if not match: return None
        
    start_idx = match.start()
    array_open_idx = content.find('[', start_idx)
    bc = 0
    in_s = False
    for i in range(array_open_idx, len(content)):
        if content[i] == '"': in_s = not in_s
        if not in_s:
            if content[i] == '[': bc += 1
            elif content[i] == ']':
                bc -= 1
                if bc == 0: return content[start_idx:i+1]
    return None

for path in filepaths:
    if not os.path.exists(path): continue
    print(f"File: {path}")
    with open(path, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    for m in ['da_mock1', 'da_mock2']:
        m_str = find_mock_bounds(content, m)
        if m_str:
            # count '{'
            count = len(re.findall(r'\{', m_str))
            # verify IDs
            ids = re.findall(r'id["\']?\s*:\s*(\d+)', m_str, re.I)
            max_id = max([int(x) for x in ids]) if ids else 0
            print(f"  {m}: {count} questions, max ID: {max_id}")
        else:
            print(f"  {m}: NOT FOUND")
