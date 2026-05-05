import re

file_path = r'c:\Users\kj anand\Downloads\Quiz DD\data_quiz_data.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

match = re.search(r'\"data1\": \[(.*?)^\s+\],', content, re.DOTALL | re.MULTILINE)

if match:
    data1_content = match.group(1)
    
    class Renumberer:
        def __init__(self):
            self.current_id = 1
        def __call__(self, m):
            res = f"id: {self.current_id}"
            self.current_id += 1
            return res
            
    renumberer = Renumberer()
    new_data1_content = re.sub(r'id:\s+\d+', renumberer, data1_content)
    
    new_content = content[:match.start(1)] + new_data1_content + content[match.end(1):]
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Renumbered data1 to {renumberer.current_id - 1} questions.")
else:
    print("Could not find data1.")
