import sys
import argparse
import os
import json

looperpath = os.environ.get('LOOPERPATH')

def parse():
    parser = argparse.ArgumentParser()

    parser.add_argument("video", 
                        help="the video to play", 
                        type=argparse.FileType('r')
                       )

    parser.add_argument("--looper",
                        help="looper to suscribe to.", 
                        nargs='?',
                        type=json.loads,
                        required= False,
                        default={"script":[]}
                       )   

    args = parser.parse_args()
    return args

def readlooper():
    state = {}
    with open(currentfilepath, 'r') as current:
        state = json.loads(current.read())

    print("STATE", state)


args = parse()
#readlooper()
print("playin uwu")
