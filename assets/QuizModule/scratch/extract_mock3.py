import re

file_path = r'c:\Users\kj anand\Downloads\Quiz DD\quiz_data.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'\"da_mock3\": \[(.*?)^\s+\],', content, re.DOTALL | re.MULTILINE)

if match:
    print(f"Found da_mock3 content. Length: {len(match.group(1))}")
    with open(r'c:\Users\kj anand\Downloads\Quiz DD\scratch\da_mock3.txt', 'w', encoding='utf-8') as f:
        f.write(match.group(1))
else:
    # Try searching for it at the end of the file
    match = re.search(r'\"da_mock3\": \[(.*?)\};', content, re.DOTALL | re.MULTILINE)
    if match:
        print(f"Found da_mock3 content (at end). Length: {len(match.group(1))}")
        with open(r'c:\Users\kj anand\Downloads\Quiz DD\scratch\da_mock3.txt', 'w', encoding='utf-8') as f:
            f.write(match.group(1))
    else:
        print("da_mock3 not found in quiz_data.js")
