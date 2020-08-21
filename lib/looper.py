import os
import argparse
import json
import sys

looperpath = os.environ.get('LOOPERPATH')
currentfilepath = os.path.join(looperpath, "current")
def parse():
    parser = argparse.ArgumentParser()

    parser.add_argument("name",
                        help="name to suscribe looper",
                        type=str
                       )
    parser.add_argument("video",
                        help="video to play",
                        type=argparse.FileType('r')
                       )
    args = parser.parse_args()
    return args

def writecurrent(loopername, video):
    state = {"script": [], "name": loopername, "video":video }
    return state

args = parse()
state = writecurrent(args.name, args.video.name)

print(args.video.name)
print("--looper")
print(json.dumps(state))
