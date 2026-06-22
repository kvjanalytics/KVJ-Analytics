import os
import re

target_dir = r"C:\Users\kj anand\Downloads\Quiz DD"
modules = [f"Module-{i}.html" for i in range(1, 7)]

# Fix 1: Make strong tags visible inside practice-card
old_practice_card = r"\.practice-card p \{ color: #e2e8f0; font-size: 16px; margin-bottom: 20px; \}"
new_practice_card = ".practice-card p { color: #e2e8f0; font-size: 16px; margin-bottom: 20px; }\n        .practice-card strong { color: #f8fafc; font-weight: 800; }"

# Fix 2: Change sidebar pink/purple to black
old_sidebar_h3 = r"\.sidebar h3 \{[\s\S]*?color: var\(--brand-python\);[\s\S]*?\}"
new_sidebar_h3 = """.sidebar h3 {
            font-family: 'Montserrat', sans-serif; font-size: 12px;
            color: var(--primary-blue); text-transform: uppercase;
            margin-bottom: 20px; border-bottom: 2px solid var(--bg-light);
            padding-bottom: 10px; font-weight: 800; letter-spacing: 1px;
        }"""

old_sidebar_active = r"\.sidebar a\.active \{[\s\S]*?\}"
new_sidebar_active = """.sidebar a.active {
            color: var(--primary-blue); font-weight: 700;
            background: #f1f5f9; border-left: 4px solid var(--primary-blue);
        }"""

old_sidebar_hover = r"\.sidebar a:hover:not\(\.active\) \{ background: #f8fafc; color: var\(--brand-python\); \}"
new_sidebar_hover = ".sidebar a:hover:not(.active) { background: #f8fafc; color: var(--primary-blue); }"


for mod in modules:
    filepath = os.path.join(target_dir, mod)
    if not os.path.exists(filepath):
        continue
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Fix strong tags in practice cards
    if ".practice-card strong" not in content:
        content = re.sub(old_practice_card, new_practice_card, content)

    # 2. Fix sidebar styles
    content = re.sub(old_sidebar_h3, new_sidebar_h3, content)
    content = re.sub(old_sidebar_active, new_sidebar_active, content)
    content = re.sub(old_sidebar_hover, new_sidebar_hover, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print(f"Fixed styles for {mod}")
