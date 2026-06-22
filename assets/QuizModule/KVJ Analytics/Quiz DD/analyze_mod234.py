import re

# Look at Module 2, 3, 4 headings and structure
for mod_num in [2, 3, 4]:
    fname = f'Module-{mod_num}.html'
    with open(fname, 'r', encoding='utf-8') as f:
        content = f.read()
    headings = re.findall(r'<h[1-4][^>]*>(.*?)</h[1-4]>', content, re.DOTALL)
    print(f"=== Module {mod_num} Headings ===")
    for h in headings:
        clean = re.sub(r'<[^>]+>', '', h).strip()
        if clean:
            print(f"  {clean[:120]}")
    print()
    
    # Check for code blocks
    code_blocks = re.findall(r'<pre[^>]*>.*?</pre>', content, re.DOTALL)
    print(f"  Code blocks: {len(code_blocks)}")
    
    # Check for practice/mission sections
    missions = len(re.findall(r'mission|practice|Practice|Mission', content))
    print(f"  Mission/Practice mentions: {missions}")
    print()
