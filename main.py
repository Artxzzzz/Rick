from manager import getFrames
from Packages import constants

import time

Frames = getFrames()
while True:
    for frame in Frames:
        print(frame)
        time.sleep(1/constants.FPS)