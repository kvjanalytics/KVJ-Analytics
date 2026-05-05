import re

def replace_pattern_section():
    file_path = 'Data-Module-3.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # The block to replace starts at line 2284 (index 2283 if 0-indexed)
    # But it's safer to use a regex that matches the structure.
    
    pattern = r'<div class="comparison-side" style="flex: 1;">\s*<div style="display: flex; flex-direction: column; gap: 15px;">.*?<!-- Temporal -->.*?</div>\s*</div>\s*</div>'
    
    new_content = """<div class="comparison-side" style="flex: 1;">
                    <div style="display: flex; flex-direction: column; gap: 25px;">
                        <!-- Frequent Patterns -->
                        <div style="padding: 25px; background: #f0fdf4; border-left: 5px solid #10b981; border-radius: 16px; border: 1px solid #dcfce7;">
                            <h5 style="margin: 0 0 15px 0; color: #065f46; font-size: 19px; font-weight: 800;">3.11.1 Frequent Patterns (Association Rules)</h5>
                            <ul style="margin: 0; padding-left: 0; list-style: none; color: #065f46; font-size: 15px; line-height: 1.6;">
                                <li><strong>Goal:</strong> Discover sets of items that appear together frequently in a dataset.</li>
                                <li><strong>Focus:</strong> Co-occurrence (e.g., "People who buy bread also buy butter").</li>
                                <li><strong>Order:</strong> Not important.</li>
                                <li><strong>Techniques:</strong> Apriori, FP-Growth.</li>
                            </ul>
                        </div>

                        <!-- Sequential Patterns -->
                        <div style="padding: 25px; background: #eff6ff; border-left: 5px solid #3b82f6; border-radius: 16px; border: 1px solid #dbeafe;">
                            <h5 style="margin: 0 0 15px 0; color: #1e40af; font-size: 19px; font-weight: 800;">3.11.2 Sequential Patterns</h5>
                            <ul style="margin: 0; padding-left: 0; list-style: none; color: #1e40af; font-size: 15px; line-height: 1.6;">
                                <li><strong>Goal:</strong> Identify patterns where items occur in a specific order.</li>
                                <li><strong>Focus:</strong> Order (e.g., "A person who buys a laptop then buys a mouse").</li>
                                <li><strong>Order:</strong> Crucial.</li>
                                <li><strong>Techniques:</strong> PrefixSpan, SPADE.</li>
                                <li><strong>Types:</strong> Can be gapped (events in between) or ungapped (consecutive).</li>
                            </ul>
                        </div>

                        <!-- Temporal Patterns -->
                        <div style="padding: 25px; background: #fffaf3; border-left: 5px solid #f59e0b; border-radius: 16px; border: 1px solid #ffedd5;">
                            <h5 style="margin: 0 0 15px 0; color: #92400e; font-size: 19px; font-weight: 800;">3.11.3 Temporal Patterns</h5>
                            <ul style="margin: 0; padding-left: 0; list-style: none; color: #92400e; font-size: 15px; line-height: 1.6;">
                                <li><strong>Goal:</strong> Discover patterns involving time intervals, durations, or precise times.</li>
                                <li><strong>Focus:</strong> Time constraints (e.g., "If event A happens, event B happens 3-5 days later").</li>
                                <li><strong>Order:</strong> Important, with added timestamp/duration information.</li>
                                <li><strong>Types:</strong> Trends (long-term increases) or Seasonality (regular intervals).</li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Comparison Summary Table -->
            <div style="margin-top: 40px; background: white; padding: 40px; border-radius: 24px; border: 1px solid #f1f5f9;">
                <h4 style="color: #1e3a5f; margin-bottom: 25px; font-size: 22px; font-weight: 800;">Comparison Summary</h4>
                <div class="table-scroll">
                    <table class="raw-data-table">
                        <thead>
                            <tr style="background: #f8fafc;">
                                <th style="width: 20%;">Feature</th>
                                <th style="color: #059669;">Frequent Patterns</th>
                                <th style="color: #2563eb;">Sequential Patterns</th>
                                <th style="color: #d97706;">Temporal Patterns</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td><strong>Primary Goal</strong></td>
                                <td>Co-occurrence</td>
                                <td>Order of events</td>
                                <td>Time & Duration</td>
                            </tr>
                            <tr>
                                <td><strong>Order Constraint</strong></td>
                                <td>Irrelevant</td>
                                <td>Crucial</td>
                                <td>Crucial</td>
                            </tr>
                            <tr>
                                <td><strong>Time/Duration</strong></td>
                                <td>None</td>
                                <td>Implicit/Ignored</td>
                                <td>Explicitly analyzed</td>
                            </tr>
                            <tr>
                                <td><strong>Example</strong></td>
                                <td>{Bread, Milk}</td>
                                <td>A &rarr; B &rarr; C</td>
                                <td>A &rarr; (10 min) B</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>"""

    # We need to be very precise with the regex because of the nested divs.
    # Let's find the unique comments or structure.
    
    start_tag = '<div class="comparison-side" style="flex: 1;">'
    # We want the one that contains <!-- Sequential -->
    
    # Let's use a more specific search
    if '<!-- Sequential -->' in content:
        # Find the div starting at lines around 2284
        # We can split by <!-- Sequential --> and then find the enclosing tags.
        # But let's just do a string replace of the known block.
        
        old_block = """                <div class="comparison-side" style="flex: 1;">
                    <div style="display: flex; flex-direction: column; gap: 15px;">
                        <!-- Sequential -->
                        <div style="padding: 20px; background: #f8fafc; border-left: 4px solid #3b82f6; border-radius: 8px;">
                            <h5 style="margin: 0 0 5px 0; color: #1e40af; font-size: 17px;">3.11.1 Sequential Patterns</h5>
                            <p style="margin: 0; font-size: 15px; color: #475569;">
                                Identifying a sequence of events. 
                                <br><span style="font-style: italic; color: #1e293b; font-weight: 600;">Example: Customer buys a smartphone, then accessories a few weeks later.</span>
                            </p>
                        </div>
                        <!-- Frequent -->
                        <div style="padding: 20px; background: #f8fafc; border-left: 4px solid #10b981; border-radius: 8px;">
                            <h5 style="margin: 0 0 5px 0; color: #059669; font-size: 17px;">3.11.2 Frequent Patterns</h5>
                            <p style="margin: 0; font-size: 15px; color: #475569;">
                                Items or events that appear together (Market Basket Analysis).
                                <br><span style="font-style: italic; color: #1e293b; font-weight: 600;">Example: Customers often buy bread together with milk.</span>
                            </p>
                        </div>
                        <!-- Temporal -->
                        <div style="padding: 20px; background: #f8fafc; border-left: 4px solid #f59e0b; border-radius: 8px;">
                            <h5 style="margin: 0 0 5px 0; color: #92400e; font-size: 17px;">3.11.3 Temporal Patterns</h5>
                            <p style="margin: 0; font-size: 15px; color: #475569;">
                                Identifying how data changes over time.
                                <br><span style="font-style: italic; color: #1e293b; font-weight: 600;">Example: Retail sales significantly increasing during specific holiday months.</span>
                            </p>
                        </div>
                    </div>
                </div>
            </div>"""
        
        if old_block in content:
            new_text = content.replace(old_block, new_content)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(new_text)
            print("Successfully replaced pattern section")
        else:
            print("Could not find exact old block. Trying regex...")
            # Fallback to a slightly more flexible regex
            content = re.sub(r'<div class="comparison-side" style="flex: 1;">\s*<div style="display: flex; flex-direction: column; gap: 15px;">.*?<!-- Temporal -->.*?</div>\s*</div>\s*</div>', new_content, content, flags=re.DOTALL)
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            print("Replaced pattern section using regex")

replace_pattern_section()
