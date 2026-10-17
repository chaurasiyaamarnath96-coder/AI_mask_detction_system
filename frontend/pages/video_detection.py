import streamlit as st
import requests
import tempfile
import os

st.set_page_config(
    page_title="Video Detection",
    layout="wide"
)

st.title("🎥 Face Mask Video Detection")

video = st.file_uploader(
    "Upload Video",
    type=["mp4", "avi", "mov"]
)

if video:

    left, right = st.columns(2)

    with left:

        st.subheader("Original Video")

        st.video(video)

    if st.button(
        "🚀 Process Video"
    ):

        with st.spinner(
            "Processing video..."
        ):

            video.seek(0)

            response = requests.post(
                "http://127.0.0.1:8000/predict-video",
                files={
                    "file": (
                        video.name,
                        video,
                        video.type
                    )
                },
                timeout=300
            )

        if response.status_code != 200:

            st.error(
                f"Backend Error: {response.status_code}"
            )

            st.text(
                response.text
            )

            st.stop()

        data = response.json()

        st.json(data)

        with right:

            st.subheader(
                "Detection Result"
            )

            if "video_url" in data:

                st.video(
                    data["video_url"]
                )

            elif "output_video" in data:

                video_path = data["output_video"]

                if os.path.exists(video_path):

                    with open(video_path, "rb") as f:
                        video_bytes = f.read()

                    st.video(video_bytes)

                else:
                    st.error(
                        f"Video not found: {video_path}"
                )

            else:

                st.warning(
                    "Processed video path not returned"
                )

        st.success(
            "✅ Processing Complete"
        )