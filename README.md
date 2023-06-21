YouTube Video to News Article Generator
This code provides a web application that allows users to generate a news article based on the transcript of a YouTube video. The application uses various libraries and APIs to download the audio from the video, convert it to text, and generate a news article based on the provided prompt and transcript.

Installation
To install and run the code, follow the instructions below based on your operating system.

Windows
Install Python 3.x from the official website: https://www.python.org/downloads/
Download the code files and extract them to a folder.
Open a command prompt and navigate to the folder where the code files are located.
Create a virtual environment (optional but recommended):
Copy code
python -m venv myenv
Activate the virtual environment:
Copy code
myenv\Scripts\activate
Install the required Python packages:
Copy code
pip install -r requirements.txt
Set the environment variable for the OpenAI API key (replace <YOUR_API_KEY> with your actual API key):
arduino
Copy code
set OPENAI_API_KEY=<YOUR_API_KEY>
Run the application:
php
Copy code
python <filename>.py
Linux and macOS
Install Python 3.x if it is not already installed (check with python3 --version).
Download the code files and extract them to a folder.
Open a terminal and navigate to the folder where the code files are located.
Create a virtual environment (optional but recommended):
Copy code
python3 -m venv myenv
Activate the virtual environment:
bash
Copy code
source myenv/bin/activate
Install the required Python packages:
Copy code
pip install -r requirements.txt
Set the environment variable for the OpenAI API key (replace <YOUR_API_KEY> with your actual API key):
arduino
Copy code
export OPENAI_API_KEY=<YOUR_API_KEY>
Run the application:
php
Copy code
python3 <filename>.py
Replace <filename> with the actual name of the Python file containing the code.

Requirements
The requirements.txt file contains the necessary Python packages and their versions for running the code. Use the following command to install them:

Copy code
pip install -r requirements.txt
Make sure to run this command within the virtual environment (if you created one) to keep the dependencies isolated.

Usage
After running the application, a web page will open in your default browser.
Input the URL of the YouTube video in the provided text field.
Optionally, check the "Create TTS Audio" checkbox to generate a text-to-speech (TTS) audio version of the news article.
Optionally, check the "Edit Prompt" checkbox to modify the default prompt for generating the news article.
Click the "Start" button to begin the process.
The audio from the YouTube video will be downloaded and processed. The audio file will be displayed and played on the web page.
The transcript of the audio will be generated and shown on the web page.
The news article will be generated based on the transcript and the provided prompt. The generated article will be displayed on the web page.
If the "Create TTS Audio" checkbox is checked, the TTS audio version of the news article will be generated and displayed on the web page.
The transcript, article, and (optionally) the TTS audio file will be saved as text files in a ZIP archive.
A download link for the ZIP archive will be provided on the web
