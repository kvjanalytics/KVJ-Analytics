import os

path = r'C:/Users/kj anand/Downloads/Quiz DD (13) 6/Quiz DD/data_quiz_data.js'
temp_path = r'C:/Users/kj anand/Downloads/Quiz DD (13) 6/Quiz DD/data_quiz_data_utf8.js'

with open(path, 'rb') as f:
    content = f.read().decode('utf-16')

with open(temp_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f'Converted {path} to UTF-8 at {temp_path}')
