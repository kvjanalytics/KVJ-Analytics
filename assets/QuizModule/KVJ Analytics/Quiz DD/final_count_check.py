import os
import re

def analyze_file(path, label):
    print(f'--- Analyzing {label}: {path} ---')
    if not os.path.exists(path):
        print('File not found')
        return
    
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
        print('Could not decode file')
        return

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
        if q_count > 5:
            print(f'Key: {key}, Line: {content.count("\n", 0, m.start())+1}, Questions: {q_count}')

analyze_file(r'C:/Users/kj anand/Downloads/Quiz DD (13) 6/Quiz DD/quiz_data.js', 'quiz_data.js')
analyze_file(r'C:/Users/kj anand/Downloads/Quiz DD (13) 6/Quiz DD/data_quiz_data.js', 'data_quiz_data.js')
analyze_file(r'C:/Users/kj anand/Downloads/Quiz DD (13) 6/Quiz DD/data_quiz_data (2).js', 'data_quiz_data (2).js')
