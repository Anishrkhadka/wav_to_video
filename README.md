
# 🎙️ WAV to Video Converter (with Static Cover)

This is a simple Streamlit web app that allows you to upload a `.wav` audio file and a cover image (JPEG or PNG), and generates an `.mp4` video using FFmpeg. Perfect for publishing podcast episodes on platforms that require video format.

## Features

- Drag-and-drop UI for uploading WAV and image files  
- Converts to `.mp4` using FFmpeg with a static image  
- Compatible with major podcast and video platforms  
- One-click download of the generated video


## Requirements

This project is designed to run in a **Micromamba** or **Conda** environment.

### Create environment with micromamba
```bash
micromamba create -n wav2video python=3.11 streamlit ffmpeg -c conda-forge
micromamba activate wav2video
````



## Running the App

```bash
streamlit run app.py
```

Once running, open the browser link provided (usually [http://localhost:8501](http://localhost:8501)) and upload your `.wav` and cover image files.


## How it Works

The app wraps this FFmpeg command under the hood:

```bash
ffmpeg -loop 1 -i cover.jpg -i episode.wav -c:v libx264 -c:a aac -b:a 192k -shortest -pix_fmt yuv420p output.mp4
```
