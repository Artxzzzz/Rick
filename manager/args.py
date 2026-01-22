from packages import constants
from features import openURL

def args(args):
    fps = args.frame if not args.frame == 0 else 14
    bright = args.bright
    version = args.version

    color = args.color
    color = color.upper() if color.upper() in constants.SUPPORTEDCOLORS else "WHITE"
    openURL() if args.sound else None

    return fps, bright, color, version