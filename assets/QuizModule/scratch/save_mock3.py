lines = open('quiz_data.js', encoding='utf-8').readlines()
with open('scratch/da_mock3_exact.txt', 'w', encoding='utf-8') as f:
    f.writelines(lines[3852:4235])
