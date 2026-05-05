import glob
import re

files = glob.glob('*.html')
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    if 's3-21-role-ai' in content:
        new_content = content.replace('s3-21-role-ai', 's3-21-ai-role')
        with open(f, 'w', encoding='utf-8') as file:
            file.write(new_content)
        print(f'Updated {f}')
