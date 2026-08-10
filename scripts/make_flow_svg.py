import os

ASSETS_DIR = r"C:\Users\SVCS\.gemini\antigravity\scratch\prathik-05\assets"
os.makedirs(ASSETS_DIR, exist_ok=True)

# Animated AI Systems & RAG Flow Banner (Pure SVG, Zero JS, Vercel/Linear Aesthetic)
flow_svg = """<svg width="850" height="260" viewBox="0 0 850 260" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="850" height="260" rx="12" fill="#090D16" stroke="#1E293B" stroke-width="1"/>
  
  <!-- Subtle Gradient Glows -->
  <circle cx="150" cy="130" r="100" fill="#38BDF8" fill-opacity="0.05" filter="blur(50px)"/>
  <circle cx="700" cy="130" r="100" fill="#6366F1" fill-opacity="0.06" filter="blur(50px)"/>

  <!-- Top Accent Bar -->
  <rect width="850" height="2" rx="1" fill="url(#banner_grad)"/>
  <defs>
    <linearGradient id="banner_grad" x1="0" y1="0" x2="850" y2="0" gradientUnits="userSpaceOnUse">
      <stop stop-color="#38BDF8"/>
      <stop offset="0.5" stop-color="#6366F1"/>
      <stop offset="1" stop-color="#38BDF8"/>
    </linearGradient>
  </defs>

  <!-- Title & Badge -->
  <text x="36" y="44" fill="#F8FAFC" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="20" font-weight="700">AI SYSTEMS &amp; RAG ARCHITECTURE</text>
  <text x="36" y="66" fill="#94A3B8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="12" font-weight="500">Live Multimodal Data Pipeline &amp; Model Context Protocol (MCP)</text>
  
  <g transform="translate(685, 30)">
    <rect width="130" height="24" rx="12" fill="#0F172A" stroke="#334155" stroke-width="1"/>
    <circle cx="14" cy="12" r="3.5" fill="#22C55E">
      <animate attributeName="opacity" values="1;0.3;1" dur="2s" repeatCount="indefinite"/>
    </circle>
    <text x="24" y="16" fill="#38BDF8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11" font-weight="600">SYSTEM ONLINE</text>
  </g>

  <!-- Connecting Data Flow Lines -->
  <path d="M 160 150 L 290 150 M 390 150 L 510 150 M 610 150 L 710 150" stroke="#1E293B" stroke-width="3" stroke-dasharray="4 4"/>

  <!-- Animated Glowing Flow Particles -->
  <circle r="4" fill="#38BDF8">
    <animateMotion path="M 160 150 L 290 150" dur="2s" repeatCount="indefinite"/>
  </circle>
  <circle r="4" fill="#6366F1">
    <animateMotion path="M 390 150 L 510 150" dur="2.5s" repeatCount="indefinite"/>
  </circle>
  <circle r="4" fill="#10B981">
    <animateMotion path="M 610 150 L 710 150" dur="2.2s" repeatCount="indefinite"/>
  </circle>

  <!-- NODE 1: User / Input -->
  <g transform="translate(60, 110)">
    <rect width="100" height="80" rx="8" fill="#0D1117" stroke="#38BDF8" stroke-width="1.5"/>
    <text x="50" y="36" text-anchor="middle" fill="#F0F6FC" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="13" font-weight="600">Input Data</text>
    <text x="50" y="56" text-anchor="middle" fill="#8B949E" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11">Video / Text / CSV</text>
  </g>

  <!-- NODE 2: Vector Search / RAG -->
  <g transform="translate(290, 110)">
    <rect width="100" height="80" rx="8" fill="#0D1117" stroke="#6366F1" stroke-width="1.5"/>
    <text x="50" y="36" text-anchor="middle" fill="#F0F6FC" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="13" font-weight="600">RAG Engine</text>
    <text x="50" y="56" text-anchor="middle" fill="#8B949E" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11">Vector Embeddings</text>
  </g>

  <!-- NODE 3: MCP / Model Context Protocol -->
  <g transform="translate(510, 110)">
    <rect width="100" height="80" rx="8" fill="#0D1117" stroke="#8B5CF6" stroke-width="1.5"/>
    <text x="50" y="36" text-anchor="middle" fill="#F0F6FC" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="13" font-weight="600">MCP Protocol</text>
    <text x="50" y="56" text-anchor="middle" fill="#8B949E" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11">Tool Execution</text>
  </g>

  <!-- NODE 4: Multimodal Output -->
  <g transform="translate(710, 110)">
    <rect width="90" height="80" rx="8" fill="#0D1117" stroke="#10B981" stroke-width="1.5"/>
    <text x="45" y="36" text-anchor="middle" fill="#F0F6FC" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="13" font-weight="600">AI Output</text>
    <text x="45" y="56" text-anchor="middle" fill="#8B949E" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11">QA &amp; Analytics</text>
  </g>

  <!-- Footer Tag -->
  <text x="425" y="232" text-anchor="middle" fill="#64748B" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11">Designed &amp; Architected by Prathik Salla • Powered by RAG, YOLOv11 &amp; MCP</text>
</svg>"""

with open(os.path.join(ASSETS_DIR, "ai-systems-flow.svg"), "w", encoding="utf-8") as f:
    f.write(flow_svg)

print("AI Systems Flow SVG created successfully!")
