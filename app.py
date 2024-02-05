from flask import Flask, render_template, request, redirect, url_for
import google.generativeai as genai
import os
import time
from PIL import Image
from io import BytesIO

app = Flask(__name__)

safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
  }
]

config = {
  'temperature': 0,
  'top_k': 20,
  'top_p': 0.9,
  'max_output_tokens': 500
}

#  gemini-pro-vision
model_vision = genai.GenerativeModel(model_name="gemini-pro-vision",
                              generation_config=config,
                              safety_settings=safety_settings)

# gemini-pro model
model_gemini = genai.GenerativeModel('gemini-pro')

genai.configure(api_key=os.getenv('api_key'))

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        try:
            prompt = request.form['prompt']
            image = request.files['image'] if 'image' in request.files else None

            # Use gemini-pro-vision if an image is uploaded
            model = model_vision if image else model_gemini

            # Handle both text and image prompts
            question = [prompt, process_image(image)] if image else prompt

            response = model.generate_content(question, stream=True)
            response.resolve()

            if response.text:
                return response.text
            else:
                return "Sorry, but I  didn't want to answer that!"
        except Exception as e:
            return "Sorry, but WaziAI didn't want to answer that!"

    return render_template('index.html', **locals())

def process_image(image):
    if image:
        # Process the image using PIL 
        img = Image.open(image)
        return img
    return None

if __name__ == '__main__':
    app.run(debug=True)
