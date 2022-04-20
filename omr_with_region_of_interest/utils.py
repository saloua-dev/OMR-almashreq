import cv2
import numpy as np


def splitBoxes(img):
    rows = np.vsplit(img,36)
    # cv2.imshow("Split",rows[0])
    cells = []
    for c in rows:
        cols = np.hsplit(c, 5)
        for cell in cols:
            cells.append(cell)
    return cells

