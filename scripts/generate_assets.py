import os

ASSETS_DIR = r"C:\Users\SVCS\.gemini\antigravity\scratch\prathik-05\assets"
os.makedirs(ASSETS_DIR, exist_ok=True)

# 1. Profile Header SVG (Vercel/Linear Design + Shimmer & Pulse Animation)
header_svg = """<svg width="850" height="130" viewBox="0 0 850 130" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="850" height="130" rx="10" fill="#090D16" stroke="#1E293B" stroke-width="1"/>
  
  <!-- Subtle Background Glow Expansion -->
  <circle cx="100" cy="65" r="80" fill="#38BDF8" fill-opacity="0.06" filter="blur(40px)">
    <animate attributeName="r" values="80;100;80" dur="6s" repeatCount="indefinite"/>
  </circle>
  <circle cx="750" cy="65" r="80" fill="#6366F1" fill-opacity="0.06" filter="blur(40px)">
    <animate attributeName="r" values="80;100;80" dur="6s" repeatCount="indefinite"/>
  </circle>

  <!-- Top Animated Shimmer Bar -->
  <rect width="850" height="2" rx="1" fill="url(#shimmer_grad)"/>
  <defs>
    <linearGradient id="shimmer_grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#38BDF8" stop-opacity="0.2"/>
      <stop offset="50%" stop-color="#6366F1" stop-opacity="1">
        <animate attributeName="offset" values="0;1;0" dur="4s" repeatCount="indefinite"/>
      </stop>
      <stop offset="100%" stop-color="#38BDF8" stop-opacity="0.2"/>
    </linearGradient>
  </defs>

  <text x="32" y="46" fill="#F8FAFC" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="26" font-weight="700" letter-spacing="-0.5">Prathik Salla</text>
  <text x="32" y="74" fill="#38BDF8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="15" font-weight="500">Computer Science Student | Software &amp; AI Systems</text>
  <text x="32" y="102" fill="#94A3B8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="13">Building RAG applications, computer vision pipelines &amp; core software systems • ACE Engineering College</text>
  
  <g transform="translate(700, 34)">
    <rect width="118" height="26" rx="13" fill="#0F172A" stroke="#334155" stroke-width="1"/>
    <circle cx="14" cy="13" r="4" fill="#22C55E">
      <animate attributeName="opacity" values="1;0.3;1" dur="2s" repeatCount="indefinite"/>
      <animate attributeName="r" values="4;5;4" dur="2s" repeatCount="indefinite"/>
    </circle>
    <text x="26" y="17" fill="#E2E8F0" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif" font-size="11" font-weight="500">Open to Roles</text>
  </g>
</svg>"""

with open(os.path.join(ASSETS_DIR, "profile-header.svg"), "w", encoding="utf-8") as f:
    f.write(header_svg)

def create_project_card(filename, title, category, description, tags, repo_url):
    tag_elements = ""
    x_offset = 24
    for tag in tags:
        tag_w = len(tag) * 7 + 16
        tag_elements += f'''
        <g transform="translate({x_offset}, 140)">
            <rect width="{tag_w}" height="22" rx="4" fill="#1E293B" />
            <text x="8" y="15" fill="#94A3B8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11" font-weight="500">{tag}</text>
        </g>'''
        x_offset += tag_w + 8

    svg = f"""<svg width="850" height="175" viewBox="0 0 850 175" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
  <a xlink:href="{repo_url}" target="_blank">
    <rect width="850" height="175" rx="10" fill="#0D1117" stroke="#21262D" stroke-width="1"/>
    
    <!-- Category pulse text -->
    <text x="24" y="32" fill="#38BDF8" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="11" font-weight="600" letter-spacing="0.5">
      {category.upper()}
    </text>
    
    <text x="24" y="58" fill="#F0F6FC" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="18" font-weight="700">{title}</text>
    
    <text x="24" y="86" fill="#C9D1D9" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="13" font-weight="400">{description[0]}</text>
    <text x="24" y="106" fill="#C9D1D9" font-family="-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif" font-size="13" font-weight="400">{description[1] if len(description)>1 else ''}</text>
    
    {tag_elements}
    
    <!-- Action Button with subtle animated pulse -->
    <g transform="translate(805, 24)">
      <circle cx="10" cy="10" r="14" fill="#161B22" stroke="#30363D" stroke-width="1">
        <animate attributeName="stroke" values="#30363D;#38BDF8;#30363D" dur="3s" repeatCount="indefinite"/>
      </circle>
      <path d="M5 10H15M15 10L10 5M15 10L10 15" stroke="#38BDF8" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
    </g>
  </a>
</svg>"""
    with open(os.path.join(ASSETS_DIR, filename), "w", encoding="utf-8") as f:
        f.write(svg)

create_project_card(
    "project-video-rag.svg",
    "MCP-Powered Video RAG Platform",
    "AI Systems & Multimodal RAG",
    ["Semantic video search & conversational QA across long-form video content.", "Interoperable tool execution & clip generation via Model Context Protocol (MCP)."],
    ["Python", "Streamlit", "RAG", "MCP", "Vector Search"],
    "https://github.com/prathik-05/MCP-Powered-Video-RAG"
)

create_project_card(
    "project-cognito-eda.svg",
    "CognitoEDA Analytics Engine",
    "Data Science & Automated Analytics",
    ["Automates core EDA workflows including dataset cleaning, feature correlation,", "distribution analysis, and interactive visual report generation."],
    ["Python", "Streamlit", "Pandas", "Scikit-Learn", "Data Analytics"],
    "https://github.com/prathik-05/CognitoEDA"
)

create_project_card(
    "project-yolo-vision.svg",
    "YOLOv11 Vision Inference Pipeline",
    "Computer Vision & Deep Learning",
    ["Real-time object detection & instance segmentation pipeline,", "configurable for live video stream and webcam inference."],
    ["Python", "YOLOv11", "OpenCV", "PyTorch", "Streamlit"],
    "https://github.com/prathik-05/yolov11-object-detection-and-segmentation"
)

print("Animated Vercel/Linear SVG assets generated successfully!")
