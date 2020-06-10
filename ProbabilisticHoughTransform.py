import cv2
import numpy as np

def show_ProbabilisticHoughTransform():

    img = cv2.imread('images/20200610-sudoku-01.jpg')
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray,50,150,apertureSize = 3)
    minLineLength = 50
    maxLineGap = 5

    lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)

    for line in lines:
        x1,y1,x2,y2 = line[0]
        cv2.line(img,(x1,y1),(x2,y2),(0,255,0),1)

    cv2.imshow('edges', edges)
    cv2.imshow('result', img)
    cv2.waitKey()
    cv2.destroyAllWindows()


show_ProbabilisticHoughTransform()