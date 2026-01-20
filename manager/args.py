from packages import constants
import features

def args(args):
    fps = args.frame
    bright = args.bright
    version = args.version
    erase = args.erase

    color = args.color
    color = color.upper()
    
    if not color in constants.SUPPORTEDCOLORS:
        color = "WHITE"
    
    if args.sound:
        features.openURL()
    
    return fps, bright, color, version, erase