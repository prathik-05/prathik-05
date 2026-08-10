import os
import base64

IMAGE_PATH = r"C:\Users\SVCS\Downloads\pic1.jpeg"
ASSETS_DIR = r"C:\Users\SVCS\.gemini\antigravity\scratch\prathik-05\assets"
os.makedirs(ASSETS_DIR, exist_ok=True)

# Encode photo to base64
with open(IMAGE_PATH, "rb") as f:
    img_b64 = base64.b64encode(f.read()).decode("utf-8")

# Create Developer ID Card Banner with fine-tuned ponytail/head framing (xMidYMin slice)
id_card_svg = f"""<svg width="850" height="280" viewBox="0 0 850 280" fill="none" xmlns="http://www.w3.org/2000/svg">
  <!-- Card Background -->
  <rect width="850" height="280" rx="14" fill="#090D16" stroke="#1E293B" stroke-width="1.5"/>
  <rect width="850" height="3" rx="1.5" fill="url(#top_shimmer)"/>

  <!-- Shimmer Gradient Definition -->
  <defs>
    <linearGradient id="top_shimmer" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38BDF8" stop-opacity="0.3"/>
      <stop offset="50%" stop-color="#6366F1" stop-opacity="1">
        <animate attributeName="offset" values="0;1;0" dur="4s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" stop-color="#10B981" stop-opacity="0.3"/>
    </linearGradient>

    <clipPath id="photo_clip">
      <rect x="28" y="28" width="180" height="224" rx="8"/>
    </clipPath>
  </defs>

  <!-- Background Decorative Grid Lines -->
  <path d="M 0 70 H 850 M 0 140 H 850 M 0 210 H 850" stroke="#1E293B" stroke-opacity="0.2" stroke-width="1" stroke-dasharray="4 4"/>
  <path d="M 230 0 V 280 M 450 0 V 280 M 670 0 V 280" stroke="#1E293B" stroke-opacity="0.2" stroke-width="1" stroke-dasharray="4 4"/>

  <!-- LEFT SIDE: ID Photo Frame (Preserves Ponytail & Head Framing) -->
  <g>
    <!-- Photo Frame Outer Glow & Border -->
    <rect x="26" y="26" width="184" height="228" rx="10" fill="#0D1117" stroke="#38BDF8" stroke-width="1.5" stroke-opacity="0.8"/>
    
    <!-- Photo Image with xMidYMin framing to keep head & ponytail fully visible -->
    <image href="data:image/jpeg;base64,{img_b64}" x="28" y="28" width="180" height="224" preserveAspectRatio="xMidYMin slice" clip-path="url(#photo_clip)"/>
    
    <!-- VERIFIED DEVELOPER Overlay Pill -->
    <g transform="translate(42, 222)">
      <rect width="152" height="24" rx="12" fill="#090D16" fill-opacity="0.95" stroke="#38BDF8" stroke-width="1"/>
      <circle cx="14" cy="12" r="3.5" fill="#22C55E">
        <animate attributeName="opacity" values="1;0.3;1" dur="2s" repeatCount="indefinite"/>
      </circle>
      <text x="24" y="16" fill="#F8FAFC" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="10" font-weight="700" letter-spacing="0.5">VERIFIED DEVELOPER</text>
    </g>
  </g>

  <!-- RIGHT SIDE: Developer ID & PAN-Card Details -->
  <!-- Top Header / Card Title -->
  <text x="238" y="44" fill="#38BDF8" font-family="'Fira Code', monospace, sans-serif" font-size="11" font-weight="600" letter-spacing="1">DEV IDENTITY CARD • PRATHIK-05</text>
  <text x="238" y="74" fill="#F8FAFC" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="24" font-weight="800" letter-spacing="-0.5">PRATHIK SALLA</text>

  <!-- Horizontal Divider Line -->
  <line x1="238" y1="88" x2="818" y2="88" stroke="#1E293B" stroke-width="1"/>

  <!-- Field Group 1: Role & Education -->
  <g transform="translate(238, 102)">
    <text y="14" fill="#64748B" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="10" font-weight="600" letter-spacing="0.5">DEGREE / EDUCATION</text>
    <text y="32" fill="#E2E8F0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="13" font-weight="600">B.Tech in Computer Science (Data Science)</text>
    <text y="48" fill="#94A3B8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="12">ACE Engineering College • CGPA: 8.50 (2023–2027)</text>
  </g>

  <!-- Field Group 2: Specialization -->
  <g transform="translate(560, 102)">
    <text y="14" fill="#64748B" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="10" font-weight="600" letter-spacing="0.5">CORE SPECIALIZATION</text>
    <text y="32" fill="#38BDF8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="13" font-weight="600">AI Systems &amp; RAG Architecture</text>
    <text y="48" fill="#94A3B8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="12">Multimodal RAG • Vision • MCP</text>
  </g>

  <!-- Field Group 3: Certification -->
  <g transform="translate(238, 178)">
    <text y="14" fill="#64748B" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="10" font-weight="600" letter-spacing="0.5">KEY CREDENTIAL</text>
    <text y="32" fill="#A7F3D0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="13" font-weight="600">Oracle OCI Generative AI Certified Professional</text>
  </g>

  <!-- Field Group 4: Status Pill & Tech Badges -->
  <g transform="translate(238, 230)">
    <rect width="114" height="24" rx="12" fill="#0F172A" stroke="#334155" stroke-width="1"/>
    <circle cx="14" cy="12" r="3.5" fill="#22C55E">
      <animate attributeName="opacity" values="1;0.3;1" dur="2s" repeatCount="indefinite"/>
    </circle>
    <text x="24" y="16" fill="#E2E8F0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11" font-weight="500">Open to Roles</text>

    <!-- Mini Tech Chips -->
    <g transform="translate(130, 0)">
      <rect width="64" height="24" rx="4" fill="#1E293B"/>
      <text x="32" y="16" text-anchor="middle" fill="#38BDF8" font-family="sans-serif" font-size="11" font-weight="600">Python</text>
      
      <rect x="72" width="54" height="24" rx="4" fill="#1E293B"/>
      <text x="99" y="16" text-anchor="middle" fill="#F43F5E" font-family="sans-serif" font-size="11" font-weight="600">Java</text>
      
      <rect x="134" width="74" height="24" rx="4" fill="#1E293B"/>
      <text x="171" y="16" text-anchor="middle" fill="#10B981" font-family="sans-serif" font-size="11" font-weight="600">Streamlit</text>

      <rect x="216" width="70" height="24" rx="4" fill="#1E293B"/>
      <text x="251" y="16" text-anchor="middle" fill="#A855F7" font-family="sans-serif" font-size="11" font-weight="600">PyTorch</text>

      <rect x="294" width="50" height="24" rx="4" fill="#1E293B"/>
      <text x="319" y="16" text-anchor="middle" fill="#3B82F6" font-family="sans-serif" font-size="11" font-weight="600">MCP</text>
    </g>
  </g>
</svg>"""

with open(os.path.join(ASSETS_DIR, "id-card-banner.svg"), "w", encoding="utf-8") as f:
    f.write(id_card_svg)

print("ID card banner updated with top-aligned framing for ponytail photo!")
