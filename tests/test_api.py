from app.processor import process_image
import cv2

img = cv2.imread("data/input/test.jpg")

result = process_image(img)

print(result)
