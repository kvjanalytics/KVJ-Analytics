import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Setup Figure
fig, ax = plt.subplots(figsize=(14, 7), facecolor='white') # Wider figure
ax.axis('off')

# Box settings
box_width = 3.8
box_height = 0.6
left_x = 0.5
right_x = 6.5 # Center for the questions
box_offset = 6.0 # Offset from right_x to the boxes
y_start = 5
y_step = 1.0

# Analysis Types (Left)
types = ["Descriptive analysis", "Predictive analysis", "Hypothesis Testing", "Diagnostic analysis", "Prescriptive analysis"]
# Analysis Questions (Right)
questions = ["What happened?", "Why did it happen?", "What should we do next?", "Is there enough evidence to draw conclusion", "What will happen?"]

# Draw Left Boxes
for i, t in enumerate(types):
    rect = patches.Rectangle((left_x, y_start - i*y_step), box_width, box_height, 
                             linewidth=1.5, edgecolor='#1e3a5f', facecolor='white')
    ax.add_patch(rect)
    ax.text(left_x + box_width/2, y_start - i*y_step + box_height/2, t, 
            ha='center', va='center', fontweight='bold', color='#1e3a5f', fontsize=11)

# Draw Right Boxes
for i, q in enumerate(questions):
    # Label
    ax.text(right_x, y_start - i*y_step + box_height/2, q, 
            ha='left', va='center', fontweight='bold', color='#1e3a5f', fontsize=11)
    # Box - Moved further right to avoid overlap
    rect = patches.Rectangle((right_x + box_offset, y_start - i*y_step), 1.0, box_height, 
                             linewidth=1.5, edgecolor='#1e3a5f', facecolor='#f1f5f9')
    ax.add_patch(rect)

# Add Column Headers
ax.text(left_x + box_width/2, 6.2, "Analysis Type", ha='center', va='center', fontsize=13, fontweight='bold', color='#1e3a5f')
ax.text(right_x + box_offset/2, 6.2, "Analysis Question", ha='center', va='center', fontsize=13, fontweight='bold', color='#1e3a5f')

plt.xlim(0, 15)
plt.ylim(0, 7)
plt.tight_layout()
plt.savefig('analysis_types_matching.png', dpi=150, bbox_inches='tight')
print("Analysis types matching illustration refined successfully.")
