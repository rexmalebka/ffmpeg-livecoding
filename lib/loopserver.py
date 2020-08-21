import os
import json

looperpath = os.environ.get('LOOPERPATH')
currentfilepath = os.path.join(looperpath, 'current')


def precheck():

    if looperpath is None:
        exit(1)

    if not os.path.exists(currentfilepath):
        os.mkfifo(currentfilepath)

def serve():
    loops = {}
    while True:
        loop = {}
        with open(currentfilepath,'r') as current:
            loop = current.read()
        try:
            loop = json.loads(loop)
        except json.decoder.JSONDecodeError:
            if "quit" in loop:
                break
        else:
            with open(currentfilepath,'w') as current:
                current.write(json.dumps(loop))
            print("WUW")

        print(loop)


precheck()
serve()
