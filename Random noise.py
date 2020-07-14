import random
import time
import os

cnt_zero = 0
cnt_one = 0

while True:
    pope = random.randint(0, 1)
    if pope:
        cnt_one += 1
    else:
        cnt_zero += 1
    print('Zero: ' + str(cnt_zero))
    print('One:  ' + str(cnt_one))

    time.sleep(0.13333)
    os.system('cls')
