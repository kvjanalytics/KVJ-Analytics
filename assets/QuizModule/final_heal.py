import os

# --- TEMPLATES ---
mock_section_html = """
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
                <div class="mock-badge">📝</div>
                <div class="mock-info">
                    <div class="mock-name">Mock Test 1</div>
                    <div class="mock-desc">Comprehensive assessment covering all fundamentals.</div>
                </div>
                <a href="javascript:void(0)" onclick="checkMockCode('PREFIXMOCK1', 'module_quiz.html?mock=1')" class="btn-mock">Take Mock</a>
            </div>
            <div class="mock-card">
                <div class="mock-badge">🏆</div>
                <div class="mock-info">
                    <div class="mock-name">Mock Test 2</div>
                    <div class="mock-desc">Advanced full-length practice exam simulation.</div>
                </div>
                <a href="javascript:void(0)" onclick="checkMockCode('PREFIXMOCK2', 'module_quiz.html?mock=2')" class="btn-mock">Take Mock</a>
            </div>
            <div class="mock-card">
                <div class="mock-badge">🏅</div>
                <div class="mock-info">
                    <div class="mock-name">Mock Test 3 — Full Simulation</div>
                    <div class="mock-desc">Final certification level assessment.</div>
                </div>
                <a href="javascript:void(0)" onclick="checkMockCode('PREFIXMOCK3', 'module_quiz.html?mock=3')" class="btn-mock">Take Mock</a>
            </div>
        </div>
    </div>
"""

sidebar_html = """
    <div class="sidebar">
        <div class="sidebar-card">
            <div class="sidebar-thumb" style="background: #1e293b; color: white; padding: 40px 20px; text-align: center;">
                <img src="pearson_python_badge_transparent.png" alt="Badge" style="max-width: 120px; margin-bottom: 15px;">
                <p style="font-weight: 700;">Professional Certification</p>
            </div>
            <div class="sidebar-body" style="padding: 20px;">
                <h4>Industry Recognized</h4>
                <p style="font-size: 0.85rem; color: #64748b;">Earn globally recognized certificates from Pearson IT Specialist and KVJ Analytics.</p>
                <button class="btn-cta" onclick="openCertModal()" style="width: 100%; margin-top: 15px;">View Sample Certificate</button>
            </div>
        </div>
    </div>
"""

modal_html = """
    <div id="mockCodeModal" style="display:none; position:fixed; top:0; left:0; width:100%; height:100%; background:rgba(15,23,42,0.6); backdrop-filter:blur(8px); z-index:10000; align-items:center; justify-content:center; padding:20px;">
        <div style="background:white; padding:40px; border-radius:24px; max-width:440px; width:100%; position:relative; text-align:center; box-shadow: 0 20px 25px -5px rgba(0, 0, 0, 0.1);">
            <h3 style="font-size:1.5rem; font-weight:800; color:#0f172a; margin-bottom:12px;">Access Restricted</h3>
            <p style="color:#64748b; font-size:0.95rem; margin-bottom:24px;">Complete all modules with 85%+ or enter an access code.</p>
            <div id="mockProgressNote" style="font-size: 0.8rem; color: #f59e0b; background: #fffbeb; padding: 10px; border-radius: 8px; margin-bottom: 20px; display: none; font-weight: 500;"></div>
            <input type="text" id="mockCodeInput" placeholder="Enter Access Code" style="width:100%; padding:14px 20px; border:2px solid #e2e8f0; border-radius:12px; font-size:1rem; font-weight:600; margin-bottom:12px; text-align:center;">
            <div id="mockCodeError" style="color:#ef4444; font-size:0.85rem; font-weight:600; margin-bottom:20px; display:none;">Invalid code.</div>
            <div style="display:grid; grid-template-columns:1fr 1fr; gap:12px;">
                <button onclick="closeMockModal()" style="padding:14px; background:#f8fafc; color:#64748b; border:none; border-radius:12px; font-weight:700; cursor:pointer;">Cancel</button>
                <button onclick="submitMockCode()" style="padding:14px; background:#ef4444; color:white; border:none; border-radius:12px; font-weight:700; cursor:pointer;">Unlock</button>
            </div>
        </div>
    </div>
"""

def heal_roadmap(path, prefix, code_prefix):
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    # If the file is truncated (ends with </body></html> but missing parts)
    # Let's find the closing tag of the module list
    # The file currently has modules M1-M6.
    
    # We'll split the file at the <script> tag
    script_start = content.find('<script>')
    head_part = content[:script_start]
    script_part = content[script_start:]

    # Final reconstruction
    # 1. Head part (Navbar, Hero, Modules)
    # 2. Mock Section
    # 3. Closing main </div> (the one that closes the left column)
    # 4. Sidebar
    # 5. Closing page-body </div>
    # 6. Modal
    # 7. Script
    
    # Let's try to find if we are missing the main closing divs
    # The modules were inside <div class="module-list"> inside <div class="modules-section">
    # Which was inside <div class="page-body"> (left column)
    
    m_section = mock_section_html.replace('PREFIX', code_prefix)
    
    # RECONSTRUCTED BODY
    # We'll assume head_part ends right after M6.
    # We need to close the modules-section, then the left column div.
    
    new_body = f"""
            </div> <!-- end of module-list -->
        </div> <!-- end of modules-section -->

        {m_section}
    </div> <!-- end of left column (page-body > div) -->

    {sidebar_html}
</div> <!-- end of page-body -->

{modal_html}
"""
    
    # Check if we already have these closing divs in head_part
    # To be safe, we'll just search for the end of the modules section.
    last_div = head_part.rfind('</div>')
    # Actually, let's just use the head_part as is if it ends with M6 actions.
    
    final_html = head_part + new_body + script_part
    
    # Ensure no duplicate scripts or corrupted ends
    final_html = final_html.replace('</body>\\n</html>', '').replace('</html>', '') + "\\n</body>\\n</html>"

    with open(path, 'w', encoding='utf-8') as f:
        f.write(final_html)
    print(f"Healed {path}")

heal_roadmap('c:/Users/kj anand/Downloads/Quiz DD/roadmap.html', '', 'PY')
heal_roadmap('c:/Users/kj anand/Downloads/Quiz DD/data_roadmap.html', 'data', 'DA')
