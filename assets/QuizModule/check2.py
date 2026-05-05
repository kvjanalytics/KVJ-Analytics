import re

with open('data_quiz_data.js', 'r', encoding='utf-8') as f:
    text = f.read()

# We just want to find all arrays and count the objects inside them with an 'id'
# Let's search for the 'marks: X' to calculate total marks.
for match in re.finditer(r'\"([^\"]+)\":\s*\[(.*?)\](?=\s*,|\s*\n\})', text, re.DOTALL):
    name = match.group(1)
    content = match.group(2)
    q_count = len(re.findall(r'id:\s*\d+', content))
    marks = re.findall(r'marks:\s*(\d+)', content)
    total_marks = sum(int(m) for m in marks) + (q_count - len(marks))
    print(f"{name}: {q_count} questions, {total_marks} marks")
