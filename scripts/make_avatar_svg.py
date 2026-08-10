import os
import base64
from PIL import Image

IMAGE_PATH = r"C:\Users\SVCS\Downloads\pic1.jpeg"
ASSETS_DIR = r"C:\Users\SVCS\.gemini\antigravity\scratch\prathik-05\assets"
os.makedirs(ASSETS_DIR, exist_ok=True)

# Read and encode pic1.jpeg to base64
with open(IMAGE_PATH, "rb") as f:
    img_b64 = base64.b64encode(f.read()).decode("utf-8")

# Create ultra-clean, high-definition animated avatar SVG (Vercel/Linear Cyber Neon Style)
avatar_svg = f"""<svg width="480" height="480" viewBox="0 0 480 480" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="480" height="480" rx="16" fill="#090D16" stroke="#1E293B" stroke-width="1"/>
  
  <!-- Subtle Background Glows -->
  <circle cx="240" cy="220" r="160" fill="#38BDF8" fill-opacity="0.08" filter="blur(60px)"/>
  <circle cx="240" cy="220" r="120" fill="#6366F1" fill-opacity="0.08" filter="blur(50px)"/>

  <!-- Rotating Animated Outer Ring -->
  <circle cx="240" cy="210" r="142" stroke="url(#ring_gradient)" stroke-width="3" stroke-dasharray="16 8">
    <animateTransform attributeName="transform" type="rotate" from="0 240 210" to="360 240 210" dur="12s" repeatCount="indefinite"/>
  </circle>

  <!-- Inner Glowing Ring -->
  <circle cx="240" cy="210" r="132" stroke="#38BDF8" stroke-opacity="0.5" stroke-width="1.5"/>

  <!-- Clip Path for Crystal Clear Photo -->
  <defs>
    <clipPath id="avatar-clip">
      <circle cx="240" cy="210" r="126"/>
    </clipPath>
    <linearGradient id="ring_gradient" x1="0" y1="0" x2="480" y2="480" gradientUnits="userSpaceOnUse">
      <stop stop-color="#38BDF8"/>
      <stop offset="0.5" stop-color="#6366F1"/>
      <stop offset="1" stop-color="#10B981"/>
    </linearGradient>
  </defs>

  <!-- High Definition Photo -->
  <image href="data:image/jpeg;base64,{img_b64}" x="114" y="84" width="252" height="252" preserveAspectRatio="xMidYMid slice" clip-path="url(#avatar-clip)"/>

  <!-- Name & Status Badge Overlay -->
  <g transform="translate(140, 370)">
    <rect width="200" height="38" rx="19" fill="#0D1117" stroke="#334155" stroke-width="1"/>
    <circle cx="22" cy="19" r="4.5" fill="#22C55E">
      <animate attributeName="opacity" values="1;0.4;1" dur="2s" repeatCount="indefinite"/>
    </circle>
    <text x="36" y="24" fill="#F8FAFC" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13" font-weight="700">Prathik Salla</text>
    <text x="122" y="24" fill="#38BDF8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="500">• AI Systems</text>
  </g>
</svg>"""

with open(os.path.join(ASSETS_DIR, "avatar-portrait.svg"), "w", encoding="utf-8") as f:
    f.write(avatar_svg)

print("Crystal-clear animated avatar SVG generated!")
