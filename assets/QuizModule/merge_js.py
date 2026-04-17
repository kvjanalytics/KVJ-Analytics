import re

with open('quiz_data_test.js', 'r', encoding='utf-8') as f:
    old_data = f.read()

with open('quiz_data.js', 'r', encoding='utf-8') as f:
    new_data = f.read()

# We want to extract "1", "2", "3", "4", "5", "6", and "mock1" from old_data.
# The structure is:
# var quizData = {
#     "1": [ ... ],
#     "2": [ ... ],
#     ...
#     "mock1": [ ... ]
# }

# Find the content between 'var quizData = {' and the end '}'
old_inner = re.search(r'var quizData = \{(.*)\}', old_data, re.DOTALL)
new_inner = re.search(r'var quizData = \{(.*)\}', new_data, re.DOTALL)

if old_inner and new_inner:
    # We will rename old_inner's "mock1" to "py_mock1" just in case.
    # Actually, let's just grab "1" through "6".
    # We can split old_inner by top-level keys if needed, but it's simpler to just grab 
    # everything up to the end of "6": [ ... ]
    # Let's find `"mock1": [` in old_data
    mock1_index = old_inner.group(1).find('"mock1": [')
    
    if mock1_index != -1:
        python_modules = old_inner.group(1)[:mock1_index]
        python_mock = old_inner.group(1)[mock1_index:]
        # Rename python mock1 to py_mock1
        python_mock = python_mock.replace('"mock1": [', '"py_mock1": [', 1)
        
        merged_inner = python_modules + python_mock + ",\n" + new_inner.group(1)
    else:
        merged_inner = old_inner.group(1) + ",\n" + new_inner.group(1)

    merged_data = 'var quizData = {' + merged_inner + '}'
    
    with open('quiz_data.js', 'w', encoding='utf-8') as f:
        f.write(merged_data)
        
    print("Merge successful")
else:
    print("Regex failed to match")
