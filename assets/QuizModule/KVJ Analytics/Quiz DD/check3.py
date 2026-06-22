import re
import sys

def parse():
    with open('data_quiz_data.js', 'r', encoding='utf-8') as f:
        text = f.read()

    # Split by module keys roughly: "data1": [, "data2": [
    parts = re.split(r'\"(da_mock\d+|data\d+|mock\d+)\":\s*\[', text)
    
    for i in range(1, len(parts), 2):
        name = parts[i]
        content = parts[i+1]
        
        # We only want the array content, so we cut at the first `],` that seems to end the array.
        # But this can be tricky. Let's just find all `id: \d+` or `id:\d+` followed by `marks: \d+`.
        
        # First, find how many questions there are. They usually have 'id: ' or 'id:'
        qs = re.findall(r'id:\s*\d+', content)
        q_count = len(qs)
        
        # Then find all marks
        marks = re.findall(r'marks:\s*(\d+)', content)
        
        # wait, if q_count > 0, it's a module
        if q_count > 0:
            total_marks = sum(int(m) for m in marks) + (q_count - len(marks))
            print(f'{name}: {q_count} questions, {total_marks} marks')

parse()
