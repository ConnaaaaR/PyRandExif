# pyRandExif

pyRandExif is a command-line tool that adds random EXIF data, including GPS coordinates and timestamps, to an image file. This tool is useful for testing, anonymization, and other purposes where random EXIF data might be needed.

## Features

- Adds random GPS coordinates to the image EXIF data.
- Adds a random date and time within the last year to the image EXIF data.
- Generates multiple copies of the image with unique EXIF data.

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/ConnaaaaR/PyRandExif.git
    cd pyRandExif
    ```

2. Install the package using `pip`:

    ```sh
    pip install .
    ```

## Usage

After installing the package, you can use the `pyRandExif` command in your terminal:
### Example
```sh
pyRandExif /path/to/image.jpg /path/to/destination_folder 5
```

This command will generate 5 images with random EXIF data in the specified destination folder.

### Command-line Arguments
- image_path (str): Path to the image file.
- dest_folder (str): Destination folder to save images.
- count (int): Number of images to generate.
  

## Dependencies
- [Pillow](https://python-pillow.org/)
- [piexif](https://github.com/hMatoba/piexif)


## Future Features
- Multi-Threading
- Location & DateTime Limits / Ranges
