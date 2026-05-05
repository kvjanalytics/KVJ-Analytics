import os

old_url = "https://script.google.com/macros/s/AKfycbzIXsxw9CidSI8w23b5x_DrKogVHjwknQ67zEcWjYv8kKOtXCF9KGPM2CrqxmBVqUEX/exec"
new_url = "https://script.google.com/macros/s/AKfycbxs8bcb1jw5qpazffbr1U5KvM_PzqAhb_9F3xOSjBQxuu1KaJYFC_DkUovfuloGCCq-/exec"

files_to_update = [
    "auth.js",
    "checkout.html",
    "index.html",
    "login.html",
    "module_quiz.html",
    "registration.html",
    "roadmap.html",
    "data_roadmap.html"
]

for filename in files_to_update:
    path = os.path.join("c:/Users/kj anand/Downloads/Quiz DD", filename)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace the literal old URL
        if old_url in content:
            new_content = content.replace(old_url, new_url)
            with open(path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated URL in {filename}")
        else:
            # Fallback regex if it's slightly different
            import re
            new_content = re.sub(r'https://script\.google\.com/macros/s/[^/]+/exec', new_url, content)
            if new_content != content:
                with open(path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated URL (via regex) in {filename}")
            else:
                print(f"URL not found in {filename} or already updated.")
    else:
        print(f"File {filename} not found.")
