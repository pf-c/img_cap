# Image Caption Generator using BLIP

This repository contains a collection of tools for generating captions for images using the BLIP (Bootstrapping Language-Image Pre-training) model. BLIP is a state-of-the-art vision-language model that can generate natural language descriptions of images.

## Features

- Caption images from URLs
- Caption images from your local folders
- Interactive Gradio web interfaces for easy use
- Batch processing capability

## Applications

- **automate_url_captioner.py**: Generate captions for images from URLs
- **hello.py**: Basic Gradio demonstration app
- **image_cap.py**: Gradio app with image upload and captioning capabilities
- **image_captioing_app.py**: Caption images stored in specific folders
- **local_img_cap.py**: Batch caption images from local directories

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- Git

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/pf-c/img_cap.git
   ```

2. Navigate to the project directory:
   ```bash
   cd ImageCaptionGenerator
   ```

3. Set up a virtual environment:

   #### Using venv (Python's built-in virtual environment)
   ```bash
   # Create virtual environment
   python -m venv venv

   # Activate virtual environment
   # For Windows:
   venv\Scripts\activate
   # For macOS/Linux:
   source venv/bin/activate
   ```

   #### Using conda
   ```bash
   # Create conda environment
   conda create -n image_caption_env python=3.8
   
   # Activate conda environment
   conda activate image_caption_env
   ```

4. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Caption Images from URLs

```bash
python automate_url_captioner.py 
```

### Caption Local Images

```bash
python local_img_cap.py 
```

### Launch Gradio Web Interface

```bash
python image_cap.py
```
Then open your browser and navigate to `http://localhost:7860` to access the web interface.

## Using Different BLIP Models

The repository is configured to use the default BLIP model, but you can change it to use different versions by modifying the model initialization in the scripts:

```python
# Example for using different BLIP model variants
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")
```

## Sample Results

Input Image | Generated Caption
------------|------------------
<sample_image> | "a person hiking on a mountain trail with a scenic view"
<sample_image> | "a cat sleeping on a windowsill in the sunshine"

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements

- [BLIP: Bootstrapping Language-Image Pre-training](https://github.com/salesforce/BLIP)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers/index)
- [Gradio](https://gradio.app/)
