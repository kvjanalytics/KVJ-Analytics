import matplotlib.pyplot as plt
import numpy as np

# Data
groups = ['Group A', 'Group B']
values = [9.9, 8.9]

plt.rcParams['font.sans-serif'] = 'Arial'

fig, ax = plt.subplots(figsize=(8, 5))
# Group A is dark blue, Group B is orange. Both have light orange/yellow borders.
# Bar widths are about 0.3
bar_width = 0.3
bars = plt.bar(groups, values, width=bar_width, 
               color=['#1f6f8b', '#e87a31'], 
               edgecolor='#ffb833', linewidth=1.5)

# Setting y-axis limits to 8.4 to 10 to recreate the misleading effect
plt.ylim(8.4, 10.05)
plt.yticks(np.arange(8.4, 10.1, 0.2))

# Hide top and right spines
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_color('#cccccc')
ax.spines['bottom'].set_color('#cccccc')

ax.tick_params(axis='both', colors='#555555', length=0, pad=8)
plt.xticks(fontsize=11)
plt.yticks(fontsize=11)

plt.tight_layout()
plt.savefig('q19_misleading_chart.png', dpi=300, bbox_inches='tight')
plt.close()
