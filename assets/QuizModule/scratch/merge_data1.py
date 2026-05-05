import re
import json

file_path = r'c:\Users\kj anand\Downloads\Quiz DD\data_quiz_data.js'

with open(file_path, 'r', encoding='utf-8') as f:
    content = f.read()

# Find the first data1 definition
# "data1": [ ... ]
match1 = re.search(r'\"data1\": \[(.*?)^\s+\],', content, re.DOTALL | re.MULTILINE)
# Find the second data1 definition
match2 = re.search(r'\"data1\": \[(.*?)^\s+\],?\s+\};', content, re.DOTALL | re.MULTILINE)

if match1 and match2:
    data1_v1 = match1.group(1).strip()
    data1_v2 = match2.group(1).strip()
    
    # We want to keep BOTH sets.
    # We will put the new ones (v2) at the beginning as they seem more fundamental.
    
    # Renumbering v1 (original 10 questions) to start from 6
    # Pattern to find id: X
    def renumber_v1(m):
        old_id = int(m.group(1))
        return f"id: {old_id + 5}"
    
    data1_v1_renumbered = re.sub(r'id:\s+(\d+)', renumber_v1, data1_v1)
    
    # Combined content
    combined_content = data1_v2 + ",\n        " + data1_v1_renumbered
    
    # Update the first occurrence and delete the second
    # First, replace match1 with combined content
    new_content = content[:match1.start(1)] + combined_content + content[match1.end(1):]
    
    # Now find the second occurrence in the NEW content (it might have shifted)
    # The second occurrence starts after match1 ends.
    second_occ_start = match1.end() + len(combined_content) - len(match1.group(1))
    
    # Actually, it's easier to just use re.sub with a limit or specific markers.
    # Let's just use string replacement for the second occurrence.
    
    # The second data1 is at the end of the file.
    # We can just truncate the file at the second "data1" key.
    
    parts = new_content.split('"data1": [')
    # parts[0] is start of file
    # parts[1] is the merged first data1
    # parts[2] is the second data1 we want to remove
    
    if len(parts) >= 3:
        # Reconstruct without the last part
        # But wait, there might be content between parts[1] and parts[2].
        # parts[1] ends with the ], for the first data1.
        # We need to find where the second data1 ends.
        
        last_part = parts[-1]
        # Find the end of the array ], and the closing };
        # The script assumes the second data1 is the LAST key in the object.
        
        final_content = '"data1": ['.join(parts[:-1]).strip()
        if final_content.endswith(','):
            final_content = final_content[:-1]
        final_content += "\n};"
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(final_content)
        print("Successfully merged data1 questions and renumbered them.")
    else:
        print("Could not find both data1 occurrences for splitting.")
else:
    print(f"Match1: {bool(match1)}, Match2: {bool(match2)}")
