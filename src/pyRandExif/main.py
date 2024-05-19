import argparse
import os
import random
from datetime import datetime, timedelta
from PIL import Image
import piexif


def add_random_exif(image_path, dest_folder, count):
    """
    Adds random EXIF (Exchangeable Image File Format) data to an image.

    Args:
        image_path (str): The path to the input image file.
        dest_folder (str): The destination folder where the modified images will be saved.
        count (int): The number of modified images to generate.

    Returns:
        None
    """
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)

    for i in range(count):
        image = Image.open(image_path)
        exif_dict = piexif.load(image.info["exif"])

        # Generate random GPS coordinates
        lat = random.uniform(-90, 90)
        lon = random.uniform(-180, 180)

        exif_dict["GPS"][piexif.GPSIFD.GPSLatitudeRef] = b"N" if lat >= 0 else b"S"
        exif_dict["GPS"][piexif.GPSIFD.GPSLatitude] = to_deg(lat)
        exif_dict["GPS"][piexif.GPSIFD.GPSLongitudeRef] = b"E" if lon >= 0 else b"W"
        exif_dict["GPS"][piexif.GPSIFD.GPSLongitude] = to_deg(lon)

        # Generate random datetime
        random_date = datetime.now() - timedelta(days=random.randint(0, 365))
        exif_dict["Exif"][piexif.ExifIFD.DateTimeOriginal] = random_date.strftime(
            "%Y:%m:%d %H:%M:%S"
        ).encode()

        exif_bytes = piexif.dump(exif_dict)

        # Save image with new EXIF data
        output_path = os.path.join(dest_folder, f"output_{i+1}.jpg")
        image.save(output_path, "jpeg", exif=exif_bytes)

        print(f"Saved {output_path} with random EXIF data.")


def to_deg(value):
    """
    Convert decimal coordinates into degrees, minutes, and seconds.

    Args:
        value (float): The decimal coordinate value to convert.

    Returns:
        tuple: A tuple containing three tuples representing degrees, minutes, and seconds respectively.
               Each inner tuple contains two elements: the value and the divisor.

    Example:
        >>> to_deg(12.345)
        ((12, 1), (20, 1), (42, 1000))
    """
    abs_value = abs(value)
    d = int(abs_value)
    m = int((abs_value - d) * 60)
    s = round((abs_value - d - m / 60) * 3600 * 1000)
    return ((d, 1), (m, 1), (s, 1000))


def main():
    parser = argparse.ArgumentParser(description="Add random EXIF data to an image.")
    parser.add_argument("image_path", type=str, help="Path to the image file.")
    parser.add_argument(
        "dest_folder", type=str, help="Destination folder to save images."
    )
    parser.add_argument("count", type=int, help="Number of images to generate.")
    args = parser.parse_args()

    add_random_exif(args.image_path, args.dest_folder, args.count)


if __name__ == "__main__":
    main()
