import curses
import time
import os
from playsound import playsound
from random import choices


def game(stdscr, sped):
    curses.init_pair(3, curses.COLOR_GREEN, curses.COLOR_MAGENTA)
    curses.init_pair(5, curses.COLOR_GREEN, curses.COLOR_BLACK)
    rows = []
    speed = sped
    for u in range(5):
        inos = ""
        for _ in range(60):
            inos += '.'
        rows.append(inos)

    character = '#'
    character_index = 2
    clear = ' '
    food = '='
    score = 0
    frame = 0
    stdscr.nodelay(True)
    curses.noecho()
    bob = False
    clear_prob = 0.99
    food_prob = 0.01
    score_diff = True
    speed_diff = True
    super_diff = True
    nightmare = False
    while True:
        if score == 15 and speed_diff:
            speed -= 5
            speed_diff = False
        elif score == 30 and score_diff:
            clear_prob -= 0.01
            food_prob += 0.01
            score_diff = False
        elif score == 40 and super_diff:
            clear_prob -= 0.02
            food_prob += 0.02
            speed -= 4
            super_diff = False
        elif score == 54:
            nightmare = True

        stdscr.clear()
        c = stdscr.getch()
        if c == ord('w'):
            if character_index != 0:
                character_index -= 1
        elif c == ord('s'):
            if character_index != 4:
                character_index += 1

        for i in range(5):
            if frame == speed:
                rows[i] = rows[i][1:]
                ino = choices([clear, food], [clear_prob, food_prob])[0]
                rows[i] += ino
                if character_index != i:
                    if rows[i][0] == food:
                        if nightmare:
                            score -= 3
                        else:
                            score -= 1
                        if score < 0:
                            stdscr.clear()
                            stdscr.addstr('\n\n')
                            stdscr.addstr('             \n', curses.color_pair(3))
                            stdscr.addstr(' YOU LOST :( \n', curses.color_pair(3))
                            stdscr.addstr('             \n', curses.color_pair(3))
                            stdscr.refresh()
                            bob = True
                            time.sleep(2)

            if character_index == i:
                if rows[i][0] == food:
                    score += 1
                    playsound(os.getcwd() + "/score.mp3", block=False)
                rows[i] = character + rows[i][1:]

            stdscr.addstr(rows[i] + '\n', curses.color_pair(5))
        if bob:
            break
        stdscr.addstr('SCORE: ' + str(score), curses.color_pair(5))
        stdscr.refresh()
        time.sleep(0.005)
        if frame == speed:
            frame = 0
        frame += 1


def start_menu(stdscr):
    selected = curses.color_pair(1)
    deselected = curses.color_pair(2)
    gamemode = 0
    while True:
        stdscr.clear()
        stdscr.addstr('\n\n')
        if gamemode == 0:
            stdscr.addstr('    Easy    ' + '\n', selected)
            stdscr.addstr('    Hard    ' + '\n', deselected)
            stdscr.addstr('    EXIT    ', deselected)
            stdscr.refresh()
            c = stdscr.getch()
            if c == ord('s'):
                gamemode = 1
            elif c == ord(' '):
                game(stdscr, 20)
        elif gamemode == 1:
            stdscr.addstr('    Easy    \n', deselected)
            stdscr.addstr('    Hard    \n', selected)
            stdscr.addstr('    EXIT    ', deselected)
            stdscr.refresh()
            c = stdscr.getch()
            if c == ord('w'):
                gamemode = 0
            elif c == ord('s'):
                gamemode = 2
            elif c == ord(' '):
                game(stdscr, 11)
        else:
            stdscr.addstr('    Easy    \n', deselected)
            stdscr.addstr('    Hard    \n', deselected)
            stdscr.addstr('    EXIT    ', selected)
            stdscr.refresh()
            c = stdscr.getch()
            if c == ord('w'):
                gamemode = 1
            elif c == ord(' '):
                exit(0)


screen = curses.initscr()
#playsound("C:/Users/sigur/Music/bill.mp3", block=False)
curses.start_color()
curses.use_default_colors()
curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_MAGENTA)
curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.curs_set(0)
start_menu(screen)
