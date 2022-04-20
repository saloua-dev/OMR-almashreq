import cv2
import numpy as np
import utils

#######################################"
path = "3A.png"
questions = 72
choices = 5
#################################"#####
img = cv2.imread(path)
# resize answer image
widthImg = 850
heightImg = 850
img = cv2.resize(img,(widthImg,heightImg))
imgContours = img.copy()
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # convert im to gray scale
imgBlur = cv2.GaussianBlur(imgGray,(5,5),1) # convert to blur
# detect edges
imgCanny = cv2.Canny(imgBlur, 10,50)

# Apply threshold
# region of interest
roi1 = img[132:816, 150:365]
roi2 = img[132:816, 532:747]
roi1 = cv2.cvtColor(roi1, cv2.COLOR_BGR2GRAY)
roi2 = cv2.cvtColor(roi2, cv2.COLOR_BGR2GRAY)
roi1_thresh = cv2.threshold(roi1, 150, 255, cv2.THRESH_BINARY_INV)[1]
roi2_thresh = cv2.threshold(roi2, 150, 255, cv2.THRESH_BINARY_INV)[1]

# Get no zero pixel values for each cell
cells1 = utils.splitBoxes(roi1_thresh)
cells2 = utils.splitBoxes(roi2_thresh)
cells = cells1 + cells2


myPixelVal = np.zeros((questions,choices))
countCell = 0
countRow = 0
for image in cells:
    totalPixels = cv2.countNonZero(image)
    myPixelVal[countRow][countCell] = totalPixels
    countCell += 1
    if (countCell == choices):
        countRow +=1
        countCell = 0
# FINDIND INDEX VALUES FRO THE MARKINGS
myIndex = []
for x in range(0,questions):
    arr = myPixelVal[x]
    if arr.all():
        myIndexVal = np.where(arr == np.amax(arr))
        myIndex.append(myIndexVal[0][0])

answer_dict = {'0': 'A', '1': 'B', '2': 'C', '3': 'D', '4': 'E'}
answer_letter = []
for x in myIndex:
    answer_letter.append(answer_dict[f'{x}'])  # convert number to letter
print('answer_letter', answer_letter)
my_dict = dict()
for index,value in enumerate(answer_letter):
  my_dict[index+1] = value
print(my_dict)

