from manager import getFrames, manageArgs
from Packages import constants
from colorama import Fore

import time

def main():
    Frames = getFrames()
    args = manageArgs()

    fps = args.frame
    color = args.color
    color = color.upper()

    if not color in constants.SUPPORTEDCOLORS:
        color = "WHITE"

    try: 
        while True:
            for frame in Frames:
                print(getattr(Fore, color), frame)
                time.sleep(1/fps)
    except KeyboardInterrupt:
        print()

if __name__ == "__main__":
    main()