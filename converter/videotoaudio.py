import os
import tkinter as tk
from tkinter import filedialog
import moviepy.editor as mp

# Ask the user to select the input video file using a file dialog
root = tk.Tk()
root.withdraw()
input_path = filedialog.askopenfilename(title="Select Input Video File")

if input_path:
    # Extract the file name and extension from the input file path
    file_name, ext = os.path.splitext(input_path)

    # Define the output audio file path
    output_path = f"{file_name}.mp3"

    # Convert the video to audio using MoviePy
    video = mp.VideoFileClip(input_path)
    audio = video.audio
    audio.write_audiofile(output_path)

    print(f"Audio saved to {output_path}")
else:
    print("No input file selected")
