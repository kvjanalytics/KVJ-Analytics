import re

files = [
    r'c:\Users\kj anand\Downloads\Quiz DD\data_quiz_data.js',
    r'c:\Users\kj anand\Downloads\Quiz DD\quiz_data.js',
]

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find data1 section
    data1_start = content.find('"data1": [')
    if data1_start == -1:
        print(f"WARNING: data1 not found in {filepath}")
        continue
    
    bracket_pos = content.find('[', data1_start)
    depth = 0
    data1_end = bracket_pos
    for i in range(bracket_pos, len(content)):
        if content[i] == '[':
            depth += 1
        elif content[i] == ']':
            depth -= 1
            if depth == 0:
                data1_end = i
                break
    
    data1_block = content[data1_start:data1_end+1]
    original_block = data1_block

    # Use regex to find and transform q: "(...)" patterns
    # Pattern: q: "(X Mark/Marks) rest of text"
    # The q value may contain escaped sequences but we match the marks prefix
    
    def replacer(m):
        marks_label = m.group(1)   # e.g. "1 Mark" or "4 Marks"
        rest = m.group(2)          # rest of q text (may have HTML)
        return f', q: "{rest} ({marks_label})"'
    
    # Match:  , q: "(N Mark/Marks) <rest>"
    # rest can contain anything except unescaped "
    new_block = re.sub(
        r', q: "\((\d+ Marks?)\) ((?:[^"\\]|\\.)*)\"',
        replacer,
        data1_block
    )
    
    if new_block != original_block:
        new_content = content[:data1_start] + new_block + content[data1_end+1:]
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated: {filepath}")
        # Show changed lines
        old_lines = original_block.split('\n')
        new_lines = new_block.split('\n')
        for i, (old, new) in enumerate(zip(old_lines, new_lines)):
            if old != new:
                print(f"  Line {i+1}:")
                # find first difference
                diff_pos = next((j for j in range(min(len(old),len(new))) if old[j] != new[j]), 0)
                print(f"  OLD: ...{old[max(0,diff_pos-20):diff_pos+60]}")
                print(f"  NEW: ...{new[max(0,diff_pos-20):diff_pos+60]}")
                print()
    else:
        print(f"No changes in data1 found in: {filepath}")

print("Done!")
