# auto_screenshot_util

## Description
`auto_screenshot_util` is a Python utility designed to facilitate the automatic capture of screenshots from a video file at specified time intervals. It serves as an efficient tool for generating a series of images from videos, useful in various applications such as content creation, analysis, or simply extracting memorable moments from your favorite clips.

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
