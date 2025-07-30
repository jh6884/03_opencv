import cv2
import numpy as np
import matplotlib.pylab as plt

# 웹캠 연결
cap = cv2.VideoCapture(0)

# 해상도 설정
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

if cap.isOpened():
    while True:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        if ret:
            cv2.imshow('camera', img)
            cv2.imshow('grayscale', gray)
            cv2.imshow('hsv', hsv)
            if cv2.waitKey(1) == ord('q'):
                break
        else:
            print('no frame')
            break
else:
    print("Cannot open camera")

cap.release()
cv2.destroyAllWindows()