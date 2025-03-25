import os, sys
from PIL import Image

def gifToFrames(infile):
    try:
        im = Image.open(infile)
    except IOError:
        print ("Cant load", infile)
        sys.exit(1)
        
    f, e = os.path.splitext(infile)
    i = 0
    mypalette = im.getpalette()

    try:
        im.putpalette(mypalette)
        while True:
            new_im = Image.new("RGBA", im.size)
            new_im.paste(im)
            new_im.save(f+str(i)+'.png')

            i += 1
            im.seek(im.tell() + 1)

    except EOFError:
        pass 
                
    
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 GIFtoFrames.py <gif_file>")
        sys.exit(1)
        
    infile = sys.argv[1]
    gifToFrames(infile)
    
#aaronclassic
    
        
    