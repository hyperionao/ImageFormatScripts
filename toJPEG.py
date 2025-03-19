import os, sys
from PIL import Image
from pillow_heif import register_heif_opener

register_heif_opener()
for infile in sys.argv[1:]:
    f, e = os.path.splitext(infile)
    outfile = f + ".jpg"
    
    if infile != outfile:
        try:
            with Image.open(infile) as im:
                im = im.convert('RGB')
                im.save(outfile)
        except OSError:
            print("cannot convert ", infile)
            
            