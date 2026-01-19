from Packages import constants

import os


FramesFiles = [str(f) for f in sorted(int(fName) for fName in os.listdir(constants.FRAMESPATH))]
Frames = []

def getFrames() -> list:
    for framef in FramesFiles:
        framepath = os.path.join(constants.FRAMESPATH, framef)
        with open(framepath, "r") as f:
            Frames.append(f.read())

    return Frames