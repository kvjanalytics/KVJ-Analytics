import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'Year': ['2016', '2017', '2018', '2019', '2020', '2021', '2022', '2023', '2024', '2025'],
    'Price': [150000, 175000, 200000, 225000, 250000, 275000, 300000, 325000, 350000, 425000]
}
df = pd.DataFrame(data)

# Setup Figure
fig = plt.figure(figsize=(12, 6), facecolor='white')

# 1. Bar Chart (Left)
ax_chart = fig.add_axes([0.05, 0.15, 0.55, 0.7])
bars = ax_chart.bar(df['Year'], df['Price'], color='#1e3a5f', width=0.6)
ax_chart.set_title('Regional Housing Prices Trend', fontsize=14, fontweight='bold', color='#1e3a5f', pad=20)
ax_chart.set_ylim(0, 450000)
ax_chart.set_yticks(range(0, 500000, 50000))
ax_chart.get_yaxis().set_major_formatter(plt.FuncFormatter(lambda x, p: format(int(x), ',')))
ax_chart.grid(axis='y', linestyle='--', alpha=0.3)
ax_chart.spines['top'].set_visible(False)
ax_chart.spines['right'].set_visible(False)

# 2. Table (Right)
ax_table = fig.add_axes([0.65, 0.1, 0.3, 0.8])
ax_table.axis('off')

# Table Formatting
table_data = df.copy()
table_data['Price'] = table_data['Price'].apply(lambda x: f'${x:,.00f}')
table = ax_table.table(cellText=table_data.values, colLabels=table_data.columns, 
                       loc='center', cellLoc='center', colColours=['#f8fafc']*2)

table.auto_set_font_size(False)
table.set_fontsize(11)
table.scale(1.2, 1.8)

# Header styling
for (row, col), cell in table.get_celld().items():
    if row == 0:
        cell.set_text_props(fontweight='bold', color='#1e3a5f')
        cell.set_facecolor('#e2e8f0')

plt.savefig('housing_prices_v2_professional.png', dpi=150, bbox_inches='tight')
print("Refined Housing Prices image generated successfully.")
