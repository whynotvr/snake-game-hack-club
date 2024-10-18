import random
import curses

s =curses.initscr()

curses.curs_set(0)
sh, sw, = s.getmaxxyx()

w = curses.newwin(sh, sw, 0,0)

w.keypad(1)

w.timeout(100)


snk_x =sw/4
snk_y =sh/2

snake = [
    [snk_y, snk_x]
    [snk_y, snk_x-1]
    [snk_y, snk_x-2]
]

food  = [sh/2, sw/2]

w.addch(int(food[0]), int(food[1]),curses.ACS_PI)
key = curses.KEY_RIGHT
while True:
    next_key = w.getch()

    wrong_operation = True if (next_key == -1 or next_key == curses.KEY_DOWN and key == curses.KEY_UP\
                               or key == curses.KEY_DOWN and next_key == curses.KEY_UP\
                               or next_key == curses.KEY_LEFT and key == curses.KEY_RIGHT\
                               or key == curses.KEY_LEFT and next_key == curses.KEY_RIGHT) else False

    if next_key == -1:
        key = key
    else:
        key= next_key
    if snake[0][0] in [0,sh] or snake[0,1] in [0,sw] or snake[0] in snake[1:]:
        curses.nocbreak();
        w.keypad(False)
        curses.echo()
        curses.endwin()
        print("you lost")
        break
        quit()

