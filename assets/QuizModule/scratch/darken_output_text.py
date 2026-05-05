import re
import os
import glob

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Darken the table row labels (count, mean, etc.)
    # These currently use the default color or inherited color which might be too light in the screenshot.
    # I'll specifically target the td tags in the output table.
    content = content.replace('<td style="padding: 6px 0;">', '<td style="padding: 6px 0; color: #1e293b; font-weight: 500;">')
    content = content.replace('<td style="padding: 4px 0;">', '<td style="padding: 4px 0; color: #1e293b; font-weight: 500;">')
    
    # 2. Darken the table headers
    content = content.replace('color: #64748b; text-align: left;', 'color: #1e293b; text-align: left; font-weight: 700;')
    
    # 3. Darken the numbers (the values) for even better contrast
    content = content.replace('color: #0284c7;">', 'color: #0369a1; font-weight: 700;">')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {filepath} with darker text for better readability.")

# Process all HTML files
for html_file in glob.glob("*.html"):
    update_file(html_file)
