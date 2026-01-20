from manager import getFrames, getArgs, args, play
from features import showVersion
from packages import constants
from colorama import Fore, Style

import time

def main():
    Frames = getFrames()
    _args = getArgs()
    fps, bright, color, version = args(_args)

    if version:
        showVersion()
    else:
        play(Frames, bright, color, fps)


if __name__ == "__main__":
    main()