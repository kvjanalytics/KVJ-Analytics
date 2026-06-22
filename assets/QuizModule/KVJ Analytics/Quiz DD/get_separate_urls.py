import base64

def get_b64_svg(content):
    return f"data:image/svg+xml;base64,{base64.b64encode(content.encode('utf-8')).decode('utf-8')}"

# Option A: Column Chart
svg_a = """<svg width="300" height="200" viewBox="0 0 300 200" xmlns="http://www.w3.org/2000/svg">
    <rect width="300" height="200" fill="#f8fafc" rx="8"/>
    <line x1="40" y1="160" x2="260" y2="160" stroke="#475569" stroke-width="2"/>
    <line x1="40" y1="30" x2="40" y2="160" stroke="#475569" stroke-width="2"/>
    <rect x="60" y="110" width="20" height="50" fill="#4472c4"/>
    <rect x="100" y="60" width="20" height="100" fill="#4472c4"/>
    <rect x="140" y="90" width="20" height="70" fill="#4472c4"/>
    <rect x="180" y="50" width="20" height="110" fill="#4472c4"/>
    <rect x="220" y="80" width="20" height="80" fill="#4472c4"/>
</svg>"""

# Option B: Bar Chart
svg_b = """<svg width="300" height="200" viewBox="0 0 300 200" xmlns="http://www.w3.org/2000/svg">
    <rect width="300" height="200" fill="#f8fafc" rx="8"/>
    <line x1="50" y1="170" x2="270" y2="170" stroke="#475569" stroke-width="2"/>
    <line x1="50" y1="30" x2="50" y2="170" stroke="#475569" stroke-width="2"/>
    <rect x="50" y="50" width="180" height="15" fill="#4472c4"/>
    <rect x="50" y="80" width="120" height="15" fill="#4472c4"/>
    <rect x="50" y="110" width="200" height="15" fill="#4472c4"/>
    <rect x="50" y="140" width="150" height="15" fill="#4472c4"/>
</svg>"""

# Option C: Histogram
svg_c = """<svg width="300" height="200" viewBox="0 0 300 200" xmlns="http://www.w3.org/2000/svg">
    <rect width="300" height="200" fill="#f8fafc" rx="8"/>
    <line x1="40" y1="160" x2="260" y2="160" stroke="#475569" stroke-width="2"/>
    <line x1="40" y1="30" x2="40" y2="160" stroke="#475569" stroke-width="2"/>
    <rect x="60" y="70" width="40" height="90" fill="#4472c4" stroke="#ffffff" stroke-width="1"/>
    <rect x="100" y="110" width="40" height="50" fill="#4472c4" stroke="#ffffff" stroke-width="1"/>
    <rect x="140" y="90" width="40" height="70" fill="#4472c4" stroke="#ffffff" stroke-width="1"/>
    <rect x="180" y="130" width="40" height="30" fill="#4472c4" stroke="#ffffff" stroke-width="1"/>
    <text x="150" y="180" text-anchor="middle" font-family="sans-serif" font-size="10" fill="#64748b">Continuous Bins</text>
</svg>"""

# Option D: Line Chart
svg_d = """<svg width="300" height="200" viewBox="0 0 300 200" xmlns="http://www.w3.org/2000/svg">
    <rect width="300" height="200" fill="#f8fafc" rx="8"/>
    <line x1="40" y1="160" x2="260" y2="160" stroke="#475569" stroke-width="2"/>
    <line x1="40" y1="30" x2="40" y2="160" stroke="#475569" stroke-width="2"/>
    <polyline points="60,130 100,80 140,110 180,50 220,70 240,30" fill="none" stroke="#4472c4" stroke-width="2"/>
    <circle cx="60" cy="130" r="3" fill="#1e3a5f" />
    <circle cx="100" cy="80" r="3" fill="#1e3a5f" />
    <circle cx="140" cy="110" r="3" fill="#1e3a5f" />
    <circle cx="180" cy="50" r="3" fill="#1e3a5f" />
    <circle cx="220" cy="70" r="3" fill="#1e3a5f" />
    <circle cx="240" cy="30" r="3" fill="#1e3a5f" />
</svg>"""

print("OPTION_A:", get_b64_svg(svg_a))
print("OPTION_B:", get_b64_svg(svg_b))
print("OPTION_C:", get_b64_svg(svg_c))
print("OPTION_D:", get_b64_svg(svg_d))
