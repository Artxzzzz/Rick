from manager import getFrames, getArgs, args, play
from features import showVersion

def main():
    frames = getFrames()
    parsedArgs = getArgs()
    fps, bright, color, version = args(parsedArgs)

    if version:
        showVersion()
    else:
        play(frames, bright, color, fps)


if __name__ == "__main__":
    main()