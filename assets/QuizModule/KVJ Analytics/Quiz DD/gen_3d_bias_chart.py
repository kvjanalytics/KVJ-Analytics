import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Data
labels = ['Group A', 'Group B']
values = [10.0, 9.1]
x = np.arange(len(labels))
y = np.zeros(len(labels))
z = np.zeros(len(labels))
dx = 0.5 * np.ones(len(labels))
dy = 0.5 * np.ones(len(labels))
dz = values

# Truncate Z-axis (equivalent to Y in 2D)
z_min = 8.4
dz_truncated = [v - z_min for v in values]

# Setup Figure
fig = plt.figure(figsize=(10, 8), facecolor='white')
ax = fig.add_subplot(111, projection='3d')

# Plot 3D Bars
ax.bar3d(x - 0.25, y, [z_min]*2, dx, dy, dz_truncated, color='#1e3a5f', alpha=0.9, shade=True)

# Formatting
ax.set_xticks(x)
ax.set_xticklabels(labels, fontweight='bold')
ax.set_zticks(np.arange(8.4, 10.2, 0.2))
ax.set_zlim(8.4, 10.0)

# Hide unnecessary axes for cleaner look
ax.set_yticks([])
ax.xaxis.pane.fill = False
ax.yaxis.pane.fill = False
ax.zaxis.pane.fill = False
ax.grid(True, linestyle='--', alpha=0.3)

plt.title('Performance Comparison (3D View)', fontsize=14, fontweight='bold', color='#1e3a5f', pad=20)
plt.savefig('group_comparison_3d_bias.png', dpi=150, bbox_inches='tight')
print("3D Group Comparison image generated successfully.")
