file_path = 'Data-Module-3.html'
with open(file_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'salesTrendChart' in line:
        print(f"Line {i+1}: {line.strip()}")
