import os
from pathlib import Path
from PIL import Image
import numpy as np

RAMP = " .`:-=+*cs#%@"  # Bright (sparse/spaces) -> Dark (dense)

def make_ascii_svg(image_path, output_svg_path):
    img = Image.open(image_path).convert("L")
    
    # Grid dimensions for ~370px width display
    cols = 72
    aspect_ratio = img.height / img.width
    rows = int(cols * aspect_ratio * 0.55)  # Monospace font aspect correction (~0.55)
    
    small = img.resize((cols, rows), Image.Resampling.LANCZOS)
    small_np = np.array(small)
    
    # Map pixel values to ramp characters
    ramp_len = len(RAMP)
    char_matrix = []
    for y in range(rows):
        row_chars = []
        for x in range(cols):
            val = small_np[y, x]
            idx = int((val / 255.0) * (ramp_len - 1))
            char = RAMP[idx]
            # Replace spaces with non-breaking space for XML preserving
            if char == ' ':
                char = '&#160;'
            elif char == '<':
                char = '&lt;'
            elif char == '>':
                char = '&gt;'
            elif char == '&':
                char = '&amp;'
            row_chars.append(char)
        char_matrix.append("".join(row_chars))
        
    font_size = 10
    line_height = 12
    char_width = 6.2
    
    svg_w = int(cols * char_width) + 24
    svg_h = int(rows * line_height) + 30
    
    # SMIL Row-by-Row Typing Wipe Animation
    text_rows = []
    total_rows = len(char_matrix)
    duration = 4.0  # seconds total wipe duration
    
    for y, line in enumerate(char_matrix):
        delay = (y / total_rows) * duration
        row_y = 20 + y * line_height
        
        row_svg = f'''
        <g opacity="0">
          <animate attributeName="opacity" values="0;1" begin="{delay:.2f}s" dur="0.1s" fill="freeze"/>
          <text x="12" y="{row_y}" fill="#38BDF8" font-family="'Fira Code', 'Courier New', monospace" font-size="{font_size}px" xml:space="preserve">{line}</text>
        </g>'''
        text_rows.append(row_svg)
        
    svg_content = f"""<svg width="{svg_w}" height="{svg_h}" viewBox="0 0 {svg_w} {svg_h}" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="{svg_w}" height="{svg_h}" rx="10" fill="#090D16" stroke="#1E293B" stroke-width="1"/>
  
  <!-- Terminal Top Bar -->
  <rect width="{svg_w}" height="24" rx="10" fill="#0D1117"/>
  <circle cx="14" cy="12" r="4" fill="#FF5F56"/>
  <circle cx="28" cy="12" r="4" fill="#FFBD2E"/>
  <circle cx="42" cy="12" r="4" fill="#27C93F"/>
  <text x="{svg_w//2}" y="16" text-anchor="middle" fill="#64748B" font-family="monospace" font-size="10">prathik@ascii ~ portrait.sh</text>

  <g transform="translate(0, 15)">
    {''.join(text_rows)}
  </g>
</svg>"""

    with open(output_svg_path, "w", encoding="utf-8") as f:
        f.write(svg_content)
        
    print(f"Self-typing ASCII SVG generated at {output_svg_path}")

if __name__ == "__main__":
    prepped = Path("source-prepped.png")
    if not prepped.exists():
        from prep_photo import prep_photo
        prep_photo(Path(r"C:\Users\SVCS\Downloads\pic1.jpeg"), prepped)
    make_ascii_svg(prepped, Path("avi-ascii.svg"))
