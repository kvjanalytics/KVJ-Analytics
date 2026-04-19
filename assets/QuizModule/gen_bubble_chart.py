import matplotlib.pyplot as plt
import numpy as np

# Data (3 values per point: X, Y, Size)
x = [10, 20, 30, 40, 50, 60, 70, 80]
y = [20, 30, 15, 45, 33, 50, 25, 40]
sizes = [200, 600, 300, 1200, 800, 500, 1500, 900] # The third value

# Setup Figure
plt.figure(figsize=(10, 6), facecolor='white')
scatter = plt.scatter(x, y, s=sizes, color='#1e3a5f', alpha=0.6, edgecolors='white', linewidth=1.5)

# Formatting
plt.title('Multi-Variable Analysis (X, Y, and Size)', fontsize=14, fontweight='bold', color='#1e3a5f', pad=20)
plt.xlabel('Metric X', fontweight='bold', color='#1e3a5f')
plt.ylabel('Metric Y', fontweight='bold', color='#1e3a5f')
plt.grid(True, linestyle='--', alpha=0.3)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Add legend for sizes
handles, labels = scatter.legend_elements(prop="sizes", alpha=0.6)
legend2 = plt.legend(handles, labels, loc="upper left", title="Value 3 (Size)")
plt.gca().add_artist(legend2)

plt.tight_layout()
plt.savefig('three_value_bubble_chart.png', dpi=150)
print("Bubble chart image generated successfully.")
