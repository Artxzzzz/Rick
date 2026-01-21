from colorama import Fore, Style
import time 

def printFrames(Frames, bright, color, fps):
    attr = getattr(Fore, color)

    for frame in Frames:
        if not bright:
            print(attr, frame)
            time.sleep(1/fps)
            continue
        print(Style.BRIGHT, attr, frame)
        time.sleep(1/fps)


def play(Frames, bright, color, fps):
    try: 
        while True:
            printFrames(Frames, bright, color, fps)
    except KeyboardInterrupt:
        print()