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

def count_ids(text):
    # Match id: or "id": or 'id':
    return len(re.findall(r'(\"id\"|\'id\'|\bid\b)\s*:', text))

for path in filepaths:
    if not os.path.exists(path): continue
    print(f"File: {path}")
    with open(path, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    
    # Simple search for the mocks
    for mock in ['da_mock1', 'da_mock2']:
        start = content.find(f'"{mock}"')
        if start == -1: start = content.find(f"'{mock}'")
        if start == -1: start = content.find(f"{mock}:")
        
        if start != -1:
            # Look for the end of the array
            bracket_count = 0
            array_start = content.find('[', start)
            if array_start != -1:
                end = -1
                in_string = False
                for i in range(array_start, len(content)):
                    if content[i] == '"': in_string = not in_string
                    if not in_string:
                        if content[i] == '[': bracket_count += 1
                        elif content[i] == ']':
                            bracket_count -= 1
                            if bracket_count == 0:
                                end = i + 1
                                break
                if end != -1:
                    mock_content = content[array_start:end]
                    print(f"  {mock}: {count_ids(mock_content)} questions")
        else:
            print(f"  {mock}: NOT FOUND")
