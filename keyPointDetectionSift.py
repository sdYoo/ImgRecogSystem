import cv2


def show_keypoint():
    img = cv2.imread('images/20200610-sudoku-01.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    sift = cv2.xfeatures2d.SIFT_create()
    kp = sift.detect(gray, None)
    img = cv2.drawKeypoints(gray, kp, None, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    cv2.imshow('result', img)
    cv2.waitKey()
    cv2.destroyAllWindows()


show_keypoint()