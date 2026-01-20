from colorama import Fore, Style, Cursor
import time 

def printFrames(Frames, bright, color, fps):
    for frame in Frames:
        print(Cursor.POS(0, 0), end="")
        if not bright:
            print(getattr(Fore, color), frame)
            time.sleep(1/fps)
            continue
        print(Style.BRIGHT, getattr(Fore, color), frame)
        time.sleep(1/fps)


def play(Frames, bright, color, fps):
    try: 
        while True:
            printFrames(Frames, bright, color, fps)
    except KeyboardInterrupt:
        print()