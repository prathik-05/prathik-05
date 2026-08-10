import os
import argparse
from pathlib import Path
from PIL import Image
import numpy as np
import cv2

def prep_photo(image_path, output_path):
    image = Image.open(image_path).convert("RGB")
    w, h = image.size
    
    # Preserve top-aligned framing (head, hair & ponytail preservation)
    # Crop with top alignment so top of head and hair contour are captured
    crop_w = w
    crop_h = int(w * 1.1)  # Height aspect ratio for portrait matrix
    
    if crop_h > h:
        crop_h = h
        crop_w = int(h / 1.1)
        
    left = (w - crop_w) // 2
    top = 0  # Align to top to preserve hair and ponytail
    right = left + crop_w
    bottom = top + crop_h
    
    cropped = image.crop((left, top, right, bottom))
    rgb = np.array(cropped)
    
    # 1. Convert to Grayscale
    gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    
    # 2. Apply CLAHE for enhanced facial highlights and ponytail hair shadow detail
    clahe = cv2.createCLAHE(clipLimit=3.2, tileGridSize=(8,8))
    enhanced = clahe.apply(gray)
    
    # 3. Composite & Save
    result = Image.fromarray(enhanced)
    result.save(output_path)
    print(f"Prepped ponytail photo saved with top-aligned framing to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("image", type=Path, default=Path(r"C:\Users\SVCS\Downloads\pic1.jpeg"))
    parser.add_argument("-o", "--output", type=Path, default=Path("source-prepped.png"))
    args = parser.parse_args()
    prep_photo(args.image, args.output)
