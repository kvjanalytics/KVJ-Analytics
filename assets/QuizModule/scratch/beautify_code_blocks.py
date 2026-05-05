import re
import os
import glob

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern for the previous light code blocks
    pattern = r'<div style="background: #f8fafc; padding: (25|30)px; border-radius: (12|16)px; border: 1px solid #e2e8f0; color: #334155; font-family: \'Fira Code\', monospace; font-size: 1(4|5)px; overflow-x: auto;">'

    def replace_block(match):
        padding = match.group(1)
        radius = match.group(2)
        font_size = match.group(3)
        # New "Beautiful Box" design: Soft card with a gradient accent and refined shadow
        return (f'<div class="premium-code-card" style="background: white; padding: {padding}px; border-radius: 16px; '
                f'border: 1px solid #e2e8f0; border-left: 6px solid #3b82f6; box-shadow: 0 10px 25px rgba(0,0,0,0.05); '
                f'color: #334155; font-family: \'Fira Code\', monospace; font-size: 1{font_size}px; overflow-x: auto; '
                f'margin: 25px 0; position: relative; transition: transform 0.2s ease;">')

    # 1. Replace the containers
    new_content = re.sub(pattern, replace_block, content)

    # 2. Refine the header to be more "Beautiful"
    header_pattern = r'<h4 style="color: #0284c7; margin-top: 0; margin-bottom: 15px; font-size: 13px; text-transform: uppercase; letter-spacing: 1px;">Python Implementation \(Pandas\)</h4>'
    beautiful_header = (
        '<div style="display: flex; align-items: center; gap: 10px; margin-bottom: 20px; border-bottom: 1px solid #f1f5f9; padding-bottom: 15px;">'
        '<svg style="width: 20px; height: 20px; color: #3b82f6;" fill="none" stroke="currentColor" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 20l4-16m4 4l4 4-4 4M6 16l-4-4 4-4"></path></svg>'
        '<h4 style="color: #1e3a8a; margin: 0; font-size: 14px; font-weight: 800; text-transform: uppercase; letter-spacing: 1.5px; font-family: \'Montserrat\', sans-serif;">Python Implementation</h4>'
        '<span style="background: #eff6ff; color: #3b82f6; font-size: 10px; padding: 2px 8px; border-radius: 20px; font-weight: 700; margin-left: auto; border: 1px solid #dbeafe;">PANDAS</span>'
        '</div>'
    )
    new_content = new_content.replace(header_pattern, beautiful_header)
    
    # 3. Refine the header for the larger blocks
    large_header_pattern = r'<h4 style="color: #0284c7; margin-top: 0; margin-bottom: 20px; font-size: 14px; text-transform: uppercase; letter-spacing: 1.5px;">Python Implementation \(Pandas\)</h4>'
    new_content = new_content.replace(large_header_pattern, beautiful_header)

    # 4. Refine the "Output:" label
    output_label_pattern = r'<div style="font-weight: 700; color: #64748b; margin-bottom: 1(0|5)px;">Output:</div>'
    beautiful_output = (
        '<div style="display: flex; align-items: center; gap: 8px; margin-top: 20px; margin-bottom: 15px;">'
        '<div style="width: 8px; height: 8px; background: #3b82f6; border-radius: 50%;"></div>'
        '<div style="font-weight: 800; color: #1e3a8a; font-size: 12px; text-transform: uppercase; letter-spacing: 1px;">Output Console</div>'
        '<div style="flex: 1; height: 1px; background: #f1f5f9; margin-left: 10px;"></div>'
        '</div>'
    )
    new_content = re.sub(output_label_pattern, beautiful_output, new_content)

    # 5. Fix the border-top that might have been added
    new_content = new_content.replace('border-top: 1px solid #e2e8f0; padding-top: 15px;', 'padding-top: 5px;')
    new_content = new_content.replace('border-top: 1px solid #e2e8f0; padding-top: 20px;', 'padding-top: 5px;')

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Upgraded {filepath} to 'Beautiful Box' design.")

# Process all HTML files
for html_file in glob.glob("*.html"):
    update_file(html_file)
