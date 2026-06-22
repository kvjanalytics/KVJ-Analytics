def remove_dead_js():
    file_path = 'Data-Module-3.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the start and end of the anomaly chart JS
    start_marker = '// Initialize Anomaly Scatter Chart'
    end_marker = '// Initialize Sales Trend Chart'
    
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)
    
    if start_idx != -1 and end_idx != -1:
        new_content = content[:start_idx] + content[end_idx:]
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Successfully removed dead Anomaly Chart JS")
    else:
        print("Dead JS markers not found")

remove_dead_js()
