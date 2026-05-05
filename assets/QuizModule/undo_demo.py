import re

with open('Data-Module-3.html', 'r', encoding='utf-8') as f:
    text = f.read()

pattern = re.compile(
    r'<div class="comparison-side" style="flex: 1;">\s*<!-- INTERACTIVE DRILL DOWN DEMO -->.*?</div>\s*</div>\s*</div>',
    re.DOTALL
)

replacement = """<div class="comparison-side" style="flex: 1;">
                    <!-- Data Drilling Visual Illustration -->
                    <div style="background: #f8fafc; padding: 25px; border-radius: 16px; border: 1px solid #e2e8f0;">
                        <svg viewBox="0 0 400 350" style="width: 100%; height: auto;">
                            <!-- Stage 1: High Level -->
                            <rect x="50" y="20" width="300" height="80" rx="4" fill="none" stroke="#ccc" stroke-width="1"/>
                            <rect x="65" y="45" width="50" height="45" fill="#7dd3fc" rx="2"/>
                            <rect x="135" y="35" width="50" height="55" fill="#7dd3fc" rx="2"/>
                            <rect x="205" y="55" width="50" height="35" fill="#7dd3fc" rx="2"/>
                            <!-- Sub-bars in middle bar of Stage 1 -->
                            <rect x="140" y="45" width="12" height="40" fill="#94a3b8" rx="1"/>
                            <rect x="154" y="65" width="12" height="20" fill="#94a3b8" rx="1"/>
                            <rect x="168" y="55" width="12" height="30" fill="#94a3b8" rx="1"/>

                            <!-- Arrow 1 -->
                            <path d="M200 105 L200 125" stroke="#333" stroke-width="2" marker-end="url(#arrowhead)"/>

                            <!-- Stage 2: Mid Level -->
                            <rect x="50" y="135" width="300" height="80" rx="4" fill="none" stroke="#ccc" stroke-width="1"/>
                            <rect x="65" y="150" width="50" height="55" fill="#94a3b8" rx="2"/>
                            <rect x="135" y="175" width="50" height="30" fill="#94a3b8" rx="2"/>
                            <rect x="205" y="165" width="50" height="40" fill="#94a3b8" rx="2"/>
                            <!-- Sub-bars in right bar of Stage 2 -->
                            <rect x="210" y="190" width="12" height="10" fill="#7dd3fc" rx="1"/>
                            <rect x="224" y="180" width="12" height="20" fill="#7dd3fc" rx="1"/>
                            <rect x="238" y="170" width="12" height="30" fill="#7dd3fc" rx="1"/>

                            <!-- Arrow 2 -->
                            <path d="M250 220 L250 240" stroke="#333" stroke-width="2" marker-end="url(#arrowhead)"/>

                            <!-- Stage 3: Low Level (Drilled Down) -->
                            <rect x="50" y="250" width="300" height="80" rx="4" fill="none" stroke="#ccc" stroke-width="1"/>
                            <rect x="65" y="300" width="50" height="20" fill="#7dd3fc" rx="2"/>
                            <rect x="135" y="285" width="50" height="35" fill="#7dd3fc" rx="2"/>
                            <rect x="205" y="265" width="50" height="55" fill="#7dd3fc" rx="2"/>

                            <!-- Definitions -->
                            <defs>
                                <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="0" refY="3.5" orient="auto">
                                    <polygon points="0 0, 10 3.5, 0 7" fill="#333" />
                                </marker>
                            </defs>
                        </svg>
                    </div>
                    <p style="font-size: 14px; color: #1e293b; font-weight: 600; margin-top: 15px; font-style: italic;">
                        Visualizing the "Drill-Down" process: From high-level summaries to detailed individual segments.
                    </p>
                </div>
            </div>

            <!-- INTERACTIVE DRILL DOWN DEMO -->
            <div class="interactive-demo-card" style="margin-top: 50px; background: #ffffff; padding: 30px; border-radius: 16px; border: 1px solid #e2e8f0; box-shadow: 0 4px 15px rgba(0,0,0,0.05);">
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 20px;">
                    <h4 style="margin: 0; color: #1e3a5f; font-size: 18px;">Interactive Demo: Data Drilling</h4>
                    <div id="drillBreadcrumb" style="font-size: 14px; font-weight: 600; color: #64748b;">
                        Level: <span style="color: #3b82f6;">Yearly Overview</span>
                    </div>
                    <button id="btnDrillUp" style="padding: 8px 16px; background: #f1f5f9; color: #475569; border: none; border-radius: 6px; cursor: pointer; font-family: 'Inter', sans-serif; font-weight: 600; font-size: 13px; display: none; transition: 0.2s;">
                        &larr; Drill Up
                    </button>
                </div>
                <p style="font-size: 14px; color: #64748b; margin-bottom: 20px; font-style: italic;">Click on any bar to drill down into deeper data granularity (Year &rarr; Quarter &rarr; Month)!</p>
                <div style="height: 300px; width: 100%;">
                    <canvas id="interactiveDrillChart"></canvas>
                </div>
            </div>"""

if pattern.search(text):
    new_text = pattern.sub(replacement, text)
    with open('Data-Module-3.html', 'w', encoding='utf-8') as f:
        f.write(new_text)
    print("Successfully undid the change.")
else:
    print("Could not find the modified block to replace.")
