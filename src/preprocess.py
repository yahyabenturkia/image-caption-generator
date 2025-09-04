# src/preprocess.py
from PIL import Image

def load_image(path, max_size=512):
    """
    Load and preprocess an image for the captioning model.
    - Converts to RGB
    - Resizes to fit within max_size while keeping aspect ratio
    """
    img = Image.open(path).convert("RGB")
    w, h = img.size
    scale = min(max_size / w, max_size / h)
    if scale < 1:
        new_w, new_h = int(w * scale), int(h * scale)
        img = img.resize((new_w, new_h), Image.LANCZOS)
    return img

