import cv2


def show_keypoint_SURF():
    img = cv2.imread('images/20200610_hyori.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    surf = cv2.xfeatures2d.SURF_create(500)
    #surf.setUpright(True)
    kp, des = surf.detectAndCompute(gray, None)
    print(len(kp))
    img2 = cv2.drawKeypoints(gray, kp, None, (0, 0, 255), 4)
    cv2.imshow('result', img2)
    cv2.waitKey()
    cv2.destroyAllWindows()


show_keypoint_SURF()