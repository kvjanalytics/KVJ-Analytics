import matplotlib.pyplot as plt
import numpy as np

# Styles
plt.style.use('seaborn-v0_8-muted')
color_kvj = '#1e3a5f'
color_accent = '#38bdf8'
color_orange = '#f97316'

def save_opt1():
    # Line chart: Wait time vs Customers
    categories = ['Afternoon', 'Evening', 'Morning']
    wait_time = [18, 24, 9]
    customers = [55, 118, 25]
    
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.plot(categories, wait_time, marker='o', color=color_kvj, label='Average wait time', linewidth=2)
    ax.plot(categories, customers, marker='o', color=color_orange, label='Number of customers', linewidth=2)
    
    for i, txt in enumerate(wait_time):
        ax.annotate(txt, (categories[i], wait_time[i]), textcoords="offset points", xytext=(0,10), ha='center')
    for i, txt in enumerate(customers):
        ax.annotate(txt, (categories[i], customers[i]), textcoords="offset points", xytext=(0,10), ha='center')
        
    plt.title('Customer Service Metrics', fontweight='bold', pad=20)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.3)
    plt.tight_layout()
    plt.savefig('v3_q11_opt1.png', dpi=100)
    plt.close()

def save_opt2():
    # Bar chart with error bars
    categories = ['Morning', 'Afternoon', 'Evening/Weekend']
    means = [15, 28, 34]
    errors = [5, 6, 5]
    
    plt.figure(figsize=(8, 6))
    plt.bar(categories, means, yerr=errors, capsize=5, color=color_kvj, alpha=0.9)
    plt.ylabel('Customer Wait Time (min)', fontweight='bold')
    plt.title('Average Wait Time by Period', fontweight='bold', pad=20)
    plt.tight_layout()
    plt.savefig('v3_q11_opt2.png', dpi=100)
    plt.close()

def save_opt3():
    # Grouped Bar chart
    categories = ['Morning', 'Afternoon', 'Evening/Weekend']
    avg_wait = [18, 24, 8]
    std_dev = [12, 17, 5]
    
    x = np.arange(len(categories))
    width = 0.35
    
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(x - width/2, avg_wait, width, label='AVG Customer wait', color=color_kvj)
    ax.bar(x + width/2, std_dev, width, label='Customer std deviation', color=color_orange)
    
    ax.set_xticks(x)
    ax.set_xticklabels(categories)
    plt.title('Wait Time Statistics', fontweight='bold', pad=20)
    plt.legend()
    plt.tight_layout()
    plt.savefig('v3_q11_opt3.png', dpi=100)
    plt.close()

def save_opt4():
    # Scatter Plot showing outliers
    # Generating some clusters and a few outliers
    x = [2]*10 + [12]*10 + [22]*10 + [55]*5
    y = [20, 25, 40, 45, 50, 55, 70, 100, 35, 42] + \
        [60, 65, 80, 40, 55, 50, 42, 63, 61, 58] + \
        [30, 35, 75, 95, 32, 38, 41, 33, 31, 36] + \
        [5, 8, 10, 15, 12]
    
    plt.figure(figsize=(8, 6))
    plt.scatter(x, y, color=color_kvj, alpha=0.8, s=40)
    plt.xlabel('Time of Day Index', fontweight='bold')
    plt.ylabel('Wait Time (min)', fontweight='bold')
    plt.title('Wait Time Distribution (Individual Data Points)', fontweight='bold', pad=20)
    plt.grid(True, linestyle='--', alpha=0.3)
    plt.tight_layout()
    plt.savefig('v3_q11_opt4.png', dpi=100)
    plt.close()

save_opt1()
save_opt2()
save_opt3()
save_opt4()
print("Outlier analysis charts generated successfully.")
