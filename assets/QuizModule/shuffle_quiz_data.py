import json
import random
import re

p = r"c:\Users\kj anand\Downloads\Quiz DD (2) 7 (2)\Quiz DD (2) 6\Quiz DD (13) 6\Quiz DD\quiz_data.js"

with open(p, 'r', encoding='utf-8') as f:
    content = f.read()

# quiz_data.js uses var quizData = { ... };
match = re.search(r'var quizData = (\{[\s\S]*\});', content)
if not match:
    match = re.search(r'const quizData = (\{[\s\S]*\});', content)

if not match:
    print("Could not find quizData variable.")
    exit(1)

json_text = match.group(1)

# Clean trailing commas
temp_json = re.sub(r',(\s*[\]\}])', r'\1', json_text)

try:
    data = json.loads(temp_json)
except json.JSONDecodeError as e:
    print(f"JSON parsing failed: {e}")
    exit(1)


def shuffle_mcq_options(q):
    options = q.get('options', [])
    correct_answer_idx = q.get('a')
    if not options or not isinstance(correct_answer_idx, int):
        return q
    if correct_answer_idx >= len(options):
        return q
    correct_text = options[correct_answer_idx]
    indices = list(range(len(options)))
    random.shuffle(indices)
    new_options = [options[i] for i in indices]
    new_a = new_options.index(correct_text)
    q['options'] = new_options
    q['a'] = new_a
    return q


def shuffle_tf_options(q):
    options = q.get('options', [])
    answers = q.get('a', [])
    if not isinstance(answers, list) or len(options) != len(answers):
        return q
    combined = list(zip(options, answers))
    random.shuffle(combined)
    new_options, new_answers = zip(*combined)
    q['options'] = list(new_options)
    q['a'] = list(new_answers)
    return q


def process_question(q):
    q_type = q.get('type', '')
    if q_type == 'MCQ':
        q = shuffle_mcq_options(q)
    elif q_type == 'TF':
        q = shuffle_tf_options(q)
    return q


keys_to_shuffle = ['data1', 'data2', 'data3', 'data4', 'data5', 'da_mock1', 'da_mock2']

for key in keys_to_shuffle:
    if key in data:
        questions = data[key]
        random.shuffle(questions)
        for i, q in enumerate(questions):
            q = process_question(q)
            q['id'] = i + 1
            questions[i] = q
        print(f"{key}: shuffled {len(questions)} questions.")
    else:
        print(f"{key}: NOT FOUND in data.")

new_json_text = json.dumps(data, indent=4, ensure_ascii=False)
new_content = content[:match.start(1)] + new_json_text + content[match.end(1):]

with open(p, 'w', encoding='utf-8') as f:
    f.write(new_content)

print("\nDone. Shuffled and saved to quiz_data.js")
