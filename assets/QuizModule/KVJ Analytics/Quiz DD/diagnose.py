import re, os

files = {
    "quiz_data.js": r"c:\Users\kj anand\Downloads\Quiz DD (2) 7 (2)\Quiz DD (2) 6\Quiz DD (13) 6\Quiz DD\quiz_data.js",
    "data_quiz_data.js": r"c:\Users\kj anand\Downloads\Quiz DD (2) 7 (2)\Quiz DD (2) 6\Quiz DD (13) 6\Quiz DD\data_quiz_data.js",
    "data_quiz_data_utf8.js": r"c:\Users\kj anand\Downloads\Quiz DD (2) 7 (2)\Quiz DD (2) 6\Quiz DD (13) 6\Quiz DD\data_quiz_data_utf8.js",
}

def count_in_file(filepath, key):
    if not os.path.exists(filepath):
        return "NOT FOUND"
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    start = content.rfind(f'"{key}"')
    if start == -1:
        return "key not found"
    # Find next key (da_mock1 -> da_mock2, da_mock2 -> da_mock3)
    next_keys = ['da_mock2', 'da_mock3', 'da_mock1']
    end = len(content)
    for nk in next_keys:
        nk_str = f'"{nk}"'
        idx = content.find(nk_str, start + 10)
        if idx != -1 and idx < end:
            end = idx
    section = content[start:end]
    ids = re.findall(r'["\']?id["\']?\s*:\s*(\d+)', section)
    return f"{len(ids)} questions, IDs: {ids}"

for name, path in files.items():
    print(f"\n=== {name} ===")
    print(f"  da_mock1: {count_in_file(path, 'da_mock1')}")
    print(f"  da_mock2: {count_in_file(path, 'da_mock2')}")
