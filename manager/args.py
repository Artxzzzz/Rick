from packages import constants

def args(args):
    fps = args.frame
    bright = args.bright
    version = args.version

    color = args.color
    color = color.upper()
    
    if not color in constants.SUPPORTEDCOLORS:
        color = "WHITE"
    
    
    return fps, bright, color, version