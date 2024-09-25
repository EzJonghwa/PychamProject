import os
from os import makedirs

# os 는 python 표준 라이브러리로 운영체제 상호작용하는 다양한
# 기능을 제공함(파일선택, 삭제, 변경...)
forlder = os.getcwd() # 현재위치
print(forlder)
# 폴더 리스트

file_list = os.listdir(forlder)
for f in file_list:
    file_path = os.path.join(forlder,f) # 경로 결합
    if os.path.isfile(file_path):
        print('파일이구먼',file_path)
    if os.path.isdir(file_path):
        print('폴더구먼',file_path)

# 파일 삭제 os.remove('경로')
# 폴더(비어있는) 삭제 os.rmdir
# 폴더(파일있는) 전체삭제

import shutil
# 폴더(파일 있는) 전체삭제
# shutil.rmtree('경로')
# os.remove('C:/dev/PychamProject/pythonProject/Python_Base/ex_util/test/test.txt')
# os.rmdir('C:/dev/PychamProject/pythonProject/Python_Base/ex_util/test')

# 폴더 생성
image_dir = './img'
if not os.path.exists(image_dir):   #해당 경로가 존재하지 않으면
    os.makedirs(image_dir)

#  이미지 저장





