from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

# Load full BLIP model
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def generate_caption(image_path):
    """Generate a caption for a given image"""
    img = Image.open(image_path).convert("RGB")
    inputs = processor(images=img, return_tensors="pt")
    out = model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption

if __name__ == "__main__":
    img_path = "../data/sample1.jpg"  # make sure the image exists
    caption = generate_caption(img_path)
    print("Caption:", caption)

