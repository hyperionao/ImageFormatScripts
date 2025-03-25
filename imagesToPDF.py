from PIL import Image
import os, sys

def imagesToPDF(infiles):
    images = [Image.open(infile).convert('RGB') for infile in infiles]
    pdf_name = input("Enter the name of the output PDF file:\n")
    images[0].save(f'{pdf_name}.pdf', save_all=True, append_images=images[1:], format='PDF')

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 imagesToPDF.py <image_files>")
        sys.exit(1)
        
    infiles = sys.argv[1:]
    imagesToPDF(infiles)
