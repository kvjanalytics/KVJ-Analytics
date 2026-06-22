import re, json

BASE = r"C:\Users\kj anand\Downloads\Quiz DD (13) 6\Quiz DD"

# Read target file
with open(BASE + r"\data_quiz_data_utf8.js", 'r', encoding='utf-8') as f:
    js_content = f.read()

# Extract the JSON variable
start_idx = js_content.find('{')
json_content = js_content[start_idx:js_content.rfind(';')]

data = json.loads(json_content)
da_mock3 = data['da_mock3']
data4 = data.get('data4', [])

# Helper to find question by ID in a specific list
def find_q(qlist, qid):
    for q in qlist:
        if q.get('id') == qid:
            import copy
            return copy.deepcopy(q)
    return None

# We will build a new da_mock3 list.
new_da_mock3 = []

# Questions 1-22 remain mostly unchanged, except we must ensure Q21 and Q22 match expectation
for q in da_mock3:
    if q['id'] < 23:
        new_da_mock3.append(q)

# Constructing Q23 - Q33 based on user specifications
# Q23: Quarterly Sales from data4 id 1
q23 = find_q(data4, 1)
q23['id'] = 23
q23['img'] = "quarterly_sales_table.png"
q23['optionImages'] = ["v3_q21_opt1.png", "v3_q21_opt2.png", "v3_q21_opt3.png", "v3_q21_opt4.png"]
q23['a'] = 0
new_da_mock3.append(q23)

# Q24: ETL Transformation from da_mock3 id 11
q24 = find_q(da_mock3, 11)
q24['id'] = 24
q24['options'][1] = "Converting data types or structures" # update the correct answer option
q24['a'] = 1
new_da_mock3.append(q24)

# Q25: Chart Comparison from da_mock3 id 10
q25 = find_q(da_mock3, 10)
q25['id'] = 25
q25['a'] = 1 # Wait, user said: "Verified the correct answer key (a: 0)" and "identify Bubble Charts for comparing three values". Let's check: options are ["Bar Chart", "Bubble Chart", "Area Chart", "Waterfall Chart"]. If a:0, then option 0 must be Bubble Chart!
q25['options'] = ["Bubble Chart", "Bar Chart", "Area Chart", "Waterfall Chart"]
q25['a'] = 0
new_da_mock3.append(q25)

# Q26: Hypothesis Testing from da_mock3 id 22
q26 = find_q(da_mock3, 22)
q26['id'] = 26
# user said: "identify a p-value (0.001) that causes rejection of the null hypothesis at 1%. Verified correct answer key (a: 0)."
q26['options'] = ["0.001", "0.011", "0.008", "0.10"] # 0.001 is option 0
q26['a'] = 0
new_da_mock3.append(q26)

# Q27: Sales Lead Comparison from data4 id 10
q27 = find_q(data4, 10)
q27['id'] = 27
q27['a'] = 1
# Include the "conclusin" typo as seen in the source image
q27['q'] = q27['q'].replace("conclusion indicates", "conclusin indicates").replace("conclusion.", "conclusin.")
new_da_mock3.append(q27)

# Q28: Ice Cream Preference from data4 id 19
q28 = find_q(data4, 19)
q28['id'] = 28
q28['img'] = "q28_ice_cream.png"
q28['a'] = 2
q28['options'][2] = "The most students chose strawberry" # "pointing to: 'The most students chose strawberry' (40%). Verified correct answer key (a: 2)"
new_da_mock3.append(q28)

# Q29: Exporting CSV (Text Qualifier) from da_mock3 id 19
q29 = find_q(da_mock3, 19)
q29['id'] = 29
q29['a'] = 3
q29['options'] = ["To make the file look more professional", "To encrypt the information", "To reduce the file size", "To allow data containing actual commas to stay in one column"] 
new_da_mock3.append(q29)

# Q30: Flight Delay Forecasting from da_mock3 id 29
q30 = find_q(da_mock3, 29)
q30['id'] = 30
# "Verified the correct answer key (a: [0, 1, 4]) which selects the three valid approaches."
new_da_mock3.append(q30)

# Q31: Data Categorization Matching (MTF) from da_mock3 id 31
q31 = find_q(da_mock3, 31)
q31['id'] = 31
new_da_mock3.append(q31)

# Q32: Hypothesis Testing (t-test) from da_mock3 id 32
q32 = find_q(da_mock3, 32)
q32['id'] = 32
new_da_mock3.append(q32)

# Q33: Healthcare Data Security (MTF) from da_mock3 id 33
q33 = find_q(da_mock3, 33)
q33['id'] = 33
# "Fix: Resolved a minor syntax error (double commas)"
for k, v in q33['a'].items():
    q33['a'][k] = v.replace(",,", ",")
new_da_mock3.append(q33)

# Add remaining questions 34 to 44
for q in da_mock3:
    if q['id'] >= 34:
        new_da_mock3.append(q)

# Sort IDs to be safe
new_da_mock3 = sorted(new_da_mock3, key=lambda x: x['id'])

data['da_mock3'] = new_da_mock3

# Serialize and save
new_json = json.dumps(data, indent=4, ensure_ascii=False)
final_js = "const quizData = " + new_json + ";"

with open(BASE + r"\data_quiz_data.js", "wb") as f:
    f.write(final_js.encode('utf-16le'))

with open(BASE + r"\data_quiz_data_utf8.js", "w", encoding='utf-8') as f:
    f.write(final_js)

print("Successfully written updated Q23-Q33 into data_quiz_data.js in utf-16le")
