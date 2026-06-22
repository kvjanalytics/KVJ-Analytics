import os
import re

def heal_module(filepath):
    print(f"Healing: {filepath}")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Pattern to find a (possibly mangled) textarea tag and its corresponding closing tag
    # We target the id specifically as it's the anchor of our logic
    # We look for <textarea id="coding-ans-..." and we want to replace it and its content up to </textarea>
    
    # This regex handles the case where the opening tag is broken (missing closing >) 
    # or followed by garbage until a </textarea>
    def replacement_logic(match):
        id_str = match.group(1)
        return f'<textarea id="{id_str}" placeholder="# Write your code here..."></textarea>'

    # Search for <textarea id="coding-ans-xyz" followed by anything (non-greedy) until </textarea>
    # The [^>]*? handle the attributes, and .*? handles any content accidentally put inside
    # We use a pattern that is robust even if the opening tag was mangled
    pattern = r'<textarea\s+id="(coding-ans-[a-zA-Z0-9-]+)"[^>]*?>.*?</textarea>'
    
    # First, let's fix the case where the opening tag was mangled (e.g. missing >)
    # If a tag looks like <textarea id="abc" placeholder="... > ...
    # It might have been split across lines or just weird.
    
    # IMPROVED HEALER:
    # 1. Identify all coding-ans- IDs in the file
    ids = re.findall(r'id="(coding-ans-[a-zA-Z0-9-]+)"', content)
    
    for cid in ids:
        # For each ID, we want to find the block from the START of the textarea tag to the END of its closing tag
        # Even if mangled.
        # We'll search for the tag starting with <textarea and containing the ID
        # and replace everything from <textarea to </textarea> specifically for that ID.
        sub_pattern = r'<textarea\s+id="' + re.escape(cid) + r'".*?</textarea>'
        # We use re.DOTALL to ensure it matches across newlines
        content = re.sub(sub_pattern, f'<textarea id="{cid}" placeholder="# Write your code here..."></textarea>', content, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

modules = [f"Module-{i}.html" for i in range(1, 7)]
workspace = r"c:\Users\kj anand\Downloads\Quiz DD"

for m in modules:
    path = os.path.join(workspace, m)
    if os.path.exists(path):
        heal_module(path)
    else:
        print(f"Skipping: {path}")
