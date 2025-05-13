import os
import glob
from PIL import Image
import requests
from transformers import AutoProcessor, BlipForConditionalGeneration

processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

img_dir = r"your_image_dir_here"
img_exts=["jpg",'png',"jpeg"]
with open("local_image_caption.txt", "w") as local_captions_file:
    for ext in img_exts:
        for image_path in glob.glob(os.path.join(img_dir, f'*.{ext}')):
            image = Image.open(image_path)
            inputs = processor(image, return_tensors="pt")
            out = model.generate(**inputs,max_length=50)
            caption = processor.decode(out[0], skip_special_tokens=True)
            local_captions_file.write(f"{image_path}: {caption}\n")