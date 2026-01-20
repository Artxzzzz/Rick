import argparse

def getArgs():
    parser = argparse.ArgumentParser(description="Rick")

    parser.add_argument("-c", "--color", type=str, default="White", help="Set color")
    parser.add_argument("-f", "--frame", "--speed", type=int, default=14, help="Set frames")
    parser.add_argument("-v", "--version", nargs="?", const=True, default=False, type=bool, help="Show version")
    parser.add_argument("-b", "--bright", nargs="?", const=True, default=False, type=bool, help="Set bright")
    parser.add_argument("-s", "--sound", nargs="?", const=True, default=False, type=bool, help="Open youtube url from rick")
    parser.add_argument("-e", "--erase", nargs="?", const=False, default=True, type=bool, help="Disable the erase previous frame option")
    
    args = parser.parse_args()

    return args
