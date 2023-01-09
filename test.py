from pdf2image import convert_from_path, convert_from_bytes



pdf = './sample.pdf'
# this script is for windows, for linux:
# remove the poppler variable and install poppler with  ( apt-get install poppler-utils)

images = convert_from_path(pdf, poppler_path='./poppler-22.12.0/Library/bin')
for index, img in enumerate(images):
    img.save(f"./imgs/{index}.png")
        
