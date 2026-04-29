import cv2
import numpy as np

def resize(img, width=800):
    h, w = img.shape[:2]
    scale = width / w
    return cv2.resize(img, (width, int(h * scale)))
