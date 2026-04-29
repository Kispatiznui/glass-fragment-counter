import cv2
import numpy as np

def process_image(img):

    if img is None:
        return {
            "count": 0,
            "sizes": [],
            "error": "invalid image"
        }

    # =========================
    # 1. PREPROCESADO SUAVE
    # =========================
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(gray, (5, 5), 0)

    # =========================
    # 2. BINARIZACIÓN ESTABLE
    # =========================
    _, thresh = cv2.threshold(
        blur,
        0,
        255,
        cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU
    )

    # =========================
    # 3. LIMPIEZA MORFOLÓGICA SUAVE
    # =========================
    kernel = np.ones((2, 2), np.uint8)

    cleaned = cv2.morphologyEx(
        thresh,
        cv2.MORPH_OPEN,
        kernel,
        iterations=1
    )

    cleaned = cv2.morphologyEx(
        cleaned,
        cv2.MORPH_CLOSE,
        kernel,
        iterations=1
    )

    # =========================
    # 4. COMPONENTES CONECTADOS
    # =========================
    num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(cleaned)

    sizes = []
    count = 0

    # =========================
    # 5. FILTRO CORREGIDO (CLAVE)
    # =========================
    for i in range(1, num_labels):

        area = stats[i, cv2.CC_STAT_AREA]
        w = stats[i, cv2.CC_STAT_WIDTH]
        h = stats[i, cv2.CC_STAT_HEIGHT]

        aspect = w / (h + 1e-5)

        # 🔥 AJUSTE IMPORTANTE AQUÍ
        if 60 < area < 300000 and 0.3 < aspect < 4.5:

            sizes.append(int(area))
            count += 1

    # =========================
    # 6. RESULTADO
    # =========================
    return {
        "count": count,
        "sizes": sizes,
        "avg_size": int(np.mean(sizes)) if sizes else 0,
        "max_size": int(max(sizes)) if sizes else 0,
        "min_size": int(min(sizes)) if sizes else 0
    }