import matplotlib.pyplot as plt
import numpy as np

# Styles
plt.style.use('seaborn-v0_8-muted')
color_kvj = '#1e3a5f'

def save_opt1():
    # Column chart
    x = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    y = [10, 20, 30, 45, 60, 40, 15]
    plt.figure(figsize=(8, 6))
    plt.bar(x, y, color=color_kvj, width=0.5)
    plt.title('Column chart', fontweight='bold', pad=20)
    plt.grid(axis='y', linestyle='--', alpha=0.3)
    plt.tight_layout()
    plt.savefig('v3_q13_opt1.png', dpi=100)
    plt.close()

def save_opt2():
    # Line chart
    x = range(7)
    y = [20, 15, 18, 12, 35, 25, 10]
    plt.figure(figsize=(8, 6))
    plt.plot(x, y, marker='o', color=color_kvj, linewidth=2)
    plt.title('Line chart', fontweight='bold', pad=20)
    plt.grid(True, linestyle='--', alpha=0.3)
    plt.tight_layout()
    plt.savefig('v3_q13_opt2.png', dpi=100)
    plt.close()

def save_opt3():
    # Histogram
    data = np.random.normal(50, 15, 1000)
    plt.figure(figsize=(8, 6))
    plt.hist(data, bins=2, color=color_kvj, edgecolor='gray') # Bins=2 to match screenshot's 2 big blocks
    plt.title('Histogram', fontweight='bold', pad=20)
    plt.tight_layout()
    plt.savefig('v3_q13_opt3.png', dpi=100)
    plt.close()

def save_opt4():
    # Bar chart (horizontal)
    categories = ['A', 'B', 'C', 'D', 'E', 'F']
    y = [20, 25, 15, 30, 10, 12]
    plt.figure(figsize=(8, 6))
    plt.barh(categories, y, color=color_kvj)
    plt.title('Bar chart', fontweight='bold', pad=20)
    plt.grid(axis='x', linestyle='--', alpha=0.3)
    plt.tight_layout()
    plt.savefig('v3_q13_opt4.png', dpi=100)
    plt.close()

save_opt1()
save_opt2()
save_opt3()
save_opt4()
print("Distribution analysis charts generated successfully.")
