import re

with open('data_quiz_data.js', 'r', encoding='utf-8') as f:
    text = f.read()

# remove 'var dataQuizData = '
text = re.sub(r'var\s+dataQuizData\s*=\s*', '', text).strip()
if text.endswith(';'): text = text[:-1]

# split by the module names
matches = re.finditer(r'\"(da_[^\"]+|data\d+|mock\d+)\":\s*\[(.*?)\]\s*(?:,|}|\n\n)', text, re.DOTALL)
for m in matches:
    name = m.group(1)
    content = m.group(2)
    
    # count questions
    qs = content.split('id:')
    if len(qs) < 2:
        continue
    q_count = len(qs) - 1
    
    marks_total = 0
    for q in qs[1:]:
        match_marks = re.search(r'marks:\s*(\d+)', q)
        if match_marks:
            marks_total += int(match_marks.group(1))
        else:
            marks_total += 1
            
    print(f'{name}: {q_count} questions, {marks_total} marks')
