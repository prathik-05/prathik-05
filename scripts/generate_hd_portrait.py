import os
import argparse
from pathlib import Path
from PIL import Image, ImageEnhance
import numpy as np
import cv2

def generate_hd(image_path, output_path):
    image = Image.open(image_path).convert("RGB")
    w_orig, h_orig = image.size
    
    # 1. Full image aspect ratio preserving canvas
    # Target resolution: 800 width x 900 height
    W, H = 800, 900
    TOP, BOTTOM, SPACING = 40, 40, 5  # Higher dot density (5px grid instead of 8px)
    DURATION, REVEAL_END, HOLD_END = 8.5, 5.7, 7.6
    draw_h = H - TOP - BOTTOM
    
    # Crop preserving full half-body (no tight head cropping)
    aspect_target = W / draw_h
    aspect_src = w_orig / h_orig
    
    if aspect_src > aspect_target:
        new_w = int(h_orig * aspect_target)
        left = (w_orig - new_w) // 2
        crop_box = (left, 0, left + new_w, h_orig)
    else:
        new_h = int(w_orig / aspect_target)
        top = 0  # Start from top of photo to keep head & torso
        crop_box = (0, top, w_orig, top + new_h)
        
    cropped_img = image.crop(crop_box)
    
    cols = W // SPACING
    rows = draw_h // SPACING
    
    # Resize image to dot matrix grid
    small = cropped_img.resize((cols, rows), Image.Resampling.LANCZOS)
    gray_small = ImageEnhance.Contrast(small.convert("L")).enhance(1.35)
    
    # Simple foreground mask to remove flat background noise
    gray_np = np.array(gray_small)
    bg_thresh = np.percentile(gray_np, 15)  # threshold background
    
    circles = []
    total_dots = rows * cols
    
    for y in range(rows):
        for x in range(cols):
            lum = gray_small.getpixel((x, y)) / 255.0
            
            # Skip very dark background dots to keep portrait crisp
            if lum < 0.12:
                continue
                
            r = 0.8 + (lum ** 0.85) * 2.2
            opacity = 0.45 + lum * 0.55
            cx = x * SPACING + SPACING / 2
            cy = TOP + y * SPACING + SPACING / 2
            
            raster = (y * cols + x) / max(1, total_dots - 1)
            appear = 0.5 + raster * (REVEAL_END - 0.5)
            appear2 = min(appear + 0.1, HOLD_END)
            
            kt = f"0;{appear/DURATION:.6f};{appear2/DURATION:.6f};{HOLD_END/DURATION:.6f};1"
            
            # Glowing terminal emerald/cyan dots
            color = "#78ff9c" if lum > 0.4 else "#38bdf8"
            
            circles.append(
                f'<circle cx="{cx:.2f}" cy="{cy:.2f}" r="{r:.2f}" fill="{color}" fill-opacity="{opacity:.3f}" opacity="0">\n'
                f'  <animate attributeName="opacity" values="0;0;1;1;0" keyTimes="{kt}" dur="{DURATION}s" repeatCount="indefinite"/>\n'
                f'  <animate attributeName="r" values="{r:.2f};{r:.2f};{r*1.5:.2f};{r:.2f};{r:.2f}" keyTimes="{kt}" dur="{DURATION}s" repeatCount="indefinite"/>\n'
                f'</circle>'
            )

    svg = f"""<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
<rect width="100%" height="100%" fill="#090D16" rx="12"/>
<!-- Glow Filter -->
<defs>
  <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
    <feGaussianBlur stdDeviation="1.5" result="blur"/>
    <feMerge>
      <feMergeNode in="blur"/>
      <feMergeNode in="SourceGraphic"/>
    </feMerge>
  </filter>
</defs>
<g filter="url(#glow)">
{''.join(circles)}
</g>
</svg>"""

    output_path.write_text(svg, encoding="utf-8")
    print(f"Full half-body HD portrait SVG saved to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("image", type=Path)
    parser.add_argument("-o", "--output", type=Path, default=Path("portrait.svg"))
    args = parser.parse_args()
    generate_hd(args.image, args.output)
