import matplotlib.pyplot as plt
import numpy as np

colors = ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b']
main_color = '#1f77b4'

# 1. Column Chart (Option 1)
plt.figure(figsize=(6, 4))
x = np.arange(1, 8)
y = [3, 5, 6, 8, 10, 6, 4]
plt.bar(x, y, width=0.4, color=main_color)
plt.title("Column chart", fontsize=14, color='#475569', pad=15)
plt.grid(axis='y', linestyle='-', alpha=0.3)
plt.xticks([])
plt.yticks([])
for spine in plt.gca().spines.values():
    spine.set_color('#e2e8f0')
plt.tight_layout()
plt.savefig("dist_column_chart.png", dpi=300, bbox_inches='tight')
plt.close()

# 2. Line Chart (Option 2)
plt.figure(figsize=(6, 4))
y2 = [6, 4, 4.5, 2, 10, 7, 2]
plt.plot(x, y2, marker='o', markersize=4, color=main_color, linewidth=1.5)
plt.title("Line chart", fontsize=14, color='#475569', pad=15)
plt.grid(True, linestyle='-', alpha=0.3)
plt.xticks([])
plt.yticks([])
for spine in plt.gca().spines.values():
    spine.set_color('#e2e8f0')
plt.tight_layout()
plt.savefig("dist_line_chart.png", dpi=300, bbox_inches='tight')
plt.close()

# 3. Histogram (Option 3)
plt.figure(figsize=(6, 4))
# simple representation of a histogram with contiguous bins
plt.bar([1], [8], width=1, color=main_color, edgecolor='white', linewidth=0.5, align='edge')
plt.bar([2], [2], width=2, color=main_color, edgecolor='white', linewidth=0.5, align='edge')
plt.title("Histogram", fontsize=14, color='#475569', pad=15)
plt.xticks([])
plt.yticks([])
for spine in plt.gca().spines.values():
    spine.set_color('#e2e8f0')
plt.tight_layout()
plt.savefig("dist_histogram.png", dpi=300, bbox_inches='tight')
plt.close()

# 4. Bar Chart (Option 4 - Horizontal)
plt.figure(figsize=(6, 4))
y_pos = np.arange(1, 10)
widths = [5, 8, 4, 8, 3, 2, 4, 8, 3]
plt.barh(y_pos, widths, height=0.4, color=main_color)
plt.title("Bar chart", fontsize=14, color='#475569', pad=15)
plt.grid(axis='x', linestyle='-', alpha=0.3)
plt.xticks([])
plt.yticks([])
for spine in plt.gca().spines.values():
    spine.set_color('#e2e8f0')
plt.tight_layout()
plt.savefig("dist_bar_chart.png", dpi=300, bbox_inches='tight')
plt.close()
