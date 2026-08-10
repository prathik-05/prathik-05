import os

ASSETS_DIR = r"C:\Users\SVCS\.gemini\antigravity\scratch\prathik-05\assets"
os.makedirs(ASSETS_DIR, exist_ok=True)

# 1. Animated Interactive Terminal Typing Banner
typing_banner = """<svg width="850" height="120" viewBox="0 0 850 120" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="850" height="120" rx="10" fill="#090D16" stroke="#1E293B" stroke-width="1"/>
  
  <!-- Terminal Top Bar -->
  <rect width="850" height="30" rx="10" fill="#0D1117"/>
  <rect y="20" width="850" height="10" fill="#0D1117"/>
  <circle cx="20" cy="15" r="5" fill="#FF5F56"/>
  <circle cx="36" cy="15" r="5" fill="#FFBD2E"/>
  <circle cx="52" cy="15" r="5" fill="#27C93F"/>
  <text x="425" y="19" text-anchor="middle" fill="#8B949E" font-family="'Fira Code', monospace, sans-serif" font-size="11">prathik-05@terminal ~ zsh</text>

  <!-- Animated Typing Text Line 1 -->
  <g transform="translate(24, 62)">
    <text fill="#38BDF8" font-family="'Fira Code', monospace, sans-serif" font-size="14" font-weight="600">❯ prathik-05 --init-system</text>
  </g>

  <!-- Animated Typing Text Line 2 -->
  <g transform="translate(24, 90)">
    <text fill="#A7F3D0" font-family="'Fira Code', monospace, sans-serif" font-size="13" font-weight="500">
      [OK] Loaded RAG, Vision &amp; MCP Modules
      <animate attributeName="opacity" values="0;0;1;1" keyTimes="0;0.3;0.35;1" dur="4s" repeatCount="indefinite"/>
    </text>
    <text x="315" fill="#38BDF8" font-family="'Fira Code', monospace, sans-serif" font-size="13" font-weight="500">
      | Ready to Build 🚀
      <animate attributeName="opacity" values="0;0;1;1" keyTimes="0;0.6;0.65;1" dur="4s" repeatCount="indefinite"/>
    </text>

    <!-- Blinking Cursor -->
    <rect x="475" y="-12" width="8" height="15" fill="#38BDF8">
      <animate attributeName="opacity" values="1;0;1" dur="0.8s" repeatCount="indefinite"/>
    </rect>
  </g>
</svg>"""

with open(os.path.join(ASSETS_DIR, "typing-banner.svg"), "w", encoding="utf-8") as f:
    f.write(typing_banner)


# 2. Animated Tech Stack Infinite Scrolling Marquee
marquee_svg = """<svg width="850" height="60" viewBox="0 0 850 60" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="850" height="60" rx="8" fill="#0D1117" stroke="#161B22" stroke-width="1"/>
  
  <g>
    <!-- Infinite Sliding Animation Track -->
    <animateTransform attributeName="transform" type="translate" from="0 0" to="-500 0" dur="12s" repeatCount="indefinite"/>
    
    <!-- Track Set 1 -->
    <g transform="translate(20, 18)">
      <rect width="90" height="26" rx="13" fill="#1E293B"/><text x="45" y="17" text-anchor="middle" fill="#38BDF8" font-family="sans-serif" font-size="12" font-weight="600">Python</text>
      <rect x="100" width="80" height="26" rx="13" fill="#1E293B"/><text x="140" y="17" text-anchor="middle" fill="#F43F5E" font-family="sans-serif" font-size="12" font-weight="600">Java</text>
      <rect x="190" width="90" height="26" rx="13" fill="#1E293B"/><text x="235" y="17" text-anchor="middle" fill="#A855F7" font-family="sans-serif" font-size="12" font-weight="600">PyTorch</text>
      <rect x="290" width="100" height="26" rx="13" fill="#1E293B"/><text x="340" y="17" text-anchor="middle" fill="#10B981" font-family="sans-serif" font-size="12" font-weight="600">Streamlit</text>
      <rect x="400" width="80" height="26" rx="13" fill="#1E293B"/><text x="440" y="17" text-anchor="middle" fill="#F59E0B" font-family="sans-serif" font-size="12" font-weight="600">OpenCV</text>
      <rect x="490" width="70" height="26" rx="13" fill="#1E293B"/><text x="525" y="17" text-anchor="middle" fill="#3B82F6" font-family="sans-serif" font-size="12" font-weight="600">RAG</text>
      <rect x="570" width="70" height="26" rx="13" fill="#1E293B"/><text x="605" y="17" text-anchor="middle" fill="#EC4899" font-family="sans-serif" font-size="12" font-weight="600">MCP</text>
      <rect x="650" width="110" height="26" rx="13" fill="#1E293B"/><text x="705" y="17" text-anchor="middle" fill="#38BDF8" font-family="sans-serif" font-size="12" font-weight="600">Oracle OCI</text>
    </g>

    <!-- Track Set 2 (Duplicate for Seamless Loop) -->
    <g transform="translate(780, 18)">
      <rect width="90" height="26" rx="13" fill="#1E293B"/><text x="45" y="17" text-anchor="middle" fill="#38BDF8" font-family="sans-serif" font-size="12" font-weight="600">Python</text>
      <rect x="100" width="80" height="26" rx="13" fill="#1E293B"/><text x="140" y="17" text-anchor="middle" fill="#F43F5E" font-family="sans-serif" font-size="12" font-weight="600">Java</text>
      <rect x="190" width="90" height="26" rx="13" fill="#1E293B"/><text x="235" y="17" text-anchor="middle" fill="#A855F7" font-family="sans-serif" font-size="12" font-weight="600">PyTorch</text>
      <rect x="290" width="100" height="26" rx="13" fill="#1E293B"/><text x="340" y="17" text-anchor="middle" fill="#10B981" font-family="sans-serif" font-size="12" font-weight="600">Streamlit</text>
      <rect x="400" width="80" height="26" rx="13" fill="#1E293B"/><text x="440" y="17" text-anchor="middle" fill="#F59E0B" font-family="sans-serif" font-size="12" font-weight="600">OpenCV</text>
      <rect x="490" width="70" height="26" rx="13" fill="#1E293B"/><text x="525" y="17" text-anchor="middle" fill="#3B82F6" font-family="sans-serif" font-size="12" font-weight="600">RAG</text>
      <rect x="570" width="70" height="26" rx="13" fill="#1E293B"/><text x="605" y="17" text-anchor="middle" fill="#EC4899" font-family="sans-serif" font-size="12" font-weight="600">MCP</text>
      <rect x="650" width="110" height="26" rx="13" fill="#1E293B"/><text x="705" y="17" text-anchor="middle" fill="#38BDF8" font-family="sans-serif" font-size="12" font-weight="600">Oracle OCI</text>
    </g>
  </g>
</svg>"""

with open(os.path.join(ASSETS_DIR, "tech-marquee.svg"), "w", encoding="utf-8") as f:
    f.write(marquee_svg)

print("Typing banner and Tech Marquee SVGs created successfully!")
