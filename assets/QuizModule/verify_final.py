import json
import re

def verify():
    with open("quiz_data.js", "r", encoding="utf-8") as f:
        content = f.read()

    # Find the start and end of quizData object
    match = re.search(r'const quizData = (\{.*\});', content, re.DOTALL)
    if not match:
        print("Could not find quizData object.")
        return

    # This is a bit risky due to JS vs JSON differences but let's try a simpler regex for counts
    def get_count(key):
        # Match "key": [ ... ]
        pattern = r'"' + key + r'":\s*\[(.*?)\]'
        m = re.search(pattern, content, re.DOTALL)
        if m:
            # Approximate count by searching for "id":
            return len(re.findall(r'"id":', m.group(1)))
        return -1

    print(f"mock1 count: {get_count('mock1')}")
    print(f"mock2 count: {get_count('mock2')}")
    print(f"mock3 count: {get_count('mock3')}")
    print(f"da_mock1 count: {get_count('da_mock1')}")
    print(f"da_mock2 count: {get_count('da_mock2')}")
    print(f"da_mock3 count: {get_count('da_mock3')}")

    # Check module_quiz.html for the fix
    with open("module_quiz.html", "r", encoding="utf-8") as f:
        html = f.read()
    
    if 'modId = "mock" + mockId;' in html and 'else if (quizData[mockId]) {' in html:
        print("Routing fix found in module_quiz.html")
    else:
        print("Routing fix NOT found in module_quiz.html")

if __name__ == "__main__":
    verify()
