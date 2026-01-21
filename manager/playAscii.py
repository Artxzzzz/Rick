from colorama import Fore, Style
import time 

def printFrames(Frames, bright, color, fps):
    attr = getattr(Fore, color)
    style = Style.BRIGHT if bright else Style.NORMAL
    
    for frame in Frames:
        print(style, attr, frame)
        time.sleep(1/fps)


def play(Frames, bright, color, fps):
    try: 
        while True:
            printFrames(Frames, bright, color, fps)
    except KeyboardInterrupt:
        print()