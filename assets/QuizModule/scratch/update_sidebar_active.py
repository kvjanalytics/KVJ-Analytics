import os

files = [
    r"c:\Users\kj anand\Downloads\Quiz DD\Data-Module-1.html",
    r"c:\Users\kj anand\Downloads\Quiz DD\Data-Module-2.html",
    r"c:\Users\kj anand\Downloads\Quiz DD\Data-Module-3.html",
    r"c:\Users\kj anand\Downloads\Quiz DD\Data-Module-4.html",
    r"c:\Users\kj anand\Downloads\Quiz DD\Data-Module-5.html"
]

target = """        .sidebar a.active {
            color: var(--primary-blue); font-weight: 700;
            background: #eff6ff; border-left: 4px solid var(--primary-blue);
        }"""

replacement = """        .sidebar a.active {
            color: white; font-weight: 800;
            background: var(--primary-blue); border-radius: 20px;
            box-shadow: 0 4px 12px rgba(30, 58, 95, 0.2);
        }"""

for file_path in files:
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if target in content:
            new_content = content.replace(target, replacement)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {file_path}")
        else:
            # Check if it was already updated or has slight variation
            if replacement in content:
                print(f"Already updated {file_path}")
            else:
                print(f"Target not found in {file_path}")
    else:
        print(f"File not found: {file_path}")
