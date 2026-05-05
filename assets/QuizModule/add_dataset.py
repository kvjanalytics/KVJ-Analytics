import re

with open('Data-Module-3.html', 'r', encoding='utf-8') as f:
    text = f.read()

# 1. Add HTML for Table
html_table_snippet = """                </div>
                <!-- Dynamic Data Table -->
                <div style="margin-top: 30px; border-top: 1px solid #e2e8f0; padding-top: 20px;">
                    <h5 style="margin: 0 0 15px 0; color: #334155; font-size: 15px;">Underlying Dataset View</h5>
                    <div style="overflow-x: auto;">
                        <table id="drillDataTable" style="width: 100%; border-collapse: collapse; text-align: left; font-size: 14px;">
                            <thead>
                                <tr style="background: #f8fafc; border-bottom: 2px solid #e2e8f0;">
                                    <th style="padding: 10px; color: #475569;">Time Period</th>
                                    <th style="padding: 10px; color: #475569;">Sales Revenue ($)</th>
                                </tr>
                            </thead>
                            <tbody id="drillDataTableBody">
                                <!-- Populated dynamically -->
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>"""

text = re.sub(
    r'<div style="height: 300px; width: 100%;">\s*<canvas id="interactiveDrillChart"></canvas>\s*</div>\s*</div>',
    r'<div style="height: 300px; width: 100%;">\n                    <canvas id="interactiveDrillChart"></canvas>\n' + html_table_snippet,
    text
)

# 2. Add JS helper function and update updateDrillChart
js_helper = """                function populateDataTable(dataObj) {
                    const tbody = document.getElementById('drillDataTableBody');
                    if(!tbody) return;
                    tbody.innerHTML = '';
                    let total = 0;
                    for (let i = 0; i < dataObj.labels.length; i++) {
                        const tr = document.createElement('tr');
                        tr.style.borderBottom = '1px solid #f1f5f9';
                        
                        const tdLabel = document.createElement('td');
                        tdLabel.style.padding = '10px';
                        tdLabel.style.color = '#334155';
                        tdLabel.innerText = dataObj.labels[i];
                        
                        const tdValue = document.createElement('td');
                        tdValue.style.padding = '10px';
                        tdValue.style.color = '#1e3a5f';
                        tdValue.style.fontWeight = '600';
                        tdValue.innerText = '$' + dataObj.data[i].toLocaleString();
                        
                        tr.appendChild(tdLabel);
                        tr.appendChild(tdValue);
                        tbody.appendChild(tr);
                        
                        total += dataObj.data[i];
                    }
                    
                    const trTotal = document.createElement('tr');
                    trTotal.style.background = '#f8fafc';
                    trTotal.style.fontWeight = 'bold';
                    
                    const tdLabelTotal = document.createElement('td');
                    tdLabelTotal.style.padding = '10px';
                    tdLabelTotal.style.color = '#0f172a';
                    tdLabelTotal.innerText = 'Total';
                    
                    const tdValueTotal = document.createElement('td');
                    tdValueTotal.style.padding = '10px';
                    tdValueTotal.style.color = '#0f172a';
                    tdValueTotal.innerText = '$' + total.toLocaleString();
                    
                    trTotal.appendChild(tdLabelTotal);
                    trTotal.appendChild(tdValueTotal);
                    tbody.appendChild(trTotal);
                }

                function updateDrillChart(newStateKey)"""

text = text.replace('function updateDrillChart(newStateKey)', js_helper)

js_populate = """btn.style.display = 'none';
                    }
                    
                    populateDataTable(newData);
                }
                
                populateDataTable(drillData[currentDrillState]);
            }"""

text = re.sub(
    r'btn\.style\.display = \'none\';\s*}\s*}\s*}',
    js_populate,
    text
)

with open('Data-Module-3.html', 'w', encoding='utf-8') as f:
    f.write(text)

print("Added dynamically updating dataset table beneath the drill down chart.")
