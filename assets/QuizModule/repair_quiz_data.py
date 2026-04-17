def repair():
    path = r"c:\Users\kj anand\Downloads\Quiz DD\quiz_data.js"
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    # Find the line where da_mock2 ends
    da_mock2_end = -1
    for i, line in enumerate(lines):
        if '"da_mock2": [' in line:
            # Found start. Now find end.
            for j in range(i, len(lines)):
                if '    ],' in lines[j] and j > i:
                    da_mock2_end = j
                    break
            break
    
    if da_mock2_end != -1:
        print(f"Repairing from line {da_mock2_end + 1} onwards...")
        # Keep everything up to da_mock2_end
        new_lines = lines[:da_mock2_end + 1]
        # Add a clean da_mock3 and close the object
        new_lines.append('    "da_mock3": []\n')
        new_lines.append('};\n')
        
        with open(path, "w", encoding="utf-8") as f:
            f.writelines(new_lines)
        print("Successfully repaired quiz_data.js.")
    else:
        print("Could not find end of da_mock2.")

if __name__ == "__main__":
    repair()
