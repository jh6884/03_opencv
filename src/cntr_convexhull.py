import cv2
import numpy as np

img = cv2.imread('../img/hand.jpg')
img2 = img.copy()

# 그레이 스케일로 변환
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 스레시홀드를 이용해 바이너리 이미지로 변경 및 흑/백 반전
ret, imthres = cv2.threshold(imgray, 127, 255 , cv2.THRESH_BINARY_INV)

# 컨투어 찾기
contour, hierarchy = cv2.findContours(imthres, cv2.RETR_EXTERNAL, \
                                             cv2.CHAIN_APPROX_SIMPLE)

cntr = contour[0]

# 볼록 선체 찾기와 그리기
hull = cv2.convexHull(cntr)
cv2.drawContours(img2, [hull], -1, (0, 255, 0), 1)

# 볼록 선체 만족 여부 확인
print(cv2.isContourConvex(cntr), cv2.isContourConvex(hull))

# 볼록 선체 찾기
hull2 = cv2.convexHull(cntr, returnPoints=False)

# 볼록 선체 결함 찾기
defects = cv2.convexityDefects(cntr, hull2)

# 볼록 선체 결함 순회
for i in range(defects.shape[0]):
    # 시작, 종료, 가장 먼 지점, 거리
    startP, endP, farthestP, distance = defects[i, 0]
    # 가장 먼 지점의 좌표 구하기
    farthest = tuple(cntr[farthestP][0])
    # 거리를 부동 소수점으로 변환
    dist = distance/256.0
    # 거리가 1보다 큰 경우
    if dist > 1:
        # 빨강색 점 표시
        cv2.circle(img2, farthest, 3, (0,0,255), -1)

# 결과 출력
cv2.imshow('contour', img)
cv2.imshow('convex hull', img2)

cv2.waitKey(0)
cv2.destroyAllWindows()