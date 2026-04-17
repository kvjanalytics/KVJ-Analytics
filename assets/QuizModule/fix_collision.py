import re

with open('quiz_data.js', 'r', encoding='utf-8') as f:
    text = f.read()

# I want to rename the FIRST occurrence of "py_mock1": [ back to "mock1": [
# And the LAST occurrence of "mock1": [ to "da_mock1": [

text = text.replace('"py_mock1": [', '"mock1": [', 1)

# Now, to rename the last occurrence of "mock1": [, which is Data Analytics Mock 1.
# I can rfind '"mock1": ['
last_mock_idx = text.rfind('"mock1": [')

if last_mock_idx != -1:
    text = text[:last_mock_idx] + '"da_mock1": [' + text[last_mock_idx + len('"mock1": ['):]
    with open('quiz_data.js', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Renamed keys successfully.")
else:
    print("Could not find mock1.")

