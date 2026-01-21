from packages import constants
import features

def args(args):
    fps = args.frame
    bright = args.bright
    version = args.version

    color = args.color
    color = color.upper() if color.upper() in constants.SUPPORTEDCOLORS else "WHITE"
    features.openURL() if args.sound else None

    return fps, bright, color, version