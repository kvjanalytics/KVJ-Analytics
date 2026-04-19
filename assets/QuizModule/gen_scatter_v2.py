import matplotlib.pyplot as plt

# Data
x = [10, 20, 30, 40, 50, 60, 70, 80]
y = [20, 10, 32, 30, 38, 19, 44, 55]

# Setup Figure
plt.figure(figsize=(10, 6), facecolor='white')
plt.scatter(x, y, color='#1e3a5f', s=100)

# Formatting
plt.xlabel('Variable X', fontweight='bold', color='#1e3a5f')
plt.ylabel('Variable Y', fontweight='bold', color='#1e3a5f')
plt.xlim(0, 90)
plt.ylim(0, 60)
plt.grid(True, linestyle='--', alpha=0.3)
plt.title('Relationship Analysis: X vs Y', fontsize=14, fontweight='bold', color='#1e3a5f', pad=20)

plt.tight_layout()
plt.savefig('scatter_correlation_v2.png', dpi=150)
print("Scatter correlation chart generated successfully.")
