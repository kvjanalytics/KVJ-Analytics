
# Read both files
with open('quiz_data.js', 'r', encoding='utf-8') as f:
    qd = f.read()

with open('data_quiz_data.js', 'r', encoding='utf-8') as f:
    dqd = f.read()

# Extract da_mock1, da_mock2, da_mock3 from quiz_data.js
m1_start = qd.index('"da_mock1"')
m2_start = qd.index('"da_mock2"')
m3_start = qd.index('"da_mock3"')

# Extract each section  
m1_section = qd[m1_start:m2_start].rstrip().rstrip(',')
m2_section = qd[m2_start:m3_start].rstrip().rstrip(',')

# m3 goes to end of file, strip the closing }; of the var declaration
m3_section = qd[m3_start:].rstrip()
if m3_section.endswith('};'):
    m3_section = m3_section[:-2].rstrip()
elif m3_section.endswith('}'):
    m3_section = m3_section[:-1].rstrip()

print("m3 ends with:", repr(m3_section[-60:]))
print("dqd ends with:", repr(dqd[-100:]))

# Find the closing }; in data_quiz_data.js and insert before it
# The file ends with:  ]\n};
# We need to add the mock sections before the final };
insert_pos = dqd.rfind('};')
if insert_pos == -1:
    insert_pos = dqd.rfind('}')

print(f"Insert position: {insert_pos}")
print("Content around insert:", repr(dqd[insert_pos-50:insert_pos+10]))

# Build the new content
new_content = (
    dqd[:insert_pos]
    + ',\n    '
    + m1_section
    + ',\n    '
    + m2_section
    + ',\n    '
    + m3_section
    + '\n};'
)

with open('data_quiz_data.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print("Done! data_quiz_data.js updated with all 3 mocks.")

# Verify
with open('data_quiz_data.js', 'r', encoding='utf-8') as f:
    content = f.read()

for key in ['da_mock1', 'da_mock2', 'da_mock3']:
    if key in content:
        print(f"  {key}: FOUND")
    else:
        print(f"  {key}: MISSING!")
