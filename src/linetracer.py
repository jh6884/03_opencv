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
            if cv2.waitKey(1) == ord('q'): # q 키 입력시 출력 종료
                break
            elif cv2.waitKey(1) == 32: # 스페이스바 입력시 이미지 캡처 > 히스토그램 출력
                cv2.imwrite('../img/capture.jpg', img)
                histimg = cv2.imread('../img/capture.jpg', cv2.IMREAD_GRAYSCALE)
                hist = cv2.calcHist([histimg], [0], None, [256], [0,256])
                plt.plot(hist)
                cv2.destroyAllWindows()
                cv2.imshow('image', histimg)
                plt.show()
        else:
            print('no frame')
            break
else:
    print("Cannot open camera")

cap.release()
cv2.destroyAllWindows()