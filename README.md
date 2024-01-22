# auto_screenshot

## Description
`auto_screenshot` is a Python utility designed to facilitate the automatic capture of screenshots from a video file at specified time intervals. It serves as an efficient tool for generating a series of images from videos, useful in various applications such as content creation, analysis, or simply extracting memorable moments from your favorite clips.

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
