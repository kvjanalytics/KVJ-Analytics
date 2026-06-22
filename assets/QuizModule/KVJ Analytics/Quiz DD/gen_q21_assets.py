import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Data
data = {
    'Year': ['2025', '2024', '2023', '2022', '2021', 'Break-Even Point'],
    'Quarter 1': [482502, 421809, 395931, 381844, 404197, 357762],
    'Quarter 2': [384947, 435556, 341514, 333025, 396341, 321218],
    'Quarter 3': [454211, 441299, 472201, 391607, 409349, 349781],
    'Quarter 4': [423547, 509480, 388033, 340080, 435237, 349819],
    'Total': [1745207, 1808144, 1597679, 1446556, 1645124, 1378580]
}
df = pd.DataFrame(data)

# 1. Generate Table Asset
fig_table, ax_table = plt.subplots(figsize=(12, 4), facecolor='white')
ax_table.axis('off')
vals = df.values.tolist()
# format large numbers with commas
for row in vals:
    for i in range(1, 6):
        row[i] = f"{row[i]:,}"

table = ax_table.table(cellText=vals, colLabels=df.columns, loc='center', cellLoc='center')
table.auto_set_font_size(False)
table.set_fontsize(11)
table.scale(1.2, 2.5)

# Style header
for (row, col), cell in table.get_celld().items():
    if row == 0:
        cell.set_facecolor('#e2e8f0')
        cell.set_text_props(fontweight='bold', color='#1e3a5f')
    else:
        cell.set_facecolor('white')

plt.savefig('quarterly_sales_table.png', dpi=150, bbox_inches='tight')
plt.close()

# 2. Options
# Opt 1: Grouped Bar + Line
years_only = df['Year'][:-1].tolist()
quarters = ['Quarter 1', 'Quarter 2', 'Quarter 3', 'Quarter 4']
bep_vals = df.iloc[-1, 1:5].values

plt.figure(figsize=(8, 6))
x = np.arange(len(quarters))
width = 0.15
for i, yr in enumerate(years_only):
    plt.bar(x + (i-2)*width, df.iloc[i, 1:5].values, width, label=yr)
plt.plot(x, bep_vals, color='red', marker='o', label='Break-Even', linewidth=2)
plt.xticks(x, quarters)
plt.title('Option 1: Grouped Bar with BEP Line', fontweight='bold')
plt.legend(fontsize=8, loc='upper right')
plt.tight_layout()
plt.savefig('v3_q21_opt1.png', dpi=100)
plt.close()

# Opt 2: Pie (Misleading)
plt.figure(figsize=(8, 6))
plt.pie(df['Total'][:-1], labels=years_only, autopct='%1.1f%%', shadow=True)
plt.title('Option 2: 3D-Style Pie Chart', fontweight='bold')
plt.tight_layout()
plt.savefig('v3_q21_opt2.png', dpi=100)
plt.close()

# Opt 3: Stacked Bar
plt.figure(figsize=(8, 6))
bottoms = np.zeros(len(df['Year']))
for q in quarters:
    plt.bar(df['Year'], df[q], bottom=bottoms, label=q)
    bottoms += df[q].values
plt.title('Option 3: Stacked Bar Chart', fontweight='bold')
plt.legend(fontsize=8)
plt.tight_layout()
plt.savefig('v3_q21_opt3.png', dpi=100)
plt.close()

# Opt 4: Grouped Bar with DISTORTED TOTAL
plt.figure(figsize=(8, 6))
plt.bar(df['Year'], df['Total'], color='purple')
plt.title('Option 4: Scale Distorted (Total Bars Only)', fontweight='bold')
plt.tight_layout()
plt.savefig('v3_q21_opt4.png', dpi=100)
plt.close()

print("Question 21 assets generated successfully.")
