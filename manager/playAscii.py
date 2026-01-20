from colorama import Fore, Style, Cursor
import time 

def printFrames(Frames, bright, color, fps, erase):
    for frame in Frames:
        erase and print(Cursor.POS(0, 0), end="")

        if not bright:
            print(getattr(Fore, color), frame)
            time.sleep(1/fps)
            continue
        print(Style.BRIGHT, getattr(Fore, color), frame)
        time.sleep(1/fps)


def play(Frames, bright, color, fps, erase):
    try: 
        while True:
            printFrames(Frames, bright, color, fps, erase)
    except KeyboardInterrupt:
        print()