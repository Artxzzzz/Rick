from manager import getFrames, getArgs, args, play
from features import showVersion

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