import matplotlib.pyplot as plt
import numpy as np

# Data
labels = ['Motorized Bike', 'Golf Cart', 'Utility Vehicle', '2-Wheel Scooter', '3-Wheel Scooter', '4-Wheel Scooter']
num_sold = [600, 600, 425, 850, 1200, 789]
prices = [1200, 7500, 8000, 900, 2999, 3500]
colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']

# 1. Pie Chart
plt.figure(figsize=(8, 6))
plt.pie(num_sold, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)
plt.title('Total Sales Contribution by Vehicle Type', pad=20, fontsize=16)
plt.tight_layout()
plt.savefig('recreational_pie_chart.png', dpi=300)
plt.close()

# 2. Combo Chart (Bar + Line)
fig, ax1 = plt.subplots(figsize=(10, 6))
x = np.arange(len(labels))
ax1.bar(x, num_sold, color='#1f77b4', alpha=0.7, label='Num Sold')
ax1.set_ylabel('Number Sold', color='#1f77b4', fontsize=12)
ax1.tick_params(axis='y', labelcolor='#1f77b4')
ax1.set_xticks(x)
ax1.set_xticklabels(labels, rotation=45, ha='right')

ax2 = ax1.twinx()
ax2.plot(x, prices, color='#ff7f0e', marker='o', linewidth=2, label='Price')
ax2.set_ylabel('Price ($)', color='#ff7f0e', fontsize=12)
ax2.tick_params(axis='y', labelcolor='#ff7f0e')

plt.title('Vehicle Sales and Prices', pad=20, fontsize=16)
fig.tight_layout()
plt.savefig('recreational_combo_chart.png', dpi=300)
plt.close()

# 3. Scatter Plot
plt.figure(figsize=(10, 6))
plt.scatter(num_sold, prices, color='#d62728', s=100, alpha=0.7)
for i, label in enumerate(labels):
    plt.annotate(label, (num_sold[i], prices[i]), xytext=(5, 5), textcoords='offset points')
plt.xlabel('Number Sold', fontsize=12)
plt.ylabel('Price ($)', fontsize=12)
plt.title('Price vs. Quantity Sold', pad=20, fontsize=16)
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()
plt.savefig('recreational_scatter_plot.png', dpi=300)
plt.close()

# 4. Bar Chart
plt.figure(figsize=(10, 6))
width = 0.35
plt.bar(x - width/2, num_sold, width, label='Num Sold', color='#1f77b4')
# Scaling price to fit on the same axis just to mimic the screenshot
scaled_prices = [p/10 for p in prices] 
plt.bar(x + width/2, scaled_prices, width, label='Price (scaled)', color='#ff7f0e')
plt.xticks(x, labels, rotation=45, ha='right')
plt.ylabel('Value', fontsize=12)
plt.title('Sales Comparison', pad=20, fontsize=16)
plt.legend()
plt.tight_layout()
plt.savefig('recreational_bar_chart.png', dpi=300)
plt.close()
