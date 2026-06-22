import os
import re

def analyze_file(path):
    # Try multiple encodings
    content = None
    for enc in ['utf-8', 'utf-16', 'utf-16le', 'utf-16be']:
        try:
            with open(path, 'rb') as f:
                content = f.read().decode(enc)
            break
        except:
            continue
    
    if content is None:
        return
    
    # Simple check: does it contain "id": 60?
    if '"id": 60' in content or "'id': 60" in content or 'id: 60' in content:
        print(f'FILE HAS ID 60: {path}')

    matches = re.finditer(r'[\"\']?([a-zA-Z0-9_]+)[\"\']?\s*:\s*\[', content)
    for m in matches:
        key = m.group(1)
        if key in ["options", "a", "labels", "rows", "cols", "optionImages", "type", "q", "img", "optionTexts"]: continue
        
        p = m.end()
        d = 1
        j = p
        while j < len(content) and d > 0:
            if content[j] == '[': d += 1
            elif content[j] == ']': d -= 1
            j += 1
        sub = content[p:j]
        q_count = len(re.findall(r'\"id\"\s*:\s*\d+|[\"\']id[\"\']\s*:\s*\d+', sub))
        if q_count >= 50:
            print(f'File: {path}, Key: {key}, Count: {q_count}')

for root, dirs, files in os.walk(r'C:/Users/kj anand/Downloads/Quiz DD (13) 6/Quiz DD'):
    for file in files:
        if file.endswith('.js') or file.endswith('.json'):
            analyze_file(os.path.join(root, file))
