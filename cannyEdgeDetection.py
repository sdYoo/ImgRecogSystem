import numpy as np
import cv2
import matplotlib.pyplot as plt


def show_canny():

    img = cv2.imread('images/20200610_hyori.jpg', cv2.IMREAD_GRAYSCALE)

    edge1 = cv2.Canny(img, 50, 200)
    edge2 = cv2.Canny(img, 200, 200)
    edge3 = cv2.Canny(img, 400, 200)

    cv2.imshow('original', img)
    cv2.imshow('canny Edge1', edge1)
    cv2.imshow('canny Edge2', edge2)
    cv2.imshow('canny Edge3', edge3)

    cv2.waitKey(0)
    cv2.destroyWindow()


show_canny()
