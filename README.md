# Wazi AI Chat Application

Welcome to Wazi AI, your AI companion for learning and innovating with WaziLab. This chat application integrates LLMs to provide intelligent responses to your prompts.

## Prerequisites

- Python (3.7 or higher)
- Flask
- Pillow
- Google Generative AI library

## Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/your-username/wazi-ai.git
   ```

2. Navigate to the project directory:

   ```bash
   cd wazi-ai
   ```

3. Create a virtual environment:

   ```bash
   python -m venv venv
   ```

4. Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

5. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. Obtain your Google Generative AI API key from [Google Cloud Console](https://console.cloud.google.com/).

2. Set your API key as an environment variable:

   ```bash
   export API_KEY=your-api-key
   ```

   Replace `your-api-key` with your actual API key.

## Usage

1. Start the Flask application:

   ```bash
   python app.py
   ```

2. Open your web browser and navigate to [http://localhost:5000](http://localhost:5000).

3. Interact with Wazi AI by entering prompts in the chat input and clicking "Ask WaziAI."

4. Optionally, upload an image along with your prompt for enhanced AI responses.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
