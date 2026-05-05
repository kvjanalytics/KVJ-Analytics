import re
import os
import glob

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace the too-light gray text with dark slate
    content = content.replace('color: #94a3b8;', 'color: #1e293b; font-weight: 600;')
    content = content.replace('color: #64748b;', 'color: #1e293b; font-weight: 600;')
    
    # 2. Replace the too-light blue headers with dark blue
    content = content.replace('color: #38bdf8;', 'color: #1e3a8a; font-weight: 800;')
    content = content.replace('color: #0284c7;', 'color: #1e3a8a; font-weight: 800;')
    
    # 3. Ensure the values (numbers) are also dark
    # For tags like <td style="text-align: right;">5.000000</td>
    content = content.replace('<td style="text-align: right;">', '<td style="text-align: right; color: #1e293b; font-weight: 700;">')
    
    # 4. Handle any remaining light text in the output tables
    content = content.replace('color: #cbd5e1;', 'color: #1e293b;')
    
    # 5. Fix the headers specifically in the Premium Code Card
    # If there's an h4 with #0284c7 (which I used in beautify), darken it
    content = content.replace('color: #0284c7;', 'color: #1e3a8a;')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Deeply darkened text in {filepath} for maximum visibility.")

# Process all HTML files
for html_file in glob.glob("*.html"):
    update_file(html_file)
