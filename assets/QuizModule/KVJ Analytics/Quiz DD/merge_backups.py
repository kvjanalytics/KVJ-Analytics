import os

backup_dir = r"C:\Users\kj anand\Downloads\Quiz DD (11)\Quiz DD"
target_dir = r"C:\Users\kj anand\Downloads\Quiz DD"

modules = [
    "Module-1.html",
    "Module-2.html",
    "Module-3.html",
    "Module-4.html",
    "Module-5.html",
    "Module-6.html"
]

for mod in modules:
    backup_path = os.path.join(backup_dir, mod)
    target_path = os.path.join(target_dir, mod)

    if not os.path.exists(backup_path):
        print(f"Skipping {mod}: Backup not found.")
        continue

    with open(backup_path, 'r', encoding='utf-8') as fb:
        backup_content = fb.read()

    with open(target_path, 'r', encoding='utf-8') as ft:
        target_content = ft.read()

    # Extract main content from backup safely using split
    try:
        backup_main = backup_content.split('<main class="main-content">')[1].split('</main>')[0]
        backup_script = backup_content.split('<script>')[1].split('</script>')[0]
    except IndexError:
        print(f"Skipping {mod}: Could not find main or script block in backup.")
        continue

    # Apply Udemy UI patches to the backup main content
    backup_main = backup_main.replace('<div class="coding-practice">', '<div class="practice-card coding-practice">')
    
    # We want to replace the target's main and script blocks.
    try:
        target_pre_main = target_content.split('<main class="main-content">')[0]
        target_post_main = target_content.split('</main>')[1]
        
        # Now target_content has the new main block
        target_content = target_pre_main + '<main class="main-content">' + backup_main + '</main>' + target_post_main
        
        target_pre_script = target_content.split('<script>')[0]
        target_post_script = target_content.split('</script>')[1]
        
        target_content = target_pre_script + '<script>' + backup_script + '</script>' + target_post_script
        
    except IndexError:
        print(f"Skipping {mod}: Could not find main or script block in target.")
        continue

    with open(target_path, 'w', encoding='utf-8') as ft:
        ft.write(target_content)

    print(f"Successfully restored {mod} from backup while preserving new UI.")
