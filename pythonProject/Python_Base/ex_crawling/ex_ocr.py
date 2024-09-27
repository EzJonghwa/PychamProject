# ocr 관련 라이브러리
# pip install easyOCR
# 이미지 편집관련 라이브라리
#pip install opencv-python

import easyocr
import cv2


src = cv2.imread('./car.JPG')
# 원본 이미지를 그레이 컬러로 저장 함
gray = cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)
cv2.imwrite('car_gray.jpg',gray)

#원본 이미지를 블러처리해 저장
blur =cv2.medianBlur(src,15)
cv2.imwrite('car_blur.jpg',blur)

# 이미지 크기
height,width,_=src.shape
print(height,width)
crop_width = 250
crop_height =250
center_x,center_y=width//2,height//2

#  자를 영역의 시작 및 끝 좌표 계산
x_start = center_x -(crop_width //2)
x_end = center_x+(crop_width //2)

y_start = center_y -(crop_height //2)
y_end = center_y +(crop_height //2)

# 이미지 자르기
cropped = src[y_start:y_end , x_start:x_end]
cv2.imwrite('corpped_car.jpg',cropped)

# reader = easyocr.Reader(['en','ko'],gpu=False)
# results = reader.readtext('./corpped_car.JPG')
# for result in results:
#     if result[2]>0.4: print(result[1])




reader = easyocr.Reader(['en','ko'],gpu=False)
results = reader.readtext('./recipe.png')
for result in results:
    if result[2]: print(result[1])



# pip install easyOCR
# import easyocr

# 해당 배열에서 40 퍼 이상의 정확도를 가진 것들만 출력

# 해당 이미지에서 텍스트로 인식 되는 것들은 모두 추출함