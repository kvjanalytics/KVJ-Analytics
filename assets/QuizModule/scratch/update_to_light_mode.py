import re

with open('Data-Module-2.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Pattern for the dark code blocks
pattern = r'<div style="background: #0f172a; padding: (25|30)px; border-radius: (12|16)px; color: #e2e8f0; font-family: \'Fira Code\', monospace; font-size: 1(4|5)px; overflow-x: auto;">'

def replace_block(match):
    padding = match.group(1)
    radius = match.group(2)
    font_size = match.group(3)
    return f'<div style="background: #f8fafc; padding: {padding}px; border-radius: {radius}px; border: 1px solid #e2e8f0; color: #334155; font-family: \'Fira Code\', monospace; font-size: 1{font_size}px; overflow-x: auto;">'

# 1. Replace the containers
content = re.sub(pattern, replace_block, content)

# 2. Replace the colors inside these containers
# Header color
content = content.replace('color: #38bdf8; margin-top: 0;', 'color: #0284c7; margin-top: 0;')
# Comment color
content = content.replace('color: #94a3b8; margin-bottom:', 'color: #64748b; margin-bottom:')
# Code color (text inside the div)
content = content.replace('color: #cbd5e1;">', 'color: #334155;">')
# String color
content = content.replace('color: #34d399;', 'color: #059669;')
# Lambda color (used in mode)
content = content.replace('color: #fb7185;', 'color: #be123c;')
# Output header color
content = content.replace('color: #94a3b8; text-align: left;', 'color: #64748b; text-align: left;')
# Table text color inside output
content = re.sub(r'color: #38bdf8;">', r'color: #0284c7;">', content)
# Border color
content = content.replace('border-top: 1px solid #334155;', 'border-top: 1px solid #e2e8f0;')

with open('Data-Module-2.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated all blocks in Data-Module-2.html to light mode.")
