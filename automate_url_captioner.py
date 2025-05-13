import requests
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup
from transformers import AutoProcessor, BlipForConditionalGeneration


processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

url = "url_here"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
img_tags = soup.find_all("img")

with open("captions.txt", "w") as caption_file:
    for img_tag in img_tags:
        img_url = img_tag.get("src")
        if 'svg' in img_url or '1x1' in img_url:
            continue
        if img_url.startswith("//"):
            img_url = "https:" + img_url
        elif not img_url.startswith("http://") and not img_url.startswith("https://"):
            continue

        try:
            response = requests.get(img_url)
            image = Image.open(BytesIO(response.content)).convert('RGB')
            inputs = processor(image, return_tensors="pt")
            out = model.generate(**inputs, max_length=50)
            caption = processor.decode(out[0], skip_special_tokens=True)
            caption_file.write(f"{img_url}: {caption}\n")
        except Exception as e:
            print(f"Error processing image {img_url}: {str(e)}")
            continue