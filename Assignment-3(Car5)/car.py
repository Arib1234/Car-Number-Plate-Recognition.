import cv2
from PIL import Image
import pytesseract

def ocr_core(img):
    text = pytesseract.image_to_string(Image.open(img))
    return text

im = Image.open('renault.jpg')

left = 555
top = 2400
right = 1026
bottom = 2580

im = im.rotate(5)
im = im.crop((left,top,right,bottom))

im.save("Segmented2.jpg")
print(ocr_core("Segmented2.jpg"))