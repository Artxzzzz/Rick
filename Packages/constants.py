import sys
import os

if getattr(sys, 'frozen', False):

    FRAMESPATH = os.path.join(sys._MEIPASS,"Frames")
else:
    FRAMESPATH = "Frames"
SUPPORTEDCOLORS = (
    "BLACK",
    "RED",
    "GREEN",
    "YELLOW",
    "BLUE",
    "MAGENTA",
    "CYAN",
    "WHITE"
)