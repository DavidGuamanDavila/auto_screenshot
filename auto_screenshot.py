from moviepy.editor import VideoFileClip
from PIL import Image
import os


def take_screenshots(video_filename, output_dir_name, interval=5):
    # Define the base directory (Downloads folder)
    base_dir = os.path.expanduser('~/Downloads')

    # Build the full paths for the video file and the output directory
    video_path = os.path.join(base_dir, video_filename)
    output_dir = os.path.join(base_dir, output_dir_name)

    # Load the video
    clip = VideoFileClip(video_path)