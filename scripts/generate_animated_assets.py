import os

ASSETS_DIR = r"C:\Users\SVCS\.gemini\antigravity\scratch\prathik-05\assets"
os.makedirs(ASSETS_DIR, exist_ok=True)

# 1. Animated Tech Stack Infinite Scrolling Marquee
# Exact badges: Python, Java, SQL, PyTorch, Streamlit, RAG, MCP, OCI
marquee_svg = """<svg width="850" height="60" viewBox="0 0 850 60" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="850" height="60" rx="8" fill="#0D1117" stroke="#161B22" stroke-width="1"/>
  
  <g>
    <!-- Infinite Sliding Animation Track -->
    <animateTransform attributeName="transform" type="translate" from="0 0" to="-660 0" dur="14s" repeatCount="indefinite"/>
    
    <!-- Unique Track Set 1 -->
    <g transform="translate(20, 18)">
      <rect width="85" height="26" rx="13" fill="#1E293B"/><text x="42" y="17" text-anchor="middle" fill="#38BDF8" font-family="sans-serif" font-size="12" font-weight="600">Python</text>
      <rect x="95" width="75" height="26" rx="13" fill="#1E293B"/><text x="132" y="17" text-anchor="middle" fill="#F43F5E" font-family="sans-serif" font-size="12" font-weight="600">Java</text>
      <rect x="180" width="70" height="26" rx="13" fill="#1E293B"/><text x="215" y="17" text-anchor="middle" fill="#F59E0B" font-family="sans-serif" font-size="12" font-weight="600">SQL</text>
      <rect x="260" width="85" height="26" rx="13" fill="#1E293B"/><text x="302" y="17" text-anchor="middle" fill="#A855F7" font-family="sans-serif" font-size="12" font-weight="600">PyTorch</text>
      <rect x="355" width="95" height="26" rx="13" fill="#1E293B"/><text x="402" y="17" text-anchor="middle" fill="#10B981" font-family="sans-serif" font-size="12" font-weight="600">Streamlit</text>
      <rect x="460" width="65" height="26" rx="13" fill="#1E293B"/><text x="492" y="17" text-anchor="middle" fill="#3B82F6" font-family="sans-serif" font-size="12" font-weight="600">RAG</text>
      <rect x="535" width="65" height="26" rx="13" fill="#1E293B"/><text x="567" y="17" text-anchor="middle" fill="#EC4899" font-family="sans-serif" font-size="12" font-weight="600">MCP</text>
      <rect x="610" width="65" height="26" rx="13" fill="#1E293B"/><text x="642" y="17" text-anchor="middle" fill="#38BDF8" font-family="sans-serif" font-size="12" font-weight="600">OCI</text>
    </g>

    <!-- Unique Track Set 2 (Seamless Duplicate Loop) -->
    <g transform="translate(680, 18)">
      <rect width="85" height="26" rx="13" fill="#1E293B"/><text x="42" y="17" text-anchor="middle" fill="#38BDF8" font-family="sans-serif" font-size="12" font-weight="600">Python</text>
      <rect x="95" width="75" height="26" rx="13" fill="#1E293B"/><text x="132" y="17" text-anchor="middle" fill="#F43F5E" font-family="sans-serif" font-size="12" font-weight="600">Java</text>
      <rect x="180" width="70" height="26" rx="13" fill="#1E293B"/><text x="215" y="17" text-anchor="middle" fill="#F59E0B" font-family="sans-serif" font-size="12" font-weight="600">SQL</text>
      <rect x="260" width="85" height="26" rx="13" fill="#1E293B"/><text x="302" y="17" text-anchor="middle" fill="#A855F7" font-family="sans-serif" font-size="12" font-weight="600">PyTorch</text>
      <rect x="355" width="95" height="26" rx="13" fill="#1E293B"/><text x="402" y="17" text-anchor="middle" fill="#10B981" font-family="sans-serif" font-size="12" font-weight="600">Streamlit</text>
      <rect x="460" width="65" height="26" rx="13" fill="#1E293B"/><text x="492" y="17" text-anchor="middle" fill="#3B82F6" font-family="sans-serif" font-size="12" font-weight="600">RAG</text>
      <rect x="535" width="65" height="26" rx="13" fill="#1E293B"/><text x="567" y="17" text-anchor="middle" fill="#EC4899" font-family="sans-serif" font-size="12" font-weight="600">MCP</text>
      <rect x="610" width="65" height="26" rx="13" fill="#1E293B"/><text x="642" y="17" text-anchor="middle" fill="#38BDF8" font-family="sans-serif" font-size="12" font-weight="600">OCI</text>
    </g>
  </g>
</svg>"""

with open(os.path.join(ASSETS_DIR, "tech-marquee.svg"), "w", encoding="utf-8") as f:
    f.write(marquee_svg)

print("Updated marquee SVG (Python, Java, SQL, PyTorch, Streamlit, RAG, MCP, OCI) generated!")
