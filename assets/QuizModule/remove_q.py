def remove_first_q_m3():
    file_path = 'data_quiz_data.js'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the data3 section
    start_marker = '"data3": ['
    end_marker = '    ],'
    
    start_pos = content.find(start_marker)
    if start_pos == -1:
        print("data3 not found")
        return

    # Find the end of data3 array
    # We look for the '],' after the data3 start
    end_pos = content.find(end_marker, start_pos)
    
    data3_content = content[start_pos:end_pos + len(end_marker)]
    
    # We want to remove the first object in the array
    # The array starts after '"data3": ['
    # The first object starts with '{' and ends with '},'
    
    # Let's use a more robust way to find the first object
    obj_start = data3_content.find('{')
    obj_end = data3_content.find('},', obj_start)
    if obj_end == -1:
        # Maybe it's the only object?
        obj_end = data3_content.find('}', obj_start)
    
    if obj_start != -1 and obj_end != -1:
        # Remove the object and the trailing comma if it exists
        removed_q = data3_content[obj_start:obj_end + 2] # +2 for '},'
        new_data3_content = data3_content[:obj_start] + data3_content[obj_end + 2:]
        
        # Now re-number the IDs in new_data3_content
        import re
        def renumber(match):
            old_id = int(match.group(1))
            return f"id: {old_id - 1},"
        
        # Only re-number inside the data3 array
        # Match 'id: X,'
        new_data3_content = re.sub(r'id:\s*(\d+),', renumber, new_data3_content)
        
        # Replace the old section with the new one
        new_full_content = content[:start_pos] + new_data3_content + content[end_pos + len(end_marker):]
        
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_full_content)
        print("Successfully removed first question and re-numbered the rest in data3")
    else:
        print("First question object not found")

remove_first_q_m3()
