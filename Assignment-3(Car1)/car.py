import cv2
from PIL import Image
import pytesseract

def ocr_core(img):
    text = pytesseract.image_to_string(Image.open(img))
    return text

im = Image.open('try2.jpeg.jpg')

left = 387
top = 345
right = 590
bottom = 429

im = im.rotate(-1)
im = im.crop((left,top,right,bottom))

im.save("Segmented2.jpg")
print(ocr_core("Segmented2.jpg"))
#Image.open("Segmented2.jpg")

