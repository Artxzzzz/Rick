from manager import getFrames, manageArgs
from Packages import constants
from colorama import Fore, Style

import time

def main():
    Frames = getFrames()
    args = manageArgs()

    fps = args.frame
    bright = args.bright
    version = args.version

    color = args.color
    color = color.upper()
    
    if not color in constants.SUPPORTEDCOLORS:
        color = "WHITE"
    
    if version:
        print("v1.0.2")

    try: 
        while not version:
            for frame in Frames:
                if not bright:
                    print(getattr(Fore, color), frame)
                    time.sleep(1/fps)
                    continue
                print(Style.BRIGHT, getattr(Fore, color), frame)
                time.sleep(1/fps)
    except KeyboardInterrupt:
        print()

if __name__ == "__main__":
    main()