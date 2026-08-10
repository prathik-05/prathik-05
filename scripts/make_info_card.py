import os
from pathlib import Path

def make_info_card(output_svg_path):
    svg_w, svg_h = 490, 480
    
    rows_data = [
        ("OS", "Prathik-OS v2.6 (x86_64)", "#38BDF8", "https://github.com/prathik-05"),
        ("Role", "Software Engineer • AI Systems Developer", "#F8FAFC", "https://github.com/prathik-05"),
        ("College", "ACE Engineering College (CGPA: 8.50)", "#E2E8F0", "https://github.com/prathik-05"),
        ("Cert", "Oracle OCI 2025 Certified Generative AI Professional", "#A7F3D0", "https://education.oracle.com/"),
        ("Focus", "Multimodal RAG • Vision Pipelines • Data Analytics", "#38BDF8", "https://github.com/prathik-05/MCP-Powered-Video-RAG"),
        ("Stack", "Python, Java, SQL, PyTorch, Streamlit, RAG, MCP", "#F43F5E", "https://github.com/prathik-05/CognitoEDA"),
        ("Cloud", "Oracle Cloud (OCI), Google Cloud, Linux, Git", "#F59E0B", "https://github.com/prathik-05/yolov11-object-detection-and-segmentation"),
        ("Status", "Seeking SDE &amp; AI Opportunities (2027)", "#10B981", "https://www.linkedin.com/in/prathik-s07/")
    ]
    
    line_elements = []
    start_y = 65
    line_gap = 48
    duration = 2.5
    
    for i, (label, value, color, link_url) in enumerate(rows_data):
        y_pos = start_y + i * line_gap
        delay = (i / len(rows_data)) * duration
        val_clean = value.replace("&", "&amp;").replace("&amp;amp;", "&amp;")
        
        line_svg = f'''
        <g opacity="0">
          <animate attributeName="opacity" values="0;1" begin="{delay:.2f}s" dur="0.3s" fill="freeze"/>
          <text x="24" y="{y_pos}" fill="#38BDF8" font-family="monospace" font-size="12" font-weight="bold">{label.upper()}:</text>
          <a href="{link_url}" target="_blank">
            <text x="115" y="{y_pos}" fill="{color}" font-family="sans-serif" font-size="12" font-weight="500">{val_clean}</text>
          </a>
        </g>'''
        line_elements.append(line_svg)
        
    svg = f"""<svg width="{svg_w}" height="{svg_h}" viewBox="0 0 {svg_w} {svg_h}" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
  <rect width="{svg_w}" height="{svg_h}" rx="10" fill="#090D16" stroke="#1E293B" stroke-width="1"/>
  
  <!-- Neofetch Terminal Top Bar -->
  <rect width="{svg_w}" height="28" rx="10" fill="#0D1117"/>
  <circle cx="16" cy="14" r="4" fill="#FF5F56"/>
  <circle cx="30" cy="14" r="4" fill="#FFBD2E"/>
  <circle cx="44" cy="14" r="4" fill="#27C93F"/>
  <text x="{svg_w//2}" y="18" text-anchor="middle" fill="#64748B" font-family="monospace" font-size="11">neofetch --user prathik-05</text>

  <!-- Neofetch Content Rows -->
  <g transform="translate(0, 10)">
    {''.join(line_elements)}
  </g>

  <!-- Color Palette Chips at Bottom -->
  <g transform="translate(24, 435)">
    <rect x="0" width="30" height="14" rx="3" fill="#090D16"/>
    <rect x="36" width="30" height="14" rx="3" fill="#F43F5E"/>
    <rect x="72" width="30" height="14" rx="3" fill="#10B981"/>
    <rect x="108" width="30" height="14" rx="3" fill="#F59E0B"/>
    <rect x="144" width="30" height="14" rx="3" fill="#38BDF8"/>
    <rect x="180" width="30" height="14" rx="3" fill="#6366F1"/>
    <rect x="216" width="30" height="14" rx="3" fill="#A855F7"/>
    <rect x="252" width="30" height="14" rx="3" fill="#F8FAFC"/>
  </g>
</svg>"""

    with open(output_svg_path, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Updated info-card.svg generated at {output_svg_path}")

if __name__ == "__main__":
    make_info_card(Path("info-card.svg"))
