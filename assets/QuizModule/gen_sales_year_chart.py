import matplotlib.pyplot as plt

# Data
years = ['2019', '2020', '2021', '2022']
sales = [8, 6, 17, 3]

# Setup Figure
plt.figure(figsize=(10, 6), facecolor='white')
plt.bar(years, sales, color='#1e3a5f', width=0.3)

# Formatting
plt.title('Total Sales by Year', fontsize=14, fontweight='bold', color='#1e3a5f', pad=20)
plt.ylabel('Sales ($)', fontweight='bold', color='#1e3a5f')
plt.ylim(0, 18)
plt.yticks(range(0, 20, 2))
plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f'${int(x)}'))
plt.grid(axis='y', linestyle='--', alpha=0.3)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

plt.tight_layout()
plt.savefig('sales_by_year_column.png', dpi=150)
print("Sales by year column chart generated successfully.")
