import argparse

def manageArgs():
    parser = argparse.ArgumentParser(description="Rick")

    parser.add_argument("-c", "--color", type=str, default="White", help="Set color")
    parser.add_argument("-f", "--frame", type=int, default=14, help="Set frames")
    
    args = parser.parse_args()

    return args