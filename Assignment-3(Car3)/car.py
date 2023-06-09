import cv2
from PIL import Image
import pytesseract

def ocr_core(img):
    text = pytesseract.image_to_string(Image.open(img))
    return text

im = Image.open('try1.jpg')

left = 685
top = 644
right = 1023
bottom = 710

im = im.rotate(-1)
im = im.crop((left,top,right,bottom))

im.save("Segmented2.jpg")
print(ocr_core("Segmented2.jpg"))