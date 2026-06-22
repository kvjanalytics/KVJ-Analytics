import re

BASE = r"C:\Users\kj anand\Downloads\Quiz DD (13) 6\Quiz DD"

with open(BASE + r"\data_quiz_data_utf8.js", 'r', encoding='utf-8') as f:
    content = f.read()

start = content.find('"da_mock3":')
section = content[start:]

# Find Q44
q44_match = re.search(r'"id":\s*44.*?(?="id":\s*\d|\]\s*[,}])', section, re.DOTALL)
if q44_match:
    print("Q44 content:")
    print(q44_match.group(0)[:2000])
