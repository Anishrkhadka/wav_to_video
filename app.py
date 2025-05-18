import streamlit as st
import subprocess
from pathlib import Path

st.set_page_config(page_title="WAV to Video Converter", layout="centered")

st.title("🎙️ WAV to Video Converter")
st.markdown("Upload a `.wav` file and a cover image to create a video with a static image.")

# Upload files
audio_file = st.file_uploader("Upload a WAV file", type=["wav"])
image_file = st.file_uploader("Upload a cover image", type=["jpg", "jpeg", "png"])

# Create temp directory
output_dir = Path("temp_uploads")
output_dir.mkdir(exist_ok=True)

if audio_file and image_file:
    audio_path = output_dir / audio_file.name
    image_path = output_dir / image_file.name
    video_output = output_dir / f"{audio_file.name.rsplit('.', 1)[0]}.mp4"

    # Save files
    with open(audio_path, "wb") as f:
        f.write(audio_file.getbuffer())
    with open(image_path, "wb") as f:
        f.write(image_file.getbuffer())

    st.success("Files uploaded successfully!")

    if st.button("🎬 Convert to Video"):
        # Run FFmpeg
        ffmpeg_cmd = [
            "ffmpeg",
            "-loop", "1",
            "-i", str(image_path),
            "-i", str(audio_path),
            "-c:v", "libx264",
            "-c:a", "aac",
            "-b:a", "192k",
            "-shortest",
            "-pix_fmt", "yuv420p",
            str(video_output)
        ]

        with st.spinner("Converting..."):
            try:
                subprocess.run(ffmpeg_cmd, check=True)
                st.success("✅ Video created successfully!")

                # Allow download
                with open(video_output, "rb") as f:
                    st.download_button(
                        label="⬇️ Download Video",
                        data=f,
                        file_name=video_output.name,
                        mime="video/mp4"
                    )
            except subprocess.CalledProcessError as e:
                st.error(f"FFmpeg error: {e}")

# Cleanup note
st.markdown("⚠️ Videos are stored temporarily and will be overwritten on next run.")
