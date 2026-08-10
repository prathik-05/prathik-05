import os

ASSETS_DIR = r"C:\Users\SVCS\.gemini\antigravity\scratch\prathik-05\assets"
os.makedirs(ASSETS_DIR, exist_ok=True)

# 1. Animated Tech Stack Infinite Scrolling Marquee (Clean Unique Badges)
# Set 1 & Set 2 contain exact 8 unique badges: Python, Java, PyTorch, Streamlit, OpenCV, RAG, MCP, Oracle OCI
marquee_svg = """<svg width="850" height="60" viewBox="0 0 850 60" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="850" height="60" rx="8" fill="#0D1117" stroke="#161B22" stroke-width="1"/>
  
  <g>
    <!-- Infinite Sliding Animation Track -->
    <animateTransform attributeName="transform" type="translate" from="0 0" to="-730 0" dur="14s" repeatCount="indefinite"/>
    
    <!-- Unique Track Set 1 -->
    <g transform="translate(20, 18)">
      <rect width="85" height="26" rx="13" fill="#1E293B"/><text x="42" y="17" text-anchor="middle" fill="#38BDF8" font-family="sans-serif" font-size="12" font-weight="600">Python</text>
      <rect x="95" width="75" height="26" rx="13" fill="#1E293B"/><text x="132" y="17" text-anchor="middle" fill="#F43F5E" font-family="sans-serif" font-size="12" font-weight="600">Java</text>
      <rect x="180" width="85" height="26" rx="13" fill="#1E293B"/><text x="222" y="17" text-anchor="middle" fill="#A855F7" font-family="sans-serif" font-size="12" font-weight="600">PyTorch</text>
      <rect x="275" width="95" height="26" rx="13" fill="#1E293B"/><text x="322" y="17" text-anchor="middle" fill="#10B981" font-family="sans-serif" font-size="12" font-weight="600">Streamlit</text>
      <rect x="380" width="85" height="26" rx="13" fill="#1E293B"/><text x="422" y="17" text-anchor="middle" fill="#F59E0B" font-family="sans-serif" font-size="12" font-weight="600">OpenCV</text>
      <rect x="475" width="65" height="26" rx="13" fill="#1E293B"/><text x="507" y="17" text-anchor="middle" fill="#3B82F6" font-family="sans-serif" font-size="12" font-weight="600">RAG</text>
      <rect x="550" width="65" height="26" rx="13" fill="#1E293B"/><text x="582" y="17" text-anchor="middle" fill="#EC4899" font-family="sans-serif" font-size="12" font-weight="600">MCP</text>
      <rect x="625" width="105" height="26" rx="13" fill="#1E293B"/><text x="677" y="17" text-anchor="middle" fill="#38BDF8" font-family="sans-serif" font-size="12" font-weight="600">Oracle OCI</text>
    </g>

    <!-- Unique Track Set 2 (Seamless Duplicate Loop) -->
    <g transform="translate(750, 18)">
      <rect width="85" height="26" rx="13" fill="#1E293B"/><text x="42" y="17" text-anchor="middle" fill="#38BDF8" font-family="sans-serif" font-size="12" font-weight="600">Python</text>
      <rect x="95" width="75" height="26" rx="13" fill="#1E293B"/><text x="132" y="17" text-anchor="middle" fill="#F43F5E" font-family="sans-serif" font-size="12" font-weight="600">Java</text>
      <rect x="180" width="85" height="26" rx="13" fill="#1E293B"/><text x="222" y="17" text-anchor="middle" fill="#A855F7" font-family="sans-serif" font-size="12" font-weight="600">PyTorch</text>
      <rect x="275" width="95" height="26" rx="13" fill="#1E293B"/><text x="322" y="17" text-anchor="middle" fill="#10B981" font-family="sans-serif" font-size="12" font-weight="600">Streamlit</text>
      <rect x="380" width="85" height="26" rx="13" fill="#1E293B"/><text x="422" y="17" text-anchor="middle" fill="#F59E0B" font-family="sans-serif" font-size="12" font-weight="600">OpenCV</text>
      <rect x="475" width="65" height="26" rx="13" fill="#1E293B"/><text x="507" y="17" text-anchor="middle" fill="#3B82F6" font-family="sans-serif" font-size="12" font-weight="600">RAG</text>
      <rect x="550" width="65" height="26" rx="13" fill="#1E293B"/><text x="582" y="17" text-anchor="middle" fill="#EC4899" font-family="sans-serif" font-size="12" font-weight="600">MCP</text>
      <rect x="625" width="105" height="26" rx="13" fill="#1E293B"/><text x="677" y="17" text-anchor="middle" fill="#38BDF8" font-family="sans-serif" font-size="12" font-weight="600">Oracle OCI</text>
    </g>
  </g>
</svg>"""

with open(os.path.join(ASSETS_DIR, "tech-marquee.svg"), "w", encoding="utf-8") as f:
    f.write(marquee_svg)

print("Unique, deduplicated tech marquee SVG generated!")
