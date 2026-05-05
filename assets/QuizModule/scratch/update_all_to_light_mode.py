import re
import os
import glob

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern for the dark code blocks
    pattern = r'<div style="background: #(1e293b|0f172a); padding: (25|30)px; border-radius: (12|16)px; color: #e2e8f0; font-family: \'Fira Code\', monospace; font-size: 1(4|5)px; overflow-x: auto;">'

    def replace_block(match):
        padding = match.group(2)
        radius = match.group(3)
        font_size = match.group(4)
        return f'<div style="background: #f8fafc; padding: {padding}px; border-radius: {radius}px; border: 1px solid #e2e8f0; color: #334155; font-family: \'Fira Code\', monospace; font-size: 1{font_size}px; overflow-x: auto;">'

    # 1. Replace the containers
    new_content = re.sub(pattern, replace_block, content)

    # 2. Replace the colors inside these containers
    new_content = new_content.replace('color: #38bdf8; margin-top: 0;', 'color: #0284c7; margin-top: 0;')
    new_content = new_content.replace('color: #94a3b8; margin-bottom:', 'color: #64748b; margin-bottom:')
    new_content = new_content.replace('color: #cbd5e1;">', 'color: #334155;">')
    new_content = new_content.replace('color: #34d399;', 'color: #059669;')
    new_content = new_content.replace('color: #fb7185;', 'color: #be123c;')
    new_content = new_content.replace('color: #94a3b8; text-align: left;', 'color: #64748b; text-align: left;')
    new_content = re.sub(r'color: #(38bdf8|34d399);">', r'color: #0284c7;">', new_content)
    new_content = new_content.replace('border-top: 1px solid #334155;', 'border-top: 1px solid #e2e8f0;')

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath} to light mode.")

# Process all HTML files
for html_file in glob.glob("*.html"):
    update_file(html_file)
