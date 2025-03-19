import os
import sys
import glob
from PIL import Image, UnidentifiedImageError
from pillow_heif import register_heif_opener

register_heif_opener()

accepted_formats = ('.jpeg', '.bmp', '.tiff', '.webp', '.heic', '.jpg')
unsuccessful = []

def imtoJPEG(file):
    f, e = os.path.splitext(file)
    outfile = f + ".png"

    counter = 1
    while os.path.exists(outfile):
        outfile = f"{f}_converted{counter}.png"
        counter += 1
    
    try:
        with Image.open(file) as im:
            im = im.convert('RGB')
            im.save(outfile, "PNG")
    except (UnidentifiedImageError, OSError) as e:
        print(f"Skipping {file}: {e}")
        unsuccessful.append(file)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python batch_toJPEG.py <directory>")
        sys.exit(1)

    directory = sys.argv[1]

    for filename in glob.glob(os.path.join(directory, "**/*"), recursive=True):
        if os.path.isfile(filename) and filename.lower().endswith(accepted_formats):
            imtoJPEG(filename)
        else:
            unsuccessful.append(filename)

    if unsuccessful:
        print("\nSome files could not be converted:")
        for file in unsuccessful:
            print(f"- {file}")
