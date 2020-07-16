import os
import keyboard
from random import choices

rows = []

for i in range(10):
    ino = ""
    for _ in range(50):
        ino += '.'
    rows.append(ino)

character = '#'
character_index = 4
clear = '.'
food = '='
score = 0
frame = 0
sup = True
while True:
    if sup:
        if keyboard.is_pressed('w'):
            if character_index != 0:
                character_index -= 1
        elif keyboard.is_pressed('s'):
            if character_index != 9:
                character_index += 1
        sup = False

    temp_row = []
    clear_prob = 0.99
    food_prob = 0.01
    for i in range(len(rows)):
        if frame == 4:
            rows[i] = rows[i][1:]
            ino = choices([clear, food], [clear_prob, food_prob])[0]
            rows[i] += ino
            #print(ino)
            temp_row.append(rows[i])
        if character_index == i:
            if rows[i][0] == food:
                score += 1
            rows[i] = character + rows[i][1:]
        print(rows[i])
    print()
    print('SCORE :', score)
    if frame == 4:
        sup = True
        frame = 0
    #time.sleep(0.01)
    os.system('cls')



    frame += 1
