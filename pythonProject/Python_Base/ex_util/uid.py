import uuid
# universally unique identifier , 범용 고유 삭별자
# 128비트 길이 3.4 * 10^38

unique_filename = str(uuid.uuid4()) + 'png'
print(unique_filename)


# 현재 시간 사용
import time
time_filename = time.strftime('%Y%M%D%H%M%S') + '.png'
print(time_filename)
#random 값 추가
import random
time_random_filename = time.strftime(time.strftime('%Y%M%D%H%M%S') + str(random.randint(1000,9999))) +'.png'
print(time_random_filename)
#hash
import hashlib
# 현재 시각을 md5 해시함수로 변환하여 유니크하게
hash = hashlib.md5(time.strftime('%Y%M%D%H%M%S').encode())
hash_filename = hash.hexdigest() + '.png'
print(hash_filename)


