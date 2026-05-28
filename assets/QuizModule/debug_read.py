import os
import json

def find_block(content, name):
    start_marker = f'\"{name}\": ['
    start_idx = content.find(start_marker)
    if start_idx == -1:
        print(f"NOT FOUND: {name}")
        return
    
    bracket_count = 0
    end_idx = -1
    for i in range(start_idx + len(start_marker) - 1, len(content)):
        if content[i] == '[':
            bracket_count += 1
        elif content[i] == ']':
            bracket_count -= 1
            if bracket_count == 0:
                end_idx = i + 1
                break
    
    if end_idx != -1:
        snippet = content[start_idx:end_idx]
        print(f"SUCCESS: Found {name} block ({len(snippet)} chars)")
        # count manually
        count = snippet.count('\"id\":')
        print(f"Manual count of '\"id\":' in {name}: {count}")
        
        # Save to a file for inspection
        with open(f"extracted_{name}.json", "w", encoding="utf-8") as out:
            out.write("{" + snippet + "}")
    else:
        print(f"Could not find end of {name} array")

def try_read(path):
    print(f"\n--- Scanning {os.path.basename(path)} ---")
    encodings = ['utf-16le', 'utf-8']
    for enc in encodings:
        try:
            with open(path, 'r', encoding=enc, errors='ignore') as f:
                content = f.read()
            print(f"Read {path} with {enc} (len: {len(content)})")
            find_block(content, "mock3")
            find_block(content, "da_mock3")
            # Also look for any large array if we suspect it
        except Exception as e:
            print(f"Failed with {enc}: {e}")

try_read(r'C:/Users/kj anand/Downloads/Quiz DD (13) 6/Quiz DD/quiz_data.js')
try_read(r'C:/Users/kj anand/Downloads/Quiz DD (13) 6/Quiz DD/data_quiz_data.js')
