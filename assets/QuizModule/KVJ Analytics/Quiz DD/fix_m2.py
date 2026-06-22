with open('Data-Module-2.html', 'r', encoding='utf-8') as f:
    text = f.read()

replacements = {
    '2.2.1 Extract Transform and Load (ETL)': '2.1 Extract Transform and Load (ETL)',
    '2.2.2 Common Data File Format': '2.2 Common Data File Format',
    '2.2.3 Data Cleaning': '2.3 Data Cleaning',
    '2.2.4 Data Organizing': '2.4 Data Organizing',
    '2.2.5 Data Aggregation': '2.5 Data Aggregation',
    '2.2.6 Summarizing': '2.6 Summarizing',
    '2.2.7 Pivoting': '2.7 Pivoting'
}

for old, new in replacements.items():
    text = text.replace(old, new)

with open('Data-Module-2.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Fixed Data-Module-2.html")
