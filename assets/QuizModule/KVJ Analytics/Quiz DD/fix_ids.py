import re

def fix_ids_m3_v2():
    file_path = 'data_quiz_data.js'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the data3 section
    start_marker = '"data3": ['
    end_marker = '    ],'
    
    start_pos = content.find(start_marker)
    # Find the matching end_marker after start_pos
    # We look for the one that is NOT indented as much as questions
    # Assessment ends with '    ],' (4 spaces)
    # Questions end with '        },' (8 spaces)
    end_pos = content.find('\n' + end_marker, start_pos)
    if end_pos == -1:
        # try without newline
        end_pos = content.find(end_marker, start_pos)

    if start_pos == -1 or end_pos == -1:
        print(f"data3 section not found (start: {start_pos}, end: {end_pos})")
        return

    data3_content = content[start_pos:end_pos + len(end_marker)]
    
    # We want to find all 'id: X,' or 'id:X' or '"id": X' etc.
    current_id = 1
    def replace_id(match):
        nonlocal current_id
        # Preserve the prefix (spaces, quotes)
        prefix = match.group(1)
        res = f"{prefix}{current_id},"
        current_id += 1
        return res

    # Match 'id: X,' or '"id": X,'
    new_data3_content = re.sub(r'((?:"id"|id):\s*)\d+,', replace_id, data3_content)
    
    new_full_content = content[:start_pos] + new_data3_content + content[end_pos + len(end_marker):]
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_full_content)
    print(f"Successfully fixed {current_id - 1} IDs in data3")

fix_ids_m3_v2()
