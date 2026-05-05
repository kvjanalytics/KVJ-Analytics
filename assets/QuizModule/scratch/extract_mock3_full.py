import re

file_path = r'c:\Users\kj anand\Downloads\Quiz DD\quiz_data.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find the start of da_mock3
start_match = re.search(r'\"da_mock3\": \[', content)
if start_match:
    start_pos = start_match.end()
    # Find the matching closing bracket ] for the array
    # Since there are nested brackets, we need to count them or look for the pattern ending the object
    
    # Actually, da_mock3 is at the end of the file.
    # It ends with ] };
    end_pos = content.rfind(']')
    
    da_mock3_content = content[start_pos:end_pos].strip()
    
    # Let's verify it has questions
    count = len(re.findall(r'\"id\":\s+\d+|id:\s+\d+', da_mock3_content))
    print(f"Extracted da_mock3 with {count} questions.")
    
    with open(r'c:\Users\kj anand\Downloads\Quiz DD\scratch\da_mock3_full.txt', 'w', encoding='utf-8') as f:
        f.write(da_mock3_content)
else:
    print("da_mock3 not found.")
