import re

with open('Data-Module-3.html', 'r', encoding='utf-8') as f:
    text = f.read()

ids_to_check = ['s1-analysis', 's3-1-types', 's3-2-descriptive', 's3-3-diagnostic', 's3-4-predictive', 's3-5-prescriptive', 's3-6-exploratory', 's3-11-patterns', 's3-13-outlier', 's3-15-hypothesis', 's3-19-lab-regression']
for i in ids_to_check:
    if f'id="{i}"' not in text:
        print(f'Missing: {i}')
print('Done checking')
