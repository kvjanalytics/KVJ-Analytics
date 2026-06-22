import re

with open('Data-Module-3.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# 1. HTML Insertion
html_snippet = """
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
            </div>
"""

# Find insertion point
target = r'(Visualizing the "Drill-Down" process: From high-level summaries to detailed individual segments.\s*</p>\s*</div>\s*</div>)'
if re.search(target, html_content):
    html_content = re.sub(target, r'\1\n' + html_snippet, html_content)
else:
    print("Could not find HTML insertion point")

# 2. JS Insertion
js_snippet = """
            // --- Interactive Drill-Down Chart Data ---
            const drillData = {
                'Year': {
                    labels: ['2022', '2023'],
                    data: [150000, 210000],
                    colors: ['#3b82f6', '#3b82f6'],
                    level: 'Yearly Overview',
                    nextLevel: 'Quarter'
                },
                'Quarter_2022': {
                    labels: ['Q1 2022', 'Q2 2022', 'Q3 2022', 'Q4 2022'],
                    data: [35000, 40000, 30000, 45000],
                    colors: ['#10b981', '#10b981', '#10b981', '#10b981'],
                    level: 'Quarterly Overview (2022)',
                    nextLevel: 'Month',
                    parent: 'Year'
                },
                'Quarter_2023': {
                    labels: ['Q1 2023', 'Q2 2023', 'Q3 2023', 'Q4 2023'],
                    data: [45000, 50000, 60000, 55000],
                    colors: ['#10b981', '#10b981', '#10b981', '#10b981'],
                    level: 'Quarterly Overview (2023)',
                    nextLevel: 'Month',
                    parent: 'Year'
                },
                'Month_2022_Q1': { labels: ['Jan', 'Feb', 'Mar'], data: [10000, 12000, 13000], colors: ['#f59e0b', '#f59e0b', '#f59e0b'], level: 'Monthly Detail (Q1 2022)', parent: 'Quarter_2022' },
                'Month_2022_Q2': { labels: ['Apr', 'May', 'Jun'], data: [13000, 14000, 13000], colors: ['#f59e0b', '#f59e0b', '#f59e0b'], level: 'Monthly Detail (Q2 2022)', parent: 'Quarter_2022' },
                'Month_2022_Q3': { labels: ['Jul', 'Aug', 'Sep'], data: [10000, 9000, 11000], colors: ['#f59e0b', '#f59e0b', '#f59e0b'], level: 'Monthly Detail (Q3 2022)', parent: 'Quarter_2022' },
                'Month_2022_Q4': { labels: ['Oct', 'Nov', 'Dec'], data: [14000, 15000, 16000], colors: ['#f59e0b', '#f59e0b', '#f59e0b'], level: 'Monthly Detail (Q4 2022)', parent: 'Quarter_2022' },
                
                'Month_2023_Q1': { labels: ['Jan', 'Feb', 'Mar'], data: [14000, 15000, 16000], colors: ['#f59e0b', '#f59e0b', '#f59e0b'], level: 'Monthly Detail (Q1 2023)', parent: 'Quarter_2023' },
                'Month_2023_Q2': { labels: ['Apr', 'May', 'Jun'], data: [16000, 17000, 17000], colors: ['#f59e0b', '#f59e0b', '#f59e0b'], level: 'Monthly Detail (Q2 2023)', parent: 'Quarter_2023' },
                'Month_2023_Q3': { labels: ['Jul', 'Aug', 'Sep'], data: [19000, 20000, 21000], colors: ['#f59e0b', '#f59e0b', '#f59e0b'], level: 'Monthly Detail (Q3 2023)', parent: 'Quarter_2023' },
                'Month_2023_Q4': { labels: ['Oct', 'Nov', 'Dec'], data: [18000, 18500, 18500], colors: ['#f59e0b', '#f59e0b', '#f59e0b'], level: 'Monthly Detail (Q4 2023)', parent: 'Quarter_2023' }
            };

            let currentDrillState = 'Year';
            const drillCanvas = document.getElementById('interactiveDrillChart');
            if (drillCanvas) {
                const drillCtx = drillCanvas.getContext('2d');
                const drillChart = new Chart(drillCtx, {
                    type: 'bar',
                    plugins: [ChartDataLabels],
                    data: {
                        labels: drillData[currentDrillState].labels,
                        datasets: [{
                            label: 'Sales Revenue ($)',
                            data: drillData[currentDrillState].data,
                            backgroundColor: drillData[currentDrillState].colors,
                            borderRadius: 6,
                            barPercentage: 0.6
                        }]
                    },
                    options: {
                        responsive: true,
                        maintainAspectRatio: false,
                        plugins: {
                            legend: { display: false },
                            tooltip: {
                                backgroundColor: 'rgba(30, 58, 95, 0.9)',
                                titleFont: { family: 'Inter', size: 14 },
                                bodyFont: { family: 'Inter', size: 15, weight: 'bold' },
                                padding: 12,
                                callbacks: {
                                    label: function(context) {
                                        return '$' + context.parsed.y.toLocaleString();
                                    }
                                }
                            },
                            datalabels: {
                                anchor: 'end',
                                align: 'top',
                                color: '#1e3a5f',
                                font: { weight: 'bold', family: 'Inter', size: 13 },
                                formatter: function(value) {
                                    return '$' + value.toLocaleString();
                                }
                            }
                        },
                        scales: {
                            y: { beginAtZero: true, grid: { color: '#f1f5f9' }, border: { display: false } },
                            x: { grid: { display: false }, border: { display: false }, ticks: { font: { weight: '600', family: 'Inter', size: 14 } } }
                        },
                        onClick: (e, elements) => {
                            if (elements.length > 0) {
                                const index = elements[0].index;
                                handleDrillDown(index);
                            }
                        },
                        onHover: (e, elements) => {
                            e.native.target.style.cursor = elements.length > 0 && drillData[currentDrillState].nextLevel ? 'pointer' : 'default';
                        }
                    }
                });

                function handleDrillDown(index) {
                    const currentStateData = drillData[currentDrillState];
                    if (!currentStateData.nextLevel) return;

                    let nextStateKey = '';
                    if (currentDrillState === 'Year') {
                        const year = currentStateData.labels[index];
                        nextStateKey = `Quarter_${year}`;
                    } else if (currentDrillState.startsWith('Quarter')) {
                        const year = currentDrillState.split('_')[1];
                        const q = currentStateData.labels[index].split(' ')[0];
                        nextStateKey = `Month_${year}_${q}`;
                    }

                    if (drillData[nextStateKey]) {
                        updateDrillChart(nextStateKey);
                    }
                }

                document.getElementById('btnDrillUp').addEventListener('click', () => {
                    const currentStateData = drillData[currentDrillState];
                    if (currentStateData.parent) {
                        updateDrillChart(currentStateData.parent);
                    }
                });

                function updateDrillChart(newStateKey) {
                    currentDrillState = newStateKey;
                    const newData = drillData[currentDrillState];
                    
                    drillChart.data.labels = newData.labels;
                    drillChart.data.datasets[0].data = newData.data;
                    drillChart.data.datasets[0].backgroundColor = newData.colors;
                    drillChart.update();

                    document.getElementById('drillBreadcrumb').innerHTML = `Level: <span style="color: #3b82f6;">${newData.level}</span>`;
                    const btn = document.getElementById('btnDrillUp');
                    if (newData.parent) {
                        btn.style.display = 'inline-block';
                    } else {
                        btn.style.display = 'none';
                    }
                }
            }
"""

js_target = r'(// Highlight active section on scroll)'
if re.search(js_target, html_content):
    html_content = re.sub(js_target, js_snippet + r'\n            \1', html_content)
else:
    print("Could not find JS insertion point")

with open('Data-Module-3.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("Updated Data-Module-3.html with Drill-Down Component")
