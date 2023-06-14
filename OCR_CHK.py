try:
    from PIL import Image


except ImportError:
    import Image

import pytesseract
pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def recText(filename):
    text=pytesseract.image_to_string(Image.open(filename))
    return text


info=recText("C:/Users/balaj/OneDrive/Pictures/Saved Pictures/test10.png")

print(info)
file=open("C:/Users/balaj/OneDrive/Documents/ress.txt","w")
file.write(info)
file.close()
print("SUCCESS")



