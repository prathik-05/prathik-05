import os
from pathlib import Path

OUTPUT_SVG = Path("assets/neural-radar-status.svg")
OUTPUT_SVG.parent.mkdir(exist_ok=True)

def generate_neural_radar():
    svg_w, svg_h = 860, 95
    
    svg = f"""<svg width="{svg_w}" height="{svg_h}" viewBox="0 0 {svg_w} {svg_h}" fill="none" xmlns="http://www.w3.org/2000/svg">
  <!-- Glassmorphism Card Frame -->
  <rect width="{svg_w}" height="{svg_h}" rx="10" fill="#090D16" stroke="#1E293B" stroke-width="1"/>
  
  <!-- Subtle Matrix Grid Pattern -->
  <defs>
    <pattern id="grid" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#1E293B" stroke-width="0.5" opacity="0.6"/>
    </pattern>
    
    <!-- Neon Linear Gradients -->
    <linearGradient id="cyan-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38BDF8" stop-opacity="0.9"/>
      <stop offset="100%" stop-color="#818CF8" stop-opacity="0.9"/>
    </linearGradient>
    
    <linearGradient id="sweep-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#38BDF8" stop-opacity="0.4"/>
      <stop offset="100%" stop-color="#38BDF8" stop-opacity="0.0"/>
    </linearGradient>

    <radialGradient id="radar-glow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#38BDF8" stop-opacity="0.3"/>
      <stop offset="100%" stop-color="#38BDF8" stop-opacity="0"/>
    </radialGradient>
  </defs>

  <rect width="{svg_w}" height="{svg_h}" fill="url(#grid)" rx="10"/>

  <!-- Left: Cyber Radar Scope Assembly (x=55, y=47, r=32) -->
  <g transform="translate(55, 47)">
    <circle r="36" fill="url(#radar-glow)"/>
    <circle r="32" fill="none" stroke="#1E293B" stroke-width="1"/>
    <circle r="22" fill="none" stroke="#334155" stroke-width="1" stroke-dasharray="3 3"/>
    <circle r="12" fill="none" stroke="#38BDF8" stroke-width="1" opacity="0.5"/>
    <circle r="3" fill="#38BDF8"/>

    <!-- Rotating Radar Sweep Beam -->
    <path d="M 0 0 L 32 0 A 32 32 0 0 0 0 -32 Z" fill="url(#sweep-grad)">
      <animateTransform attributeName="transform" type="rotate" from="0" to="360" dur="3s" repeatCount="indefinite"/>
    </path>

    <!-- Radar Ping Blips with Pulsing Expand -->
    <circle cx="15" cy="-12" r="3" fill="#10B981">
      <animate attributeName="opacity" values="0.2;1;0.2" dur="1.5s" repeatCount="indefinite"/>
    </circle>
    <circle cx="-18" cy="14" r="2.5" fill="#38BDF8">
      <animate attributeName="opacity" values="1;0.2;1" dur="2s" repeatCount="indefinite"/>
    </circle>
    <circle cx="10" cy="20" r="2" fill="#F43F5E">
      <animate attributeName="opacity" values="0.3;1;0.3" dur="1.8s" repeatCount="indefinite"/>
    </circle>
  </g>

  <!-- Middle: Animated System Status Monitor -->
  <g transform="translate(110, 0)">
    <!-- Header Badge -->
    <rect x="0" y="16" width="220" height="20" rx="4" fill="#0D1117" stroke="#334155" stroke-width="1"/>
    <circle cx="10" cy="26" r="3.5" fill="#10B981">
      <animate attributeName="opacity" values="1;0.3;1" dur="1s" repeatCount="indefinite"/>
    </circle>
    <text x="20" y="30" fill="#38BDF8" font-family="monospace" font-size="10" font-weight="700">SYSTEM_STATUS • ONLINE</text>

    <!-- Pulsing Terminal Metrics -->
    <text x="0" y="54" fill="#F8FAFC" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="13" font-weight="600">
      Prathik Salla <tspan fill="#64748B">|</tspan> <tspan fill="#38BDF8">AI Systems &amp; Software Engineering</tspan>
    </text>
    
    <text x="0" y="74" fill="#94A3B8" font-family="monospace" font-size="11">
      &gt; PIPELINES: <tspan fill="#10B981">MCP_RAG</tspan> • <tspan fill="#F59E0B">YOLOv11_VISION</tspan> • <tspan fill="#818CF8">COGNITO_EDA</tspan>
    </text>
  </g>

  <!-- Right: Real-time Audio/Data Pulse Waves & Live Latency Indicator -->
  <g transform="translate(680, 22)">
    <rect x="0" y="0" width="155" height="52" rx="6" fill="#0D1117" stroke="#1E293B" stroke-width="1"/>
    <text x="12" y="18" fill="#64748B" font-family="monospace" font-size="9" font-weight="600">INFERENCE LATENCY</text>
    <text x="12" y="38" fill="#10B981" font-family="monospace" font-size="14" font-weight="700">12ms <tspan fill="#38BDF8" font-size="10">[OPTIMAL]</tspan></text>

    <!-- Animated Equalizer Signal Wave Bars -->
    <g transform="translate(108, 14)">
      <rect x="0" y="10" width="3" height="15" rx="1.5" fill="#38BDF8">
        <animate attributeName="height" values="8;22;12;24;8" dur="1.2s" repeatCount="indefinite"/>
        <animate attributeName="y" values="12;2;10;0;12" dur="1.2s" repeatCount="indefinite"/>
      </rect>
      <rect x="6" y="5" width="3" height="20" rx="1.5" fill="#10B981">
        <animate attributeName="height" values="18;6;22;10;18" dur="0.9s" repeatCount="indefinite"/>
        <animate attributeName="y" values="4;14;2;12;4" dur="0.9s" repeatCount="indefinite"/>
      </rect>
      <rect x="12" y="12" width="3" height="12" rx="1.5" fill="#F43F5E">
        <animate attributeName="height" values="10;24;8;20;10" dur="1.4s" repeatCount="indefinite"/>
        <animate attributeName="y" values="10;0;12;2;10" dur="1.4s" repeatCount="indefinite"/>
      </rect>
      <rect x="18" y="8" width="3" height="18" rx="1.5" fill="#F59E0B">
        <animate attributeName="height" values="22;10;18;6;22" dur="1.1s" repeatCount="indefinite"/>
        <animate attributeName="y" values="2;12;4;14;2" dur="1.1s" repeatCount="indefinite"/>
      </rect>
    </g>
  </g>
</svg>"""

    with open(OUTPUT_SVG, "w", encoding="utf-8") as f:
        f.write(svg)
    print(f"Neural Radar System Status SVG generated at {OUTPUT_SVG}")

if __name__ == "__main__":
    generate_neural_radar()
