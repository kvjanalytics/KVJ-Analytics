import os

modules = [f"Module-{i}.html" for i in range(1, 7)]
directory = r"c:\Users\kj anand\Downloads\Quiz DD"

for module in modules:
    filepath = os.path.join(directory, module)
    if not os.path.exists(filepath):
        continue
    
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update CSS Variables
    content = content.replace("--bg-light: #f6f8fb;", "--bg-light: #ffffff;")
    
    # Update header banner to solid dark
    content = content.replace(
        "background: linear-gradient(135deg, var(--primary-blue) 0%, var(--brand-python) 100%);",
        "background: var(--primary-blue);"
    )
    
    # Ensure primary-blue is the dark color
    content = content.replace("--primary-blue: #1c1d1f;", "--primary-blue: #1c1d1f;") # No change needed but for clarity
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Modules updated to solid dark header and white body.")
