import gradio as gr
import numpy as np
from PIL import Image
from transformers import BlipProcessor, BlipForConditionalGeneration

processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def caption_image(image:np.ndarray):
    inputs = processor(image, return_tensors="pt")
    out = model.generate(**inputs,max_length=50)
    return processor.decode(out[0], skip_special_tokens=True)

iface = gr.Interface(
    fn=caption_image,
    inputs=gr.Image(type="pil"),
    outputs="text",
    title="Image Captioning",
    description="Upload an image and get a caption.",
)

iface.launch(share=True)