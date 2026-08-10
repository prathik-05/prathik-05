import os
import argparse
from pathlib import Path
from PIL import Image, ImageEnhance
import numpy as np
import cv2

def prep_photo(image_path, output_path):
    image = Image.open(image_path).convert("RGB")
    rgb = np.array(image)
    
    # 1. Convert to Grayscale
    gray = cv2.cvtColor(rgb, cv2.COLOR_RGB2GRAY)
    
    # 2. Apply CLAHE for enhanced facial highlights and shadows
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
    enhanced = clahe.apply(gray)
    
    # 3. Composite & Save
    result = Image.fromarray(enhanced)
    result.save(output_path)
    print(f"Prepped photo saved to {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("image", type=Path)
    parser.add_argument("-o", "--output", type=Path, default=Path("source-prepped.png"))
    args = parser.parse_args()
    prep_photo(args.image, args.output)
