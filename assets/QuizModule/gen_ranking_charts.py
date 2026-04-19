import matplotlib.pyplot as plt

# Data for ranking
labels = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
values = [95, 80, 65, 40, 25]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6), facecolor='white')

# 1. Horizontal Bar Chart (Ranking)
ax1.barh(labels[::-1], values[::-1], color='#1e3a5f')
ax1.set_title('Bar Chart (Horizontal Ranking)', fontweight='bold', pad=15)
ax1.grid(axis='x', linestyle='--', alpha=0.3)

# 2. Vertical Column Chart (Ranking)
ax2.bar(labels, values, color='#38bdf8')
ax2.set_title('Column Chart (Vertical Ranking)', fontweight='bold', pad=15)
ax2.grid(axis='y', linestyle='--', alpha=0.3)

plt.tight_layout()
plt.savefig('ranking_charts_professional.png', dpi=150)
print("Ranking charts image generated successfully.")
