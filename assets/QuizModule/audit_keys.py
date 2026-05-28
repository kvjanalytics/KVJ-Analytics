import re

path = r'Quiz DD/data_quiz_data.js'
with open(path, 'rb') as f:
    content = f.read().decode('utf-16')

keys = re.findall(r'["\'](\w+)["\']\s*:\s*\[', content)
print(keys)
