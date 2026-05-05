import re

file_path = r'c:\Users\kj anand\Downloads\Quiz DD\quiz_data.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find the start of da_mock3
# "da_mock3": [
# ...
# ],
# "data1": [

start_pattern = r'\"da_mock3\": \['
end_pattern = r'^\s+\],\s+\"data1\": \['

match = re.search(f"{start_pattern}(.*?){end_pattern}", content, re.DOTALL | re.MULTILINE)

if match:
    data = match.group(1).strip()
    with open(r'c:\Users\kj anand\Downloads\Quiz DD\scratch\da_mock3_correct.txt', 'w', encoding='utf-8') as f:
        f.write(data)
    print("Extracted da_mock3 correctly.")
else:
    print("Could not find da_mock3 with the specified boundaries.")
