import re
import sys
with open('Data-Module-3.html', 'r', encoding='utf-8') as f:
    text = f.read()

ids = re.findall(r'id="([^"]+)"', text)
s_ids = [i for i in ids if i.startswith('s')]
with open('ids.txt', 'w', encoding='utf-8') as out:
    for i in s_ids:
        out.write(i + '\n')
