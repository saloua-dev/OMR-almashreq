import cv2
import numpy as np


def rectangle_contour(contours):
    recCon = []
    for i in contours:
        area = cv2.contourArea(i)
        if area > 50:
            peri = cv2.arcLength(i, True)
            approx = cv2.approxPolyDP(i, 0.02 *peri, True)
            # print('Corner Points ',len(approx))
            if len(approx) == 4:
                recCon.append(i)
    recCon = sorted(recCon, key=cv2.contourArea, reverse=True)
    return recCon

def getCornerPoints(cont):
    peri = cv2.arcLength(cont, True)
    approx = cv2.approxPolyDP(cont, 0.02 * peri, True)
    return approx

def reorder(myPoints):
    myPoints = myPoints.reshape((4 ,2))
    myPointsNew = np.zeros((4 ,1 ,2), np.int32)
    add = myPoints.sum(1)
    # print('myPoints ',myPoints)
    # print('add ',add)
    myPointsNew[0] = myPoints[np.argmin(add)]  # [0,0]
    myPointsNew[3] = myPoints[np.argmax(add)]  # [w,h]
    diff = np.diff(myPoints ,axis=1)
    myPointsNew[1 ] =myPoints[np.argmin(diff)]
    myPointsNew[2 ] =myPoints[np.argmax(diff)]
    return myPointsNew
