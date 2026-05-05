def remove_specific_qs():
    file_path = 'data_quiz_data.js'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    start_marker = '"data3": ['
    end_marker = '    ],'
    
    start_pos = content.find(start_marker)
    end_pos = content.find(end_marker, start_pos)
    
    if start_pos == -1 or end_pos == -1:
        print("data3 section not found")
        return

    data3_content = content[start_pos:end_pos + len(end_marker)]
    
    # Let's split into individual question objects
    # They start with '{' and end with '},' (except the last one)
    import re
    # We use a non-greedy match for the content between braces
    # But wait, objects contain nested braces sometimes. 
    # Let's use a more robust way: find '{' at the start of a line (roughly)
    questions = []
    # Find all objects starting with { and ending with }, or } followed by newline/tab
    # We can use the 'id:' field as a separator
    q_blocks = re.split(r'(\s*{\s*id:\s*\d+)', data3_content)
    
    # The first element is '"data3": [\n'
    header = q_blocks[0]
    q_data = []
    for i in range(1, len(q_blocks), 2):
        block = q_blocks[i] + q_blocks[i+1]
        q_data.append(block)

    # Now we have a list of question blocks.
    # We want to remove the ones that have id: 12, 16, 17 (in the current post-reindex state)
    ids_to_remove = [12, 16, 17]
    new_q_data = []
    for q in q_data:
        match = re.search(r'id:\s*(\d+)', q)
        if match:
            q_id = int(match.group(1))
            if q_id not in ids_to_remove:
                new_q_data.append(q)
    
    # Now re-number the remaining ones
    final_qs = []
    for i, q in enumerate(new_q_data):
        new_id = i + 1
        # Replace the id: X, with id: new_id,
        new_q = re.sub(r'id:\s*\d+,', f'id: {new_id},', q)
        # Ensure the trailing comma is correct (last one shouldn't have it followed by another object)
        # Actually, the blocks already have trailing commas or brackets
        final_qs.append(new_q)

    # Reconstruct the section
    # We need to handle the last trailing comma
    # Usually the array looks like [ { ... }, { ... } ]
    # My split might have left the last ']' in the last block
    last_block = final_qs[-1]
    if '],' in last_block:
        # It's already there
        pass
    else:
        # We might need to fix the comma at the end of the second to last
        pass

    # simpler: join with nothing, but ensure the comma before the last ] is removed?
    # No, the engine usually handles it if it's JS.
    
    # Let's just join them and fix the end
    reconstructed = header + "".join(final_qs)
    # Ensure it ends with '    ],'
    if not reconstructed.strip().endswith('],'):
        reconstructed = reconstructed.rstrip().rstrip(',') + '\n    ],'

    new_full_content = content[:start_pos] + reconstructed + content[end_pos + len(end_marker):]
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_full_content)
    print("Successfully removed questions 12, 16, and 17, and re-numbered the rest.")

remove_specific_qs()
