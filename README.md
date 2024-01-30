# auto_screenshot_util

## Description
**auto_screenshot_util** is a Python utility designed to facilitate the automatic capture of screenshots from a video file at specified time intervals. This utility was inspired by the specific needs encountered in the field of computer vision, particularly in the process of creating custom datasets. It addresses a common challenge where researchers and developers extract camera feeds in MP4 format from ROS (Robot Operating System) bag files and require an efficient method to generate image datasets.

The utility streamlines the task of capturing screenshots, automating what would otherwise be a time-consuming manual process. It's particularly useful for scenarios where one needs to create image datasets from video sources, such as extracting frames from camera feeds for training computer vision models, analyzing video content, or capturing memorable moments from various video clips.

By providing an automated solution to take screenshots at defined intervals, **auto_screenshot_util** significantly enhances productivity and accuracy in the dataset creation process, making it an invaluable tool for anyone working in computer vision, video analysis, or related fields.

## Features
- **Automated Screenshot Capture**: Extracts screenshots from a video file automatically at user-defined intervals.
- **Customizable Interval Settings**: Users can easily set the frequency of screenshots (e.g., every 5 seconds).
- **Simple and User-Friendly**: Designed for ease of use, requiring minimal setup and technical know-how.
- **Organized Output**: Saves all screenshots in a specified directory, keeping your files neatly arranged.

## Requirements
- Python 3.x
- moviepy
- Pillow (Python Imaging Library)

## Installation
Ensure you have Python 3 installed on your system. Install the necessary Python libraries using the following commands:

```bash
pip3 install moviepy
pip3 install pillow
```

## Usage
1. Download the *auto_screenshot* script from this repository.
2. Open the script in a text editor and configure the *video_filename* and *output_dir_name* variables according to your needs.
3. Execute the script:
``` bash
python3 auto_screenshot.py
```
4. Your screenshots will be available in the designated output directory.

## Converting Video Formats

To use *auto_screenshot* with *.mov* files or other formats, you may first need to convert them to *.mp4*. This can be done using FFmpeg, a powerful multimedia framework.

### Install Homebrew:
Open the Terminal and run. You can visit the [Homebrew](https://brew.sh/) website for more information:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```

### Install FFmpeg:
After installing Homebrew, install FFmpeg by running:
```bash
brew install ffmpeg
```

### Convert .mov to .mp4::
Once FFmpeg is installed, convert your .mov file to .mp4 using the following command (replace input.mov with your file's path and output.mp4 with the desired output file name):
```bash
ffmpeg -i input.mov -q:v 0 output.mp4
```
