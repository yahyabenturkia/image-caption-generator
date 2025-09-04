# src/inference.py
from model import processor, model
from preprocess import load_image
from utils import draw_caption  # Our new utility for drawing captions
import os
from tqdm import tqdm

# Paths
DATA_DIR = "../data"
OUTPUT_DIR = "../outputs/results"
CAPTIONS_FILE = "../outputs/captions.txt"

# Create output folder if it doesn't exist
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Clear captions file
with open(CAPTIONS_FILE, "w") as f:
    f.write("")

# Loop over all images in the data folder
for img_file in tqdm(os.listdir(DATA_DIR), desc="Generating captions"):
    if not img_file.lower().endswith(('.jpg', '.jpeg', '.png')):
        continue  # skip non-image files
    img_path = os.path.join(DATA_DIR, img_file)
    try:
        # Load image using preprocess.py
        image = load_image(img_path)
    except:
        print(f"Cannot open {img_file}, skipping.")
        continue

    # ---- Generate caption (beam search) ----
    inputs = processor(image, return_tensors="pt")
    outputs = model.generate(
        **inputs,
        max_length=30,   # Longer captions
        num_beams=5,     # Beam search
        early_stopping=True
    )
    caption = processor.decode(outputs[0], skip_special_tokens=True)

    # Save caption in text file
    with open(CAPTIONS_FILE, "a") as f:
        f.write(f"{img_file}: {caption}\n")

    # ---- Draw caption on image (using utils.py) ----
    image = draw_caption(image, caption)

    # Save final image
    out_path = os.path.join(OUTPUT_DIR, img_file)
    image.save(out_path, format="PNG")

print("✅ All captions generated and saved with bottom black box — no overlap!")

