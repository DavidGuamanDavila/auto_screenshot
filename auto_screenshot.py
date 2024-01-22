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

    # Ensure the output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
        
    # Calculate the times to take screenshots
    times = [i for i in range(0, int(clip.duration), interval)]

    # Take and save screenshots
    for t in times:
        frame = clip.get_frame(t)
        img = Image.fromarray(frame)
        img.save(os.path.join(output_dir, f"screenshot_{t}s.png"))

    print(f"Screenshots taken at intervals of {interval} seconds and saved in {output_dir}.")