import numpy as np
import cv2
import matplotlib.pyplot as plt


def show_sobel():

    img = cv2.imread('images/20200610_hyori.jpg', cv2.IMREAD_GRAYSCALE)

    laplacian =cv2.Laplacian(img, cv2.CV_64F)
    sobelx = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)

    plt.subplot(2, 2, 1), plt.imshow(img, cmap='gray')
    plt.title('original'), plt.xticks([]), plt.yticks([])

    plt.subplot(2, 2, 2), plt.imshow(laplacian, cmap='gray')
    plt.title('laplacian'), plt.xticks([]), plt.yticks([])

    plt.subplot(2, 2, 3), plt.imshow(sobelx, cmap='gray')
    plt.title('sobelx'), plt.xticks([]), plt.yticks([])

    plt.subplot(2, 2, 4), plt.imshow(sobely, cmap='gray')
    plt.title('sobely'), plt.xticks([]), plt.yticks([])

    plt.show()


show_sobel()

