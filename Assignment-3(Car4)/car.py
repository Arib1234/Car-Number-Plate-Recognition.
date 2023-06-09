import cv2
from PIL import Image
import pytesseract

def ocr_core(img):
    text = pytesseract.image_to_string(Image.open(img))
    return text

im = Image.open('try4.jpg')

left = 494
top = 272
right = 1134
bottom = 455

im = im.rotate(-9)
im = im.crop((left,top,right,bottom))

im.save("Segmented2.jpg")
print(ocr_core("Segmented2.jpg"))