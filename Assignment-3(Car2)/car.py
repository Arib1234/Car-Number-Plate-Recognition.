import cv2
from PIL import Image
import pytesseract

def ocr_core(img):
    text = pytesseract.image_to_string(Image.open(img))
    return text

im = Image.open('try3.jpg')

left = 333
top = 310
right = 563
bottom = 370

#im = im.rotate()
im = im.crop((left,top,right,bottom))

im.save("Segmented2.jpg")
print(ocr_core("Segmented2.jpg"))