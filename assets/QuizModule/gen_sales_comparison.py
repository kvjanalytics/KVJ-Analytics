import matplotlib.pyplot as plt

# Data
labels = ['Sales person 1', 'Sales person 2']
values = [23000, 5000]

# Setup Figure
plt.figure(figsize=(10, 6), facecolor='white')
bars = plt.bar(labels, values, color='#1e3a5f', width=0.4)

# Formatting
plt.title('Sales Volume Comparison', fontsize=14, fontweight='bold', color='#1e3a5f', pad=20)
plt.ylabel('Units sold ($)', fontweight='bold', color='#1e3a5f')
plt.ylim(0, 25000)
plt.yticks(range(0, 30000, 5000))
plt.grid(axis='y', linestyle='--', alpha=0.3)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Add value labels
for bar in bars:
    height = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2., height + 500,
             f'{int(height):,}', ha='center', va='bottom', fontweight='bold', color='#1e3a5f')

plt.tight_layout()
plt.savefig('sales_lead_comparison.png', dpi=150)
print("Sales comparison image generated successfully.")
