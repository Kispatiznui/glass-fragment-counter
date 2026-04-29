import time
import cv2
from app.processor import process_image

img = cv2.imread("data/input/test.jpg")

start = time.time()
process_image(img)
end = time.time()

print("Tiempo:", end - start)
