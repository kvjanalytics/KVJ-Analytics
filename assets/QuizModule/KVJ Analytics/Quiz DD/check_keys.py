import re

with open('quiz_data_test.js', 'r', encoding='utf-8') as f:
    text = f.read()
keys = re.findall(r'    \"([a-zA-Z0-9_]+)\": \[', text)

with open('keys_out.txt', 'w', encoding='utf-8') as f:
    f.write("Test file keys: " + str(keys) + "\n")

    try:
        with open('quiz_data.js', 'r', encoding='utf-8') as f2:
            text2 = f2.read()
        keys2 = re.findall(r'    \"([a-zA-Z0-9_]+)\": \[', text2)
        f.write("Current file keys: " + str(keys2) + "\n")
    except Exception as e:
        f.write("Error: " + str(e))
