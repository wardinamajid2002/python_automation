import random
import time
import sys


tree =[


    "         *      ",
    "       ****     ",
    "      *******   ",
    "     *********  ",
    "        ||       ",
    "        ||       "
]

#ansi color code
colors = ['\033[31m','\033[32m', '\033[33m', '\033[34m']

keep_running = True

def draw_tree():
    for index,line in enumerate(tree):
        print(f'\033[{index+2};1H', end =' ')
        colored_line = ""
        for char in line:
            if char == '*':
                colored_line += random.choice(colors) + char + '\033[0m'  

            else:
                colored_line += char

        print(colored_line + ' ' * 20, end = '')

    sys.stdout.flush()

# draw_tree()

def blink_loop():
    while keep_running:
        draw_tree()
        time.sleep(0.15)



draw_tree()
blink_loop()