import re

def revert():
    path = r"c:\Users\kj anand\Downloads\Quiz DD\quiz_data.js"
    with open(path, "r", encoding="utf-8") as f:
        content = f.read()

    # Revert da_mock3 to [] using a broad regex for whatever was inserted
    pattern = r'"da_mock3":\s*\[.*?\]'
    new_content = re.sub(pattern, '"da_mock3": []', content, flags=re.DOTALL)
    
    with open(path, "w", encoding="utf-8") as f:
        f.write(new_content)
    print("Successfully reverted da_mock3 to [].")

if __name__ == "__main__":
    revert()
