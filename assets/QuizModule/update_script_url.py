import os

old_url = "https://script.google.com/macros/s/AKfycbwKpqYE5bUkT3IdyDo95KlkRTVkw-mXTYMh0f6yypNteEVuAe_JeO6CYWOSKH5X6quZ/exec"
new_url = "https://script.google.com/macros/s/AKfycbw9mb2dsJ1SSheOcpdcdeE8eKNnuCjK2U9U9kIeHV_2yga8Ujiee1w_huTzc2w5BpWD/exec"

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
