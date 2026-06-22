import os
import json

paths = [
    r'C:/Users/kj anand/Downloads/Quiz DD (13) 6/Quiz DD/data_quiz_data.js',
    r'C:/Users/kj anand/Downloads/Quiz DD (13) 6/Quiz DD/data_quiz_data (2).js',
    r'C:/Users/kj anand/Downloads/Quiz DD (13) 6/Quiz DD/quiz_data.js',
    r'C:/Users/kj anand/Downloads/Quiz DD (13) 6/Quiz DD/mock3_1_20.json',
    r'C:/Users/kj anand/Downloads/Quiz DD (13) 6/Quiz DD/mock3_21_40.json'
]

def analyze_file(file_path):
    if not os.path.exists(file_path):
        print(f'File not found: {file_path}')
        return

    content = None
    # Extensive encoding list for robustness
    encodings = ['utf-16', 'utf-8', 'utf-16le', 'utf-16be', 'latin-1', 'cp1252']
    for enc in encodings:
        try:
            with open(file_path, 'rb') as f:
                content = f.read().decode(enc)
            break
        except Exception:
            continue
    
    if content is None:
        print(f'Could not decode {os.path.basename(file_path)}')
        return

    print(f'\n--- Analyzing {os.path.basename(file_path)} ---')
    if file_path.endswith('.json'):
        try:
            obj = json.loads(content)
            if isinstance(obj, list):
                print(f'JSON List: {len(obj)} items')
            elif isinstance(obj, dict):
                print(f'JSON Dict: {len(obj.keys())} keys')
        except:
            print('JSON Parse failed')
            # Simple string count
            q_count = content.count('"id":')
            print(f'Estimated questions: {q_count}')
    else:
        keys = ['da_mock1', 'da_mock2', 'da_mock3', 'data1', 'data2', 'data3', 'data4', 'data5', '1', '2', '3', 'mock1', 'mock2', 'mock3']
        for key in keys:
            # Look for "key": [ or key: [
            patterns = [f'"{key}":', f"'{key}':", f'{key}:']
            found = False
            for p in patterns:
                if p in content:
                    start_idx = content.find(p)
                    sub_content = content[start_idx:]
                    
                    # Find next top-level key or end of object
                    # This is tricky without a full parser, but we can look for "next_key": [
                    next_idxs = []
                    for k2 in keys:
                        if k2 == key: continue
                        for p2 in patterns:
                            idx = sub_content.find(p2)
                            if idx != -1 and idx > 0: # Must be after current key
                                # Check if it looks like a key start
                                next_idxs.append(idx)
                    
                    if next_idxs:
                        end_idx = min(next_idxs)
                        actual_data = sub_content[:end_idx]
                    else:
                        actual_data = sub_content
                    
                    q_count = actual_data.count('"id":') + actual_data.count("'id':") + actual_data.count("id:")
                    print(f'{key}: {q_count} questions')
                    found = True
                    break

if __name__ == '__main__':
    for p in paths:
        analyze_file(p)
