import re
import json

def get_questions():
    with open('quiz_data.js', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract mock3 array
    mock3_match = re.search(r'"mock3"\s*:\s*\[(.*?)\]\s*,\s*"[^"]+"\s*:', content, re.DOTALL)
    if not mock3_match:
        # try end of object
        mock3_match = re.search(r'"mock3"\s*:\s*\[(.*?)\]\s*}', content, re.DOTALL)
        
    if not mock3_match:
        print("Could not find mock3")
        return
        
    mock3_content = mock3_match.group(1)
    
    # Very crude splitting by { "id": to get rough question blocks for display
    # It's better to just write a script that loads it as JS
    pass

if __name__ == "__main__":
    pass
