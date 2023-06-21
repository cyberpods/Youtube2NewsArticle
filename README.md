
# Youtube Video to News Article Generator

This application allows you to generate a news article from a YouTube video's audio transcript. It uses OpenAI's Whisper ASR model to transcribe the audio and OpenAI's text-davinci-003 model to generate the news article based on a given prompt.

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/your-repo-url.git
   ```

2. Install the required Python packages. You can use `pip` to install the dependencies listed in the `requirements.txt` file:

   ```
   pip install -r requirements.txt
   ```

3. Set up your OpenAI API key. Sign up on the [OpenAI website](https://openai.com/) and obtain an API key. Set the `OPENAI_API_KEY` environment variable on your machine to the API key value.

## Usage

1. Run the application:

   ```
   streamlit run main.py
   ```

2. Access the application in your web browser at `http://localhost:8501`.

3. Input the URL of the YouTube video in the provided text field.

4. Optionally, check the "Create TTS Audio" checkbox to generate text-to-speech audio for the generated news article.

5. Optionally, check the "Edit Prompt" checkbox to modify the default prompt for generating the news article. Enter your desired prompt in the text area.

6. Click the "Start" button to begin the process.

7. The application will download and process the audio from the YouTube video. It will then generate the transcript and the news article based on the prompt and transcript.

8. The generated news article will be displayed on the application's interface. If you checked the "Create TTS Audio" checkbox, the text-to-speech audio will also be available for playback.

9. The transcript, article, and audio files will be saved in a ZIP file, which can be downloaded by clicking the "Download ZIP" button.

## OpenAI API Requirements

This application uses the OpenAI API to transcribe the audio and generate the news article. To use the application, you need to sign up on the [OpenAI website](https://openai.com/) and obtain an API key. Set the `OPENAI_API_KEY` environment variable on your machine to the API key value before running the application.

Make sure you review the OpenAI API documentation for usage limits and pricing details.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to customize and enhance the application according to your needs.