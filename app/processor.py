import cv2
import numpy as np
from app.config import *

def process_image(img):

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (BLUR, BLUR), 0)

    edges = cv2.Canny(blur, CANNY_LOW, CANNY_HIGH)

    kernel = np.ones((3,3), np.uint8)

    bin_img = cv2.dilate(edges, kernel, iterations=DILATE_IT)
    bin_img = cv2.erode(bin_img, kernel, iterations=ERODE_IT)

    num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(bin_img)

    fragments = []
    sizes = []

    for i in range(1, num_labels):
        area = stats[i, cv2.CC_STAT_AREA]

        if area >= MIN_AREA:
            fragments.append(i)
            sizes.append(area)

    return {
        "count": len(fragments),
        "sizes": sizes,
        "labels": labels
    }
