# Youtube Video to News Article Generator App

This is a Python application that allows you to generate a news article from a YouTube video's transcript. The application uses various libraries and APIs to download the audio from the YouTube video, transcribe it, generate a news article based on the transcript, and optionally create text-to-speech (TTS) audio for the article. The generated transcript, article, and audio files are then saved and packaged into a ZIP file for easy download.

## Installation and Setup

### Prerequisites
- Python 3.x installed on your system
- pip package manager installed

### Steps
1. Clone or download the code from the repository.
2. Open a terminal or command prompt and navigate to the project directory.

#### Windows
3. Create a virtual environment (optional):
   ```
   python -m venv venv
   ```
   Activate the virtual environment:
   ```
   venv\Scripts\activate
   ```
   
#### Linux/Mac
3. Create a virtual environment (optional):
   ```
   python3 -m venv venv
   ```
   Activate the virtual environment:
   ```
   source venv/bin/activate
   ```

4. Install the required Python packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

### Running the Application

#### Windows
```
python main.py
```

#### Linux/Mac
```
python3 main.py
```

1. The application will launch in your default web browser.
2. Input the YouTube video URL in the provided text box.
3. Select the options to create TTS audio and/or edit the prompt (optional).
4. Click the "Start" button to initiate the process.

### Output

- The application will download the audio from the YouTube video, transcribe it, and display the generated transcript.
- It will then generate a news article based on the provided prompt and transcript.
- The generated news article will be displayed.
- If the "Create TTS Audio" option is selected, the application will generate an MP3 audio file for the news article and play it.
- The transcript, article, and audio files will be saved in the "output" directory.
- A ZIP file containing the transcript, article, and audio files will be created and available for download.

## Requirements.txt

```
streamlit==0.87.0
whisper==0.3.2
openai==0.29.0
pytube==11.0.1
gtts==2.2.3
```
