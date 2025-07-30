import cv2
import numpy as np

img = cv2.imread('../img/bad_rect.png')
img2 = img.copy()

# 그레이 스케일로 변환
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 스레시홀드를 이용해 바이너리 이미지로 변경 및 흑/백 반전
ret, imthres = cv2.threshold(imgray, 127, 255 , cv2.THRESH_BINARY)

# 컨투어 찾기
contour, hierarchy = cv2.findContours(imthres, cv2.RETR_EXTERNAL, \
                                             cv2.CHAIN_APPROX_SIMPLE)

contours = contour[0]
epsilon = 0.05 * cv2.arcLength(contours, True)
approx = cv2.approxPolyDP(contours, epsilon, True)

cv2.drawContours(img, [contours], -1, (0, 255, 0), 3)
cv2.drawContours(img2, [approx], -1, (0, 255, 3), 3)

# 결과 출력
cv2.imshow('CONTOUR', img)
cv2.imshow('APPROX', img2)

cv2.waitKey(0)
cv2.destroyAllWindows()