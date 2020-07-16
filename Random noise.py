import random
import time
import os
import string

cnt_zero = 0
cnt_one = 0
max_deviation = 0

while True:
    out = ""
    for i in range(110):
        out += random.choice(string.ascii_letters + ' ')
    print(out)
    time.sleep(0.00933)

