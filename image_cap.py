import requests
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

img_path ="img.png"

image = Image.open(img_path).convert('RGB')

text = "a photography of"
inputs = processor(image, text, return_tensors="pt")

out = model.generate(**inputs, max_length=50)
print(processor.decode(out[0], skip_special_tokens=True))