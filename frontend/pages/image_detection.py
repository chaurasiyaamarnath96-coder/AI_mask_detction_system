import streamlit as st
import requests
from PIL import Image
import io
import base64

st.title("🖼 Image Detection")

file = st.file_uploader(
    "Upload Image",
    type=["jpg", "jpeg", "png"]
)

if file:

    col1, col2= st.columns(2)

    with col1:

        st.subheader(
            "Original Image"
        )

        image = Image.open(file)

        st.image(
            image,
            use_container_width=True
        )

    files = {
        "file": (
            file.name,
            file,
            file.type
        )
    }
    file.seek(0)  # Reset the file pointer to the beginning
    response = requests.post(
        "http://127.0.0.1:8000/predict",
        files=files
    )

    data = response.json()

    with col2:

        st.subheader(
            "Detection Result"
        )

        if "annotated_image" in data:

            img_bytes = base64.b64decode(
                data["annotated_image"]
            )

            st.image(
                img_bytes,
                use_container_width=True
            )

    st.divider()

    c1,c2,c3,c4,c5 = st.columns(5)

    c1.metric(
        "Total Faces",
        data.get(
            "total_faces",
            0
        )
    )

    c2.metric(
        "Masked",
        data.get(
            "masked",
            0
        )
    )

    c3.metric(
        "Unmasked",
        data.get(
            "unmasked",
            0
        )
    )

    c4.metric(
        "Incorrect",
        data.get(
            "incorrect",
            0
        )
    )

    c5.metric(
        "Compliance %",
        data.get(
            "compliance",
            0
        )
    )