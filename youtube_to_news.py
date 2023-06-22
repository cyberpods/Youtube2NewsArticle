import streamlit as st
import whisper
import openai
from pytube import YouTube
import os
import sys
from pathlib import Path
from zipfile import ZipFile
from gtts import gTTS
import re
import shutil
import tempfile

openai.api_key = os.getenv('OPENAI_API_KEY')

@st.cache
def load_model():
    # Load the whisper model
    model = whisper.load_model("base")
    return model

def save_audio(url):
    # Download the audio file from the given YouTube URL
    yt = YouTube(url)
    video = yt.streams.filter(only_audio=True).first()
    out_file = video.download()
    audio_filename = os.path.join(temp_directory, f"{Path(out_file).stem}.mp3")
    os.rename(out_file, audio_filename)
    st.info(yt.title + " has been successfully downloaded")
    st.audio(audio_filename)
    return yt.title, audio_filename

def limit_string_length(string, max_length):
    # Limit the length of a string to a maximum length
    return string[:max_length]

def audio_to_transcript(audio_file):
    # Convert audio file to transcript using the loaded whisper model
    model = load_model()
    result = model.transcribe(audio_file)
    transcript = limit_string_length(result["text"], 4000)
    return transcript

def text_to_news_article(prompt, transcript):
    # Generate a news article based on the given prompt and transcript using OpenAI's text-davinci-003 model
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt + "\n\n" + transcript,
            temperature=0.7,
            max_tokens=500,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return response.choices[0].text
    except openai.OpenAIError as e:
        st.error(f"OpenAI API Error: {str(e)}")
        st.stop()

def generate_tts_audio(text, filename):
    # Generate an MP3 audio file using gTTS with a female voice
    tts = gTTS(text, lang='en-us')
    tts.save(filename)

def sanitize_file_title(title):
    # Remove invalid characters from the file title
    sanitized_title = re.sub(r'[<>:"/\\|?*]', '', title)
    return sanitized_title

st.markdown('# 📝 **Youtube to News Article Generator App**')

st.header('Input the Video URL')

url_link = st.text_input('Enter URL of YouTube video:')

create_audio = st.checkbox("Create TTS Audio?")

edit_prompt = st.checkbox("Edit Prompt?")

if edit_prompt:
    prompt = st.text_area("Edit Prompt", value="Compose an engaging news article, approximately 500 words long, highlighting the fascinating details surrounding the following text:")
else:
    prompt = "Compose an engaging news article, approximately 500 words long, highlighting the fascinating details surrounding the following text:"

if st.button('Start'):
    with st.spinner('Downloading and processing the audio...'):
        # Download and process the audio file
        video_title, audio_filename = save_audio(url_link)

    with st.spinner('Transcript is being generated...'):
        # Generate the transcript from the audio file
        transcript = audio_to_transcript(audio_filename)
        st.header("Transcript has been generated!")
        st.success(transcript)

    with st.spinner('Generating the news article...'):
        # Generate the news article based on the prompt and transcript
        result = text_to_news_article(prompt, transcript)
        st.header("News Article has been generated!")
        st.success(result)

    if create_audio:
        with st.spinner('Creating TTS audio...'):
            st.markdown("**TTS News Article audio**")
            tts_filename = "tts_news_article.mp3"
            generate_tts_audio(result, tts_filename)
            st.audio(tts_filename, format='audio/mp3')

    # Prepare filenames with the sanitized title
    sanitized_title = sanitize_file_title(video_title)
    file_title = '_'.join(sanitized_title.split()[:5])

    # Save the transcript and article as text files
    output_directory = "output"
    os.makedirs(output_directory, exist_ok=True)

    transcript_filename = f"{output_directory}/transcript_{file_title}.txt"
    with open(transcript_filename, 'w', encoding=sys.getfilesystemencoding()) as transcript_file:
        transcript_file.write(transcript)

    article_filename = f"{output_directory}/article_{file_title}.txt"
    with open(article_filename, 'w', encoding=sys.getfilesystemencoding()) as article_file:
        article_file.write(result)

    # Create a ZIP file containing the transcript, article, and audio file
    zip_filename = f"{output_directory}/{file_title}.zip"
    with ZipFile(zip_filename, 'w') as zip_file:
        zip_file.write(transcript_filename, os.path.basename(transcript_filename))
        zip_file.write(article_filename, os.path.basename(article_filename))
        if create_audio:
            zip_file.write(tts_filename, os.path.basename(tts_filename))

    with st.spinner('Saving the files and creating the ZIP...'):
        # Provide download link for the ZIP file
        with open(zip_filename, "rb") as zip_download:
            btn = st.download_button(
                label="Download ZIP",
                data=zip_download,
                file_name=os.path.basename(zip_filename),
                mime="application/zip"
            )

    # Remove the audio file
    os.remove(audio_filename)
    if create_audio:
        os.remove(tts_filename)
