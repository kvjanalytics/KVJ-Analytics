import re

def update_module_4():
    with open('Data-Module-4.html', 'r', encoding='utf-8') as f:
        content = f.read()

    # 4.3 Apple Case Study
    content = content.replace('<h4>Financial Reports</h4>', '<h4>4.3.1 Financial Reports</h4>')
    content = content.replace('<h4>Sales Reports</h4>', '<h4>4.3.2 Sales Reports</h4>')
    content = content.replace('<h4>Performance Reports</h4>', '<h4>4.3.3 Performance Reports</h4>')
    
    # 4.4 Importance/Audience
    content = content.replace('<h3>Importance of Reporting</h3>', '<h3>4.4.1 Importance of Reporting</h3>')
    content = content.replace('<h3>Who Uses Reports?</h3>', '<h3>4.4.2 Who Uses Reports?</h3>')
    
    # 4.9 Visualization Library
    charts = [
        'Column Chart', 'Bar Chart', 'Line Chart', 'Scatter Plot', 
        'Pie Chart', 'Donut Chart', 'Tree Map', 'Area Chart', 
        'Ribbon Chart', 'Funnel Chart', 'Waterfall Chart', 'Sankey Diagram'
    ]
    for i, chart in enumerate(charts, 1):
        content = content.replace(f'<h3>{chart}</h3>', f'<h3>4.9.{i} {chart}</h3>')

    with open('Data-Module-4.html', 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated Data-Module-4.html")

update_module_4()
