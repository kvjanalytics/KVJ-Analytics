import os
import re

def clear_textareas(filepath):
    print(f"Clearing textareas in: {filepath}")
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Replace placeholder text with generic one
    # We want to replace placeholders that contain code or solutions
    # Pattern matches placeholder="anything_suspect"
    def placeholder_cleaner(match):
        p = match.group(0)
        # If it looks like it already has the generic placeholder, keep it
        if "# Write your code here..." in p:
            return p
        # Otherwise, replace with generic
        return 'placeholder="# Write your code here..." '

    content = re.sub(r'placeholder=".*?"', placeholder_cleaner, content)

    # 2. Clear content between tags <textarea ...>CONTENT</textarea>
    # ONLY if it's not a special partial fix template (we identified these in previous turns)
    # Actually, to be safe, we clear all and let the CHALLENGE_DATA templates handle restoration if they were designed that way.
    # Looking at my runSkulpt, I don't restore the value, I just use it.
    # So I will clear content that looks like a solution.
    
    # Exceptions for "Partial-Fix" templates if any were hardcoded (none observed except Mod 5 try/except)
    # I'll clear the ones in Module 5 too as per user request.
    content = re.sub(r'(<textarea[^>]*>).*?(</textarea>)', r'\1\2', content, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

modules = [f"Module-{i}.html" for i in range(1, 7)]
workspace = r"c:\Users\kj anand\Downloads\Quiz DD"

for m in modules:
    path = os.path.join(workspace, m)
    if os.path.exists(path):
        clear_textareas(path)
