import matplotlib.pyplot as plt
import numpy as np

# Data
labels = ['Motorized bike', 'Golf cart', 'Utility Vehicle', '2-wheel Scooter', '3-Wheel Scooter', '4-wheel Scooter']
quantities = [600, 600, 425, 850, 1200, 789]
prices = [1200, 7500, 8000, 900, 2999, 3500]
totals = [720000, 4500000, 3400000, 765000, 3598800, 2761500]

# Adjust labels for plot
plot_labels = ['M-Bike', 'Golf', 'Utility', '2-Scout', '3-Scout', '4-Scout']

# Set Style
plt.style.use('seaborn-v0_8-muted')
color_kvj = '#1e3a5f'
color_accent = '#38bdf8'

def save_opt_b():
    fig, ax1 = plt.subplots(figsize=(8, 6))
    ax2 = ax1.twinx()
    ax1.bar(plot_labels, quantities, color=color_accent, label='Quantity')
    ax2.plot(plot_labels, prices, color=color_kvj, marker='o', linewidth=2, label='Price')
    ax1.set_ylabel('Quantity', color=color_accent, fontweight='bold')
    ax2.set_ylabel('Price ($)', color=color_kvj, fontweight='bold')
    plt.title('Quantity Sold vs Price', fontweight='bold', pad=20)
    plt.tight_layout()
    plt.savefig('v3_q6_optB.png', dpi=100)
    plt.close()

def save_opt_c():
    plt.figure(figsize=(8, 6))
    plt.scatter(quantities, prices, color=color_kvj, s=100, alpha=0.7)
    plt.xlabel('Quantity Sold', fontweight='bold')
    plt.ylabel('Price ($)', fontweight='bold')
    plt.title('Price vs Quantity Correlation', fontweight='bold', pad=20)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.savefig('v3_q6_optC.png', dpi=100)
    plt.close()

def save_opt_d():
    x = np.arange(len(plot_labels))
    width = 0.35
    fig, ax = plt.subplots(figsize=(8, 6))
    # Normalized for display since they are different scales
    ax.bar(x - width/2, [q/max(quantities) for q in quantities], width, label='Quantity (Rel)', color=color_accent)
    ax.bar(x + width/2, [t/max(totals) for t in totals], width, label='Total (Rel)', color='#f97316')
    ax.set_xticks(x)
    ax.set_xticklabels(plot_labels)
    plt.title('Quantity vs Revenue contribution', fontweight='bold', pad=20)
    plt.legend()
    plt.tight_layout()
    plt.savefig('v3_q6_optD.png', dpi=100)
    plt.close()

save_opt_b()
save_opt_c()
save_opt_d()
print("Charts generated successfully.")
