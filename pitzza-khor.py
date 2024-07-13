import curses
import random

stdscr = curses.initscr()
curses.noecho()
curses.cbreak()
stdscr.keypad(True)
max_line = curses.LINES - 1
max_col = curses.COLS - 1

map = []
plyr_line = plyr_col = 0

def init():
    global plyr_line, plyr_col
    for i in range(-1, max_line+1):
        map.append([])
        for j in range(-1, max_col+1):
            map[i].append(' ' if random.random() > 0.005 else '.')
        
    plyr_col = random.randint(0, max_col)
    plyr_line = random.randint(0, max_line)

def in_range(a, min, max):
    if a > max:
        a = min
    elif a < min:
        a = max
    return a

def draw():
    for i in range(max_line):
        for j in range(max_col): 
            stdscr.addch(i, j, map[i][j])
            
    stdscr.addch(plyr_line, plyr_col, 'X')
    stdscr.refresh()

def move(c):
    global plyr_line, plyr_col

    if c == 'w' and map[plyr_line - 1][plyr_col] != '.':
        plyr_line -= 1
    elif c == 's' and map[plyr_line + 1][plyr_col] != '.':
        plyr_line += 1
    elif c == 'a' and map[plyr_line][plyr_col - 1] != '.':
        plyr_col -= 1
    elif c == 'd' and map[plyr_line][plyr_col + 1] != '.':
        plyr_col += 1

    plyr_line = in_range(plyr_line, 0, max_line)
    plyr_col = in_range(plyr_col, 0, max_col)


init()

playing = True
while playing:
    try:
        c = stdscr.getkey()
    except:
        c = ''
    if c in 'awsd':
        move(c)
    elif c == 'q':
        playing = False
    draw()

stdscr.clear()
stdscr.refresh()