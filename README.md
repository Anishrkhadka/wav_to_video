# WAV to Video Converter (Streamlit App)

This is a simple Streamlit web app that lets you upload a `.wav` audio file and a cover image (JPG or PNG), then generates a video (`.mp4`) using FFmpeg. The output is a static-cover video suitable for podcast platforms, YouTube, or social sharing.

## Features

- Drag-and-drop interface
- WAV + cover image -> MP4 video
- Instant preview and download
- Built with Streamlit and FFmpeg
- Local, offline-friendly setup

## Requirements

- [Micromamba](https://mamba.readthedocs.io/en/latest/micromamba-installation.html)
- FFmpeg (installed via micromamba or system-wide)

---

## 📦 Setup Instructions

### 1. Install Micromamba (if you haven’t)

#### macOS / Linux:

```bash
curl micro.mamba.pm/install.sh | bash
