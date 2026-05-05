import re

def clean_replace_pattern():
    file_path = 'Data-Module-3.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the section starting at <div id="s3-11-patterns"
    # and ending before <div id="s3-12-anomaly"
    
    start_marker = '<div id="s3-11-patterns"'
    end_marker = '<div id="s3-12-anomaly"'
    
    start_idx = content.find(start_marker)
    end_idx = content.find(end_marker)
    
    if start_idx != -1 and end_idx != -1:
        # We want to keep the slide-header div
        # Find the end of the slide-header div
        header_end = content.find('</div>', start_idx) + 6
        
        new_section_content = """
            <div style="background: white; padding: 40px; border-radius: 24px; border: 1px solid #f1f5f9; margin-bottom: 60px;">
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 30px; margin-bottom: 50px;">
                    <!-- Frequent Patterns -->
                    <div style="background: #f0fdf4; padding: 30px; border-radius: 20px; border: 1px solid #dcfce7; border-top: 5px solid #10b981;">
                        <h4 style="margin: 0 0 20px 0; color: #065f46; font-size: 20px; font-weight: 800;">Frequent Patterns (Association Rules)</h4>
                        <div style="display: flex; flex-direction: column; gap: 15px; color: #065f46; font-size: 15.5px; line-height: 1.6;">
                            <div><strong style="color: #047857;">Goal:</strong> Discover sets of items that appear together frequently in a dataset.</div>
                            <div><strong style="color: #047857;">Focus:</strong> Co-occurrence (e.g., "People who buy bread also buy butter").</div>
                            <div><strong style="color: #047857;">Order:</strong> Not important.</div>
                            <div><strong style="color: #047857;">Techniques:</strong> Apriori, FP-Growth.</div>
                        </div>
                    </div>

                    <!-- Sequential Patterns -->
                    <div style="background: #eff6ff; padding: 30px; border-radius: 20px; border: 1px solid #dbeafe; border-top: 5px solid #3b82f6;">
                        <h4 style="margin: 0 0 20px 0; color: #1e40af; font-size: 20px; font-weight: 800;">Sequential Patterns</h4>
                        <div style="display: flex; flex-direction: column; gap: 15px; color: #1e40af; font-size: 15.5px; line-height: 1.6;">
                            <div><strong style="color: #1d4ed8;">Goal:</strong> Identify patterns where items occur in a specific order.</div>
                            <div><strong style="color: #1d4ed8;">Focus:</strong> Order (e.g., "A person who buys a laptop then buys a mouse").</div>
                            <div><strong style="color: #1d4ed8;">Order:</strong> Crucial.</div>
                            <div><strong style="color: #1d4ed8;">Techniques:</strong> PrefixSpan, SPADE.</div>
                            <div><strong style="color: #1d4ed8;">Types:</strong> Can be gapped (events in between) or ungapped (consecutive).</div>
                        </div>
                    </div>

                    <!-- Temporal Patterns -->
                    <div style="background: #fffaf3; padding: 30px; border-radius: 20px; border: 1px solid #ffedd5; border-top: 5px solid #f59e0b;">
                        <h4 style="margin: 0 0 20px 0; color: #92400e; font-size: 20px; font-weight: 800;">Temporal Patterns</h4>
                        <div style="display: flex; flex-direction: column; gap: 15px; color: #92400e; font-size: 15.5px; line-height: 1.6;">
                            <div><strong style="color: #b45309;">Goal:</strong> Discover patterns involving time intervals, durations, or precise times.</div>
                            <div><strong style="color: #b45309;">Focus:</strong> Time constraints (e.g., "If event A happens, event B happens 3-5 days later").</div>
                            <div><strong style="color: #b45309;">Order:</strong> Important, with added timestamp/duration information.</div>
                            <div><strong style="color: #b45309;">Types:</strong> Trends (long-term increases) or Seasonality (regular intervals). <span style="font-size: 12px; opacity: 0.6;">[1, 2, 3, 4, 5, 6]</span></div>
                        </div>
                    </div>
                </div>

                <div style="border-top: 1px solid #f1f5f9; padding-top: 40px;">
                    <h4 style="color: #1e3a5f; margin-bottom: 25px; font-size: 22px; font-weight: 800;">Comparison Summary</h4>
                    <div class="table-scroll">
                        <table class="raw-data-table">
                            <thead>
                                <tr style="background: #f8fafc;">
                                    <th style="width: 20%;">Feature <span style="font-size: 10px; opacity: 0.5;">[1, 2, 3, 4, 5]</span></th>
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
                </div>
            </div>
"""
        new_content = content[:header_end] + new_section_content + content[end_idx:]
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Successfully overhauled pattern section")
    else:
        print("Markers not found")

clean_replace_pattern()
