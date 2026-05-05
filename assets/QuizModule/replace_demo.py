import re

with open('Data-Module-3.html', 'r', encoding='utf-8') as f:
    text = f.read()

# Pattern matches the comparison-side containing the SVG and the INTERACTIVE DRILL DOWN DEMO block
pattern = re.compile(
    r'<div class="comparison-side" style="flex: 1;">\s*<!-- Data Drilling Visual Illustration -->.*?<!-- INTERACTIVE DRILL DOWN DEMO -->\s*<div class="interactive-demo-card"[^>]*>.*?</div>\s*</div>',
    re.DOTALL
)

replacement = '''<div class="comparison-side" style="flex: 1;">
                    <!-- INTERACTIVE DRILL DOWN DEMO -->
                    <div class="interactive-demo-card" style="background: #ffffff; padding: 25px; border-radius: 16px; border: 1px solid #e2e8f0; box-shadow: 0 4px 15px rgba(0,0,0,0.05);">
                        <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
                            <h4 style="margin: 0; color: #1e3a5f; font-size: 17px;">Interactive Demo: Data Drilling</h4>
                            <div id="drillBreadcrumb" style="font-size: 13px; font-weight: 600; color: #64748b;">
                                Level: <span style="color: #3b82f6;">Yearly Overview</span>
                            </div>
                            <button id="btnDrillUp" style="padding: 6px 12px; background: #f1f5f9; color: #475569; border: none; border-radius: 6px; cursor: pointer; font-family: 'Inter', sans-serif; font-weight: 600; font-size: 12px; display: none; transition: 0.2s;">
                                &larr; Drill Up
                            </button>
                        </div>
                        <p style="font-size: 13px; color: #64748b; margin-bottom: 15px; font-style: italic;">Click a bar to drill down (Year &rarr; Quarter &rarr; Month)!</p>
                        <div style="height: 250px; width: 100%;">
                            <canvas id="interactiveDrillChart"></canvas>
                        </div>
                    </div>
                </div>'''

if pattern.search(text):
    new_text = pattern.sub(replacement, text)
    with open('Data-Module-3.html', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Replaced SVG with Interactive Demo.")
else:
    print("Pattern not found. Using fallback replacement.")
    # Fallback: remove SVG div and move Interactive Demo
    svg_pattern = re.compile(r'<div class="comparison-side" style="flex: 1;">\s*<!-- Data Drilling Visual Illustration -->.*?</div>\s*</div>', re.DOTALL)
    demo_pattern = re.compile(r'<!-- INTERACTIVE DRILL DOWN DEMO -->\s*<div class="interactive-demo-card".*?</div>\s*</div>', re.DOTALL)
    
    text = svg_pattern.sub('', text)
    text = demo_pattern.sub('', text)
    
    insert_point = r'(<li><strong>Disaggregating:</strong> Breaking data down to a lower level \(Drill-down\)\.</li>\s*</ul>\s*</div>)'
    text = re.sub(insert_point, r'\1\n' + replacement, text)
    
    with open('Data-Module-3.html', 'w', encoding='utf-8') as f:
        f.write(text)
    print("Used fallback replacement.")
