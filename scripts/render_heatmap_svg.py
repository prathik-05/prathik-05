import json
from pathlib import Path

JSON_PATH = Path("data/contributions.json")
OUTPUT_SVG = Path("contrib-heatmap.svg")

# GitHub Dark Theme Green Palette
PALETTE = ["#161B22", "#0E4429", "#006D32", "#26A641", "#39D353", "#69F0A0"]

def render_heatmap_svg():
    if not JSON_PATH.exists():
        from fetch_contributions import fetch_contributions
        fetch_contributions()
        
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    days = data.get("days", [])
    
    # 53 weeks x 7 days grid
    box_size = 11
    box_gap = 4
    start_x = 40
    start_y = 45
    
    svg_w = start_x + (53 * (box_size + box_gap)) + 20
    svg_h = start_y + (7 * (box_size + box_gap)) + 45
    
    rect_elements = []
    total_days = len(days)
    
    for i, day in enumerate(days):
        week = i // 7
        weekday = i % 7
        
        if week >= 53:
            break
            
        x = start_x + week * (box_size + box_gap)
        y = start_y + weekday * (box_size + box_gap)
        
        level = min(day.get("level", 0), 5)
        color = PALETTE[level]
        
        # Diagonal reveal animation
        delay = (week + weekday) * 0.02
        
        rect_elements.append(
            f'<rect x="{x}" y="{y}" width="{box_size}" height="{box_size}" rx="2" fill="{color}" opacity="0">\n'
            f'  <animate attributeName="opacity" values="0;1" begin="{delay:.2f}s" dur="0.2s" fill="freeze"/>\n'
            f'</rect>'
        )
        
    # Month labels
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    month_labels = []
    for m_idx, m_name in enumerate(months):
        m_x = start_x + int(m_idx * 4.3 * (box_size + box_gap))
        month_labels.append(f'<text x="{m_x}" y="32" fill="#8B949E" font-family="sans-serif" font-size="10">{m_name}</text>')
        
    # Weekday labels
    weekday_labels = [
        f'<text x="15" y="{start_y + 1 * (box_size + box_gap) + 9}" fill="#8B949E" font-family="sans-serif" font-size="9">Mon</text>',
        f'<text x="15" y="{start_y + 3 * (box_size + box_gap) + 9}" fill="#8B949E" font-family="sans-serif" font-size="9">Wed</text>',
        f'<text x="15" y="{start_y + 5 * (box_size + box_gap) + 9}" fill="#8B949E" font-family="sans-serif" font-size="9">Fri</text>'
    ]
    
    svg = f"""<svg width="{svg_w}" height="{svg_h}" viewBox="0 0 {svg_w} {svg_h}" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="{svg_w}" height="{svg_h}" rx="10" fill="#090D16" stroke="#1E293B" stroke-width="1"/>
  
  <!-- Header Title -->
  <text x="20" y="24" fill="#38BDF8" font-family="'Fira Code', monospace" font-size="11" font-weight="600">LIVE CONTRIBUTION HEATMAP • @PRATHIK-05</text>

  <!-- Month & Day Labels -->
  {''.join(month_labels)}
  {''.join(weekday_labels)}

  <!-- Heatmap Boxes -->
  {''.join(rect_elements)}

  <!-- Legend at Bottom -->
  <g transform="translate({svg_w - 170}, {svg_h - 22})">
    <text x="-32" y="10" fill="#8B949E" font-family="sans-serif" font-size="9">Less</text>
    <rect x="0" y="0" width="10" height="10" rx="2" fill="{PALETTE[0]}"/>
    <rect x="14" y="0" width="10" height="10" rx="2" fill="{PALETTE[1]}"/>
    <rect x="28" y="0" width="10" height="10" rx="2" fill="{PALETTE[2]}"/>
    <rect x="42" y="0" width="10" height="10" rx="2" fill="{PALETTE[3]}"/>
    <rect x="56" y="0" width="10" height="10" rx="2" fill="{PALETTE[4]}"/>
    <rect x="70" y="0" width="10" height="10" rx="2" fill="{PALETTE[5]}"/>
    <text x="88" y="10" fill="#8B949E" font-family="sans-serif" font-size="9">More</text>
  </g>
</svg>"""

    with open(OUTPUT_SVG, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Contribution Heatmap SVG generated at {OUTPUT_SVG}")

if __name__ == "__main__":
    render_heatmap_svg()
