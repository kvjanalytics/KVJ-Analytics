import os
import re

target_dir = r"C:\Users\kj anand\Downloads\Quiz DD"
modules = [f"Module-{i}.html" for i in range(1, 7)]

# The new button CSS matching the image palette
old_btn_run = r"\.btn-run \{ background: #a435f0; color: #ffffff; border: none; padding: 12px 25px; border-radius: 8px; font-weight: 700; cursor: pointer; transition: transform 0\.2s; margin-right: 10px; \}"
new_btn_run = ".btn-run { background: #38bdf8; color: #0f172a; border: none; padding: 12px 25px; border-radius: 8px; font-weight: 700; cursor: pointer; transition: transform 0.2s; margin-right: 10px; }"

old_btn_reset = r"\.btn-reset \{ background: transparent; color: #94a3b8; border: 1px solid #334155; padding: 12px 25px; border-radius: 8px; font-weight: 700; cursor: pointer; \}"
new_btn_reset = ".btn-reset { background: #334155; color: #f8fafc; border: none; padding: 12px 25px; border-radius: 8px; font-weight: 700; cursor: pointer; transition: transform 0.2s; }"

# Also update the textarea border slightly to match the image, the image shows a blue border on focus or by default.
old_textarea = r"\.coding-practice textarea \{[\s\S]*?\}"
new_textarea = """.coding-practice textarea {
            width: 100%; height: 120px;
            background: #0f172a; color: #38bdf8;
            border: 1px solid #0ea5e9; border-radius: 8px;
            padding: 15px; font-family: 'Fira Code', monospace; font-size: 14px;
            margin-bottom: 15px; outline: none; resize: vertical;
        }"""

for mod in modules:
    filepath = os.path.join(target_dir, mod)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace btn-run
    content = re.sub(old_btn_run, new_btn_run, content)
    # Replace btn-reset
    content = re.sub(old_btn_reset, new_btn_reset, content)
    # Replace textarea
    content = re.sub(old_textarea, new_textarea, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Updated palette for {mod}")
