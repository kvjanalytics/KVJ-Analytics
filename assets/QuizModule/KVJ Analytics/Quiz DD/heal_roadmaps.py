import os

roadmap_bottom_half = """
            <!-- Mock Tests -->
            <div class="modules-section">
                <div style="text-align: center; margin: 20px 0;">
                    <button onclick="syncProgress()" id="syncBtn" style="background: #f8fafc; color: #64748b; border: 1.5px solid #e2e8f0; padding: 10px 20px; border-radius: 10px; font-weight: 600; font-size: 0.9rem; cursor: pointer; display: flex; align-items: center; justify-content: center; margin: 0 auto; gap: 8px; transition: all 0.2s;" onmouseover="this.style.background='#fff'; this.style.borderColor='#0284c7'; this.style.color='#0284c7'" onmouseout="this.style.background='#f8fafc'; this.style.borderColor='#e2e8f0'; this.style.color='#64748b'">
                        <svg width="18" height="18" fill="none" stroke="currentColor" stroke-width="2" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"></path></svg>
                        Sync Progress from Server
                    </button>
                    <p id="syncStatus" style="font-size: 0.8rem; color: #94a3b8; margin-top: 8px; display: none;"></p>
                </div>
                <h2 class="section-title">Mock Assessments</h2>
                <div class="module-list">
                    <div class="mock-card">
                        <div class="mock-badge">
                            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#0891b2" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>
                        </div>
                        <div class="mock-info">
                            <div class="mock-name">Mock Test 1</div>
                            <div class="mock-desc">Comprehensive assessment covering all Python fundamentals.</div>
                        </div>
                        <a href="javascript:void(0)" onclick="checkMockCode('PYMOCK1', 'module_quiz.html?mock=1')" class="btn-mock">Take Mock</a>
                    </div>
                    <div class="mock-card">
                        <div class="mock-badge">
                            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#0891b2" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"/><polyline points="14 2 14 8 20 8"/><line x1="16" y1="13" x2="8" y2="13"/><line x1="16" y1="17" x2="8" y2="17"/><polyline points="10 9 9 9 8 9"/></svg>
                        </div>
                        <div class="mock-info">
                            <div class="mock-name">Mock Test 2</div>
                            <div class="mock-desc">Advanced full-length practice exam simulation environment.</div>
                        </div>
                        <a href="javascript:void(0)" onclick="checkMockCode('PYMOCK2', 'module_quiz.html?mock=2')" class="btn-mock">Take Mock</a>
                    </div>
                    <div class="mock-card">
                        <div class="mock-badge">
                            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#0891b2" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M6 9H4.5a2.5 2.5 0 0 1 0-5H6"/><path d="M18 9h1.5a2.5 2.5 0 0 0 0-5H18"/><path d="M4 22h16"/><path d="M10 14.66V17c0 .55-.47.98-.97 1.21C7.85 18.75 7 20.24 7 22"/><path d="M14 14.66V17c0 .55.47.98.97 1.21C16.15 18.75 17 20.24 17 22"/><path d="M18 2H6v7a6 6 0 0 0 12 0V2z"/></svg>
                        </div>
                        <div class="mock-info">
                            <div class="mock-name">Mock Test 3 — Full Certification Simulation</div>
                            <div class="mock-desc">Final simulation covering all advanced Python topics.</div>
                        </div>
                        <a href="javascript:void(0)" onclick="checkMockCode('PYMOCK3', 'module_quiz.html?mock=3')" class="btn-mock">Take Mock</a>
                    </div>
                </div>
            </div>
        </div>
        <div class="sidebar">
            <div class="sidebar-card">
                <div class="sidebar-thumb">
                    <img src="pearson_python_badge_transparent.png" alt="Badge" style="width:100%;">
                    <p>Pearson IT Specialist & KVJ Certification</p>
                </div>
                <div class="sidebar-body">
                    <div class="sidebar-price">Career Certification</div>
                    <div class="cert-card">
                        <h4>Official Certification</h4>
                        <p>Earn globally recognized Pearson IT Specialist and KVJ Career certificates.</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
    <div id="mockCodeModal" style="display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(15,23,42,0.6); backdrop-filter:blur(8px); z-index:10000; align-items:center; justify-content:center; padding:20px;">
        <div style="background:white; padding:40px; border-radius:24px; max-width:440px; width:100%; position:relative; text-align:center;">
            <div style="width:64px; height:64px; background:#fef2f2; border-radius:16px; display:flex; align-items:center; justify-content:center; margin:0 auto 24px;">
                <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="#ef4444" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
            </div>
            <h3 style="font-size:1.5rem; font-weight:800; color:#0f172a; margin-bottom:12px;">Access Restricted</h3>
            <p style="color:#64748b; font-size:0.95rem; margin-bottom:24px;">This mock test requires an access code or completing all modules with 85%+.</p>
            <div id="mockProgressNote" style="font-size: 0.8rem; color: #f59e0b; background: #fffbeb; padding: 10px; border-radius: 8px; margin-bottom: 20px; display: none; font-weight: 500;"></div>
            <input type="text" id="mockCodeInput" placeholder="Enter Access Code" style="width:100%; padding:14px 20px; border:2px solid #e2e8f0; border-radius:12px; font-size:1rem; font-weight:600; margin-bottom:12px; text-align:center;">
            <div id="mockCodeError" style="color:#ef4444; font-size:0.85rem; font-weight:600; margin-bottom:20px; display:none;">Invalid access code.</div>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px;">
                <button onclick="closeMockModal()" style="padding:14px; background:#f8fafc; color:#64748b; border:none; border-radius:12px; font-weight:700; cursor:pointer;">Cancel</button>
                <button onclick="submitMockCode()" style="padding:14px; background:#ef4444; color:white; border:none; border-radius:12px; font-weight:700; cursor:pointer;">Unlock</button>
            </div>
        </div>
    </div>
"""

data_roadmap_bottom_half = roadmap_bottom_half.replace('PYMOCK', 'DAMOCK').replace('Python', 'Data Analytics')

def heal_file(path, content_to_add):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Find the end of modules-list (M6)
    # The broken file ends at </body></html> but we want to inject before that.
    
    # Re-read the file to get everything up to the modules
    insertion_point = content.find('<div class="modules-section" id="modules-list">')
    if insertion_point == -1: insertion_point = content.find('<div class="modules-section">')
    
    # We want to keep everything up to the END of that section
    # Let's find the closing </div> of the module-list
    # Actually, the broken file still has the modules.
    
    # Let's find where M6 ends.
    m6_index = content.find('Module 6')
    if m6_index != -1:
        # Find the next </div></div></div>
        end_of_modules = content.find('</div>', m6_index)
        end_of_modules = content.find('</div>', end_of_modules + 5)
        end_of_modules = content.find('</div>', end_of_modules + 5)
        
        main_part = content[:end_of_modules + 6]
        
        # Now find the script
        script_start = content.find('<script>')
        script_end = content.find('</script>', script_start) + 9
        script_part = content[script_start:script_end]
        
        final_html = main_part + content_to_add + script_part + "\\n</body>\\n</html>"
        
        with open(path, 'w', encoding='utf-8') as f:
            f.write(final_html)
        print(f"Healed {path}")

heal_file('c:/Users/kj anand/Downloads/Quiz DD/roadmap.html', roadmap_bottom_half)
heal_file('c:/Users/kj anand/Downloads/Quiz DD/data_roadmap.html', data_roadmap_bottom_half)
