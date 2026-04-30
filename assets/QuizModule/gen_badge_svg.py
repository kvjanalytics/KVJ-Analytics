import math

def create_pearson_badge_svg(filename, text_middle="PYTHON"):
    # Sampled Colors from pearson_badge.png
    color_dark = "#002e51"
    color_light_teal = "#64c2d6"
    color_mid_blue = "#0087b2"
    
    # Matching the specific color assignments in the original badge
    color_outer_dark = "#002e51"
    color_outer_teal = "#64c2d6"
    color_inner_ring = "#0b1c23" # sampled dark ring
    color_python_text = "#0087b2" # mid blue from sample
    
    svg = f"""<svg width="400" height="400" viewBox="0 0 400 400" xmlns="http://www.w3.org/2000/svg">
    <rect width="400" height="400" fill="none" />
    <circle cx="200" cy="200" r="160" fill="white" />
    
    <!-- Segmented Rings -->
    <g fill="none" stroke-width="15" stroke-linecap="round">
        <!-- Outer Ring -->
        <circle cx="200" cy="200" r="185" stroke="{color_outer_teal}" stroke-dasharray="140 140" stroke-dashoffset="40" />
        <circle cx="200" cy="200" r="185" stroke="{color_outer_dark}" stroke-dasharray="100 180" stroke-dashoffset="180" />
        
        <!-- Middle Ring -->
        <circle cx="200" cy="200" r="166" stroke="{color_outer_dark}" stroke-dasharray="180 80" stroke-dashoffset="20" />
        <circle cx="200" cy="200" r="166" stroke="{color_outer_teal}" stroke-dasharray="40 220" stroke-dashoffset="240" />
        
        <!-- Inner Ring -->
        <circle cx="200" cy="200" r="147" stroke="{color_inner_ring}" stroke-dasharray="120 100" stroke-dashoffset="80" />
        <circle cx="200" cy="200" r="147" stroke="{color_inner_ring}" stroke-dasharray="60 160" stroke-dashoffset="220" />
    </g>

    <!-- Text -->
    <text x="200" y="150" text-anchor="middle" font-family="Arial, sans-serif" font-weight="900" font-size="28" fill="{color_outer_dark}" style="letter-spacing: 1px;">IT SPECIALIST</text>
    <text x="200" y="215" text-anchor="middle" font-family="Arial, sans-serif" font-weight="950" font-size="48" fill="{color_python_text}" style="letter-spacing: 0.5px;">{text_middle}</text>
    
    <!-- Pearson Logo (Clean SVG path would be better but keeping it simple and accurate) -->
    <g transform="translate(142, 260) scale(0.65)">
        <circle cx="25" cy="25" r="23" fill="{color_python_text}" />
        <!-- Simplified P-mark logic -->
        <path d="M22 15 C26 15, 33 18, 33 25 C33 32, 26 35, 22 35 M30 25 L30 42" stroke="white" stroke-width="4.5" stroke-linecap="round" fill="none" />
        <text x="60" y="38" font-family="'Times New Roman', Georgia, serif" font-weight="600" font-size="28" fill="#1d1d1f">Pearson</text>
    </g>
</svg>
"""
    with open(filename, "w") as f:
        f.write(svg)

create_pearson_badge_svg("pearson_python_badge_circular.svg", "PYTHON")
print("Updated SVG with exact sampled colors.")
