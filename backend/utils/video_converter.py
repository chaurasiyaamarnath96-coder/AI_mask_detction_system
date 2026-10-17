import os
import shutil
import subprocess


def find_ffmpeg():
    """
    Locate ffmpeg executable automatically.
    """

    # 1. Check PATH
    ffmpeg = shutil.which("ffmpeg")
    if ffmpeg:
        return ffmpeg

    # 2. Common Windows locations
    common_paths = [
        #r"C:\ffmpeg\bin\ffmpeg.exe",
        r"C:\\Users\\amar0\\Downloads\\ffmpeg-9.0.2-essentials_build\\ffmpeg-9.0.2-essentials_build\\bin\\ffmpeg.exe"
        #r"C:\Program Files (x86)\ffmpeg\bin\ffmpeg.exe",
    ]

    for path in common_paths:
        if os.path.exists(path):
            return path

    raise FileNotFoundError(
        "\nFFmpeg not found.\n"
        "Install FFmpeg and either:\n"
        "1. Add ffmpeg to PATH\n"
        "2. Place it in C:\\ffmpeg\\bin\\ffmpeg.exe\n"
    )


def convert_avi_to_mp4(avi_path):

    if not os.path.exists(avi_path):
        raise FileNotFoundError(
            f"AVI file not found: {avi_path}"
        )

    ffmpeg_path = find_ffmpeg()

    mp4_path = os.path.splitext(avi_path)[0] + ".mp4"

    print("\n========== FFMPEG DEBUG ==========")
    print("FFmpeg:", ffmpeg_path)
    print("AVI:", avi_path)
    print("MP4:", mp4_path)
    print("==================================\n")

    command = [
        ffmpeg_path,
        "-y",
        "-i",
        avi_path,
        "-c:v",
        "libx264",
        "-preset",
        "fast",
        "-pix_fmt",
        "yuv420p",
        "-movflags",
        "+faststart",
        mp4_path,
    ]

    subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=True,
        text=True
    )

    if not os.path.exists(mp4_path):
        raise RuntimeError(
            "MP4 conversion failed."
        )

    print("MP4 Created:", mp4_path)
    print("Size:", os.path.getsize(mp4_path))

    return os.path.abspath(mp4_path)