import matplotlib.pyplot as plt

# Adjusted Data to make "Most chocolate" the correct answer (ID: 18 Option 3)
labels = ['Vanilla', 'Strawberry', 'Chocolate']
sizes = [25, 30, 45] # Chocolate is now definitively the most
colors = ['#f1f5f9', '#d946ef', '#1c1917'] # Light gray, Pink, Dark brown/black
explode = (0, 0, 0.1)  # slightly explode the 'Most' slice (Chocolate)

# Setup Figure
fig, ax = plt.subplots(figsize=(10, 6), facecolor='white')

# Pie Chart
patches, texts, autotexts = ax.pie(sizes, labels=labels, autopct='%1.0f%%', 
                                  startangle=90, colors=colors, explode=explode,
                                  shadow=True, wedgeprops={'edgecolor': 'gray', 'linewidth': 0.5})

# Styling texts
for text in texts:
    text.set_fontweight('bold')
    text.set_color('#1e3a5f')
for autotext in autotexts:
    autotext.set_fontweight('bold')
    autotext.set_color('white') if autotext.get_text() == '45%' else autotext.set_color('#1e3a5f')

plt.title('Favourite Ice cream Flavor', fontsize=16, fontweight='bold', color='#1e3a5f', pad=20)
plt.legend(loc='lower center', bbox_to_anchor=(0.5, -0.1), ncol=3, frameon=False)

plt.tight_layout()
plt.savefig('ice_cream_pie_chart.png', dpi=150)
print("Ice cream pie chart updated for logical consistency.")
