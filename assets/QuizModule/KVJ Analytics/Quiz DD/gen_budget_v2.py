import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'Source category': [
        'Total Monthly Budget', 'Total Monthly Budget', 'Total Monthly Budget',
        'Total Monthly Budget', 'Food & Entertainment', 'Food & Entertainment',
        'Entertainment Cost', 'Entertainment Cost'
    ],
    'Spend Category': [
        'Total Monthly Budget', 'Gym Membership', 'Rent',
        'Food & Entertainment', 'Food cost', 'Entertainment Cost',
        'Movie Theater and Play', 'Other'
    ],
    'Amount': [1000, 100, 200, 700, 400, 300, 200, 100]
}
df = pd.DataFrame(data)

# Setup Figure
fig, ax = plt.subplots(figsize=(10, 6))
ax.axis('off')

# Table Formatting
table = ax.table(cellText=df.values, colLabels=df.columns, 
                 loc='center', cellLoc='left', colColours=['#f8fafc']*3)

table.auto_set_font_size(False)
table.set_fontsize(11)
table.scale(1.2, 2.0)

# Header styling
for (row, col), cell in table.get_celld().items():
    if row == 0:
        cell.set_text_props(fontweight='bold', color='#1e3a5f')
        cell.set_facecolor('#e2e8f0')
    else:
        cell.set_facecolor('white')

plt.savefig('budget_flow_v2.png', dpi=150, bbox_inches='tight')
print("Budget flow table v2 generated successfully.")
