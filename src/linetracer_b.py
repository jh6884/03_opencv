import cv2
import numpy as np
import matplotlib.pylab as plt

# 웹캠 연결
cap = cv2.VideoCapture(0)

# 해상도 설정
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

# matplot 설정
plt.ion()

window = 'camera'
blk_size = 9
C = 5

def masking(bp, window):
    _, mask = cv2.threshold(bp, 1, 255, cv2.THRESH_BINARY)
    result = cv2.bitwise_and(img, img, mask=mask)
    cv2.imshow(window, result)

def backProject_cv(hist_roi):
    bp = cv2.calcBackProject([hsv], [0, 1], hist_roi,  [0, 180, 0, 256], 1)
    masking(bp,'result_cv')    

if cap.isOpened():
    while True:
        ret, img = cap.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (5,5), 0)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
        draw = img.copy()
        canny = cv2.Canny(gray, 150, 255)
        if ret:
            #ret2, threshold = cv2.threshold(gray, 110, 255, cv2.THRESH_BINARY_INV)
            #threshold = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUCIAN_C, cv2.THRESH_BINARY_INV, 9, 5)
            
            contour, hierarchy = cv2.findContours(canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            mu = [None]*len(contour)
            for i in range(len(contour)):
                mu[i] = cv2.moments(contour[i])
            mc = [None]*len(contour)
            for i in range(len(contour)):
                mc[i] = (mu[i]['m10']/(mu[i]['m00'] + 1e-5), mu[i]['m01']/(mu[i]['m00'] + 1e-5))
            cv2.circle(img, (int(mc[i][0]), int(mc[i][1])), 4, (0,0,255), -1)
            cv2.drawContours(img, contour, -1, (255,0,0), 2)
            cv2.imshow('camera', img)
            cv2.imshow('hsv', hsv)
            cv2.imshow('binary', canny)
            if cv2.waitKey(1) == ord('e'): # e 키 입력을 통해 ROI 선택 상태에 진입하도록 설정
                (x,y,w,h) = cv2.selectROI(window, img, False)
                if w > 0 and h > 0:
                    roi = img[y:y+h, x:x+w]
                    cv2.rectangle(img, (x, y), (x+w, y+h), (0,0,255), 2)
                    hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
                    hist_roi = cv2.calcHist([hsv_roi],[0, 1], None, [180, 256], [0, 180, 0, 256] )
                    backProject_cv(hist_roi)
            elif cv2.waitKey(1) == ord('q'): # q 키 입력시 출력 종료
                break
        else:
            print('no frame')
            break
else:
    print("Cannot open camera")

cap.release()
cv2.destroyAllWindows()