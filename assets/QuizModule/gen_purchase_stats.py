import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Data
categories = ['Mean', 'Median', 'Mode', 'Std Dev']
instore_vals = [188, 190, 199, 66]
online_vals = [228, 215, 199, 122]

# Setup Figure
fig, ax = plt.subplots(figsize=(12, 7), facecolor='white')

y = np.arange(len(categories))
height = 0.35

# Plot horizontal bars
ax.barh(y + height/2, online_vals, height, label='Online', color='#1e3a5f')
ax.barh(y - height/2, instore_vals, height, label='Instore', color='#f97316')

# Table Data for embedding below the chart
table_data = [
    ['Instore', '$188', '$190', '$199', '$66'],
    ['Online', '$228', '$215', '$199', '$122']
]
table_cols = ['', 'Mean', 'Median', 'Mode', 'Std Dev']

# Formatting axes
ax.set_yticks(y)
ax.set_yticklabels(categories, fontweight='bold', color='#1e3a5f')
ax.set_xlabel('Amount ($)', fontweight='bold', color='#1e3a5f')
ax.set_xlim(0, 250)
ax.grid(axis='x', linestyle='--', alpha=0.3)
ax.set_title('Online & Instore Purchase Statistics', fontsize=16, fontweight='bold', color='#1e3a5f', pad=30)
ax.legend(loc='lower right', frameon=True, borderpad=1)

# Add Table below plot
the_table = plt.table(cellText=table_data, colLabels=table_cols, 
                      loc='bottom', cellLoc='center', bbox=[0, -0.4, 1, 0.25])
the_table.auto_set_font_size(False)
the_table.set_fontsize(10)

plt.tight_layout()
plt.subplots_adjust(bottom=0.3)
plt.savefig('purchase_stats_comparison.png', dpi=150, bbox_inches='tight')
print("Purchase statistics comparison chart generated successfully.")
