# YouTube Video to News Article Generator

This is a simple Python script that allows you to convert a YouTube video into a news article. It utilizes OpenAI's text-davinci-003 model to generate the article based on the transcript extracted from the video's audio. The script also provides the option to create a TTS (Text-to-Speech) audio file of the generated article.

## Features

- Download audio from a YouTube video
- Transcribe the audio into text using the Whisper ASR model
- Generate a news article based on the transcript using OpenAI's text-davinci-003 model
- Calculate the estimated token count and cost for generating the article
- Create a TTS audio file of the article
- Save the transcript, article, and audio file in a ZIP archive
- Provide a download link for the generated ZIP archive

## Usage

1. Clone the repository or download the script `youtube_to_news.py` to your local machine.

2. Install the required Python dependencies by running the following command:

pip install -r requirements.txt


3. Set up your OpenAI API key by creating a `.env` file in the project directory and adding the following line:

OPENAI_API_KEY=your-api-key


Replace `your-api-key` with your actual OpenAI API key.

4. Run the script using the following command:

streamlit run youtube_to_news.py


5. Open your web browser and navigate to the provided URL (usually `http://localhost:8501`) to access the web interface.

6. Input the URL of the YouTube video you want to convert and click "Start".

7. Wait for the audio processing, transcript generation, and article generation to complete. The results will be displayed on the web interface.

8. If desired, check the "Create TTS Audio" checkbox to generate a TTS audio file of the article.

9. The generated transcript, article, and (optional) audio file will be saved in a ZIP archive. Click "Download ZIP" to download the archive.

## Requirements

The script requires the following Python packages:

- streamlit
- openai
- pytube
- whisper
- python-dotenv
- gtts

You can install the dependencies by running the following command:

pip install -r requirements.txt

