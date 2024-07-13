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
    for i in range(max_line):
        map.append([])
        for j in range(max_col):
            map[i].append(' ' if random.random() > 0.02 else '.')
        
    plyr_col = random.randint(0, max_col)
    plyr_line = random.randint(0, max_line)

def draw():
    for i in range(max_line):
        for j in range(max_col):
            stdscr.addch(i, j, map[i][j])
            
        stdscr.addch(plyr_line, plyr_col, 'X')
        stdscr.refresh()

def move(c):
    global plyr_line, plyr_col
    if c == 'w':
        plyr_line -= 1
        if plyr_line == 0:
            plyr_line = max_line
    elif c == 's':
        plyr_line += 1
    elif c == 'a':
        plyr_col -= 1
    elif c == 'd':
        plyr_col += 1

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