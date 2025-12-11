# ASCII Art Converter

A simple yet powerful GUI application that converts images into ASCII art. Upload any image, adjust the settings to your preference, and get stunning ASCII art output!

## Features

**Easy-to-use GUI** - Simple and intuitive interface for image conversion

**Multiple Detail Levels** - Choose from 4 different character sets for varying levels of detail
- Standard
- Enhanced  
- Best (Recommended)
- Extreme (Most detailed)

**Customizable Settings**
- Adjust width for different output sizes
- Control contrast (1-3) to enhance or soften details
- Real-time preview with scrollable output window

**Save Functionality** - Export your ASCII art as a `.txt` file

**Supports Multiple Formats** - Works with JPG, JPEG, PNG, BMP, and GIF images

## Installation

### Prerequisites
- Python 3.x
- pip (Python package manager)

### Steps

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ascii-art-converter.git
cd ascii-art-converter
```

2. Install required dependencies:
```bash
pip install pillow
```

3. Run the application:
```bash
python ascii_converter.py
```

## Usage

1. **Launch the Application** - Run the script to open the GUI window

2. **Configure Settings**
   - **Width**: Enter the desired output width in characters (default: 120)
   - **Contrast**: Adjust contrast level between 1-3 for better detail (default: 1.5)
   - **Detail Level**: Select from Standard, Enhanced, Best, or Extreme

3. **Upload Image** - Click "Upload Image" button to select an image from your computer

4. **View Output** - The ASCII art will appear in a new window with a black background

5. **Save Output** - Click "Save as .txt" to save the ASCII art as a text file

## Settings Guide

### Width
- **Smaller values (50-80)**: Faster processing, less detail
- **Default (120)**: Good balance of detail and performance
- **Larger values (150+)**: More detail, slower processing

### Contrast
- **1.0**: Original contrast
- **1.5** (Recommended): Enhanced detail
- **2.0-2.5**: High contrast, very dramatic
- **3.0**: Maximum contrast

### Detail Levels
- **Standard**: Basic ASCII characters, simple output
- **Enhanced**: More characters, better gradation
- **Best**: Optimal balance of quality and speed
- **Extreme**: Maximum detail with extended character set (slowest)

## Example

Input: Any image (photo, screenshot, artwork)

Output: ASCII representation in the terminal/text file

```
@@@@##%%***++++====----::::......
@@##%%***++++====----::::......  
##%%***++++====----::::......    
```

## Tips for Best Results

1. Use images with good contrast for better ASCII output
2. For portrait-oriented images, adjust width accordingly
3. Experiment with contrast settings to find your preferred look
4. High-detail images work best with "Best" or "Extreme" settings
5. Black and white or high-contrast images produce the clearest ASCII art

## Requirements

- Python 3.6 or higher
- Pillow (PIL) library for image processing
- tkinter (usually included with Python)

## Troubleshooting

**Issue**: "ModuleNotFoundError: No module named 'PIL'"
- **Solution**: Run `pip install pillow`

**Issue**: Image not loading
- **Solution**: Make sure the image file is in a supported format (JPG, PNG, BMP, GIF)

**Issue**: Output looks pixelated
- **Solution**: Try increasing the contrast value or using a "Best" or "Extreme" detail level

**Issue**: Output is too wide for the window
- **Solution**: Increase the window size or reduce the width setting

## Author

Created with ❤️ for ASCII art enthusiasts

**Enjoy creating ASCII art! 🎨**
