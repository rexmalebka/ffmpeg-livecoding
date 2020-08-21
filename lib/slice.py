import sys
import argparse
import ffmpeg
import json
from spread import spread

def check_timing(video, start, timestamp, parser):
    inp = ffmpeg.probe(video.name)
    duration = float(inp['format']['duration'])

    if start < 0:
        parser.error("start '{}' must be > 0 ".format(start))

    if timestamp < 0:
        parser.error("timestamp '{}' must be > 0 ".format(timestamp))

    if start > duration:
        parser.error("start '{}' out of range '{}'".format(start, duration))

    if start + timestamp > duration:
        parser.error("start + timestamp'{}'+'{}'  out of range    '{}'".format(start, timestamp, duration))

def execute(start, timelapse, looper):
    if looper.get('spread') is not None:
        start, timelapse = spread(start, timelapse, looper.get('spread'))
    else:
        start, timelapse = spread(start, timelapse)

    looper['script'].extend([{'slice': {"start": st, "end": st+tl }} for st, tl in zip(start, timelapse)])
    return looper


def parse():
    parser = argparse.ArgumentParser()
        
    parser.add_argument("video", 
                        help="video to slice to", 
                        type=argparse.FileType('r')
                       )
    parser.add_argument("--looper",
                        help="looper to suscribe to.", 
                        nargs='?',
                        type=json.loads,
                        required= False,
                        default={"script":[]}
                       )
    if not '-' in sys.argv:
        parser.add_argument("start", 
                            help="start of the slice", 
                            default=0,
                            type=float #type=CustomFfmpegTimeType()
                           )
        parser.add_argument("timestamp", 
                            help="timestamp of the slice", 
                            default=1,
                            type=float
                           )
    else:
        parser.add_argument("start", 
                            help="array of starting points for slicing.", 
                            nargs='+',
                            type=float #type=CustomFfmpegTimeType()
                           )
        parser.add_argument("-",
                            dest="timestamp",
                            help="array of timestamp points for slicing.", 
                            nargs='+',
                            type=float
                           )
    
    
    args = parser.parse_args()
    if type(args.start) is list:
        minstart = min(args.start)
        maxstart = min(args.start)

        minlapse = min(args.timestamp)
        maxlapse = max(args.timestamp)

        check_timing(args.video, minstart, minlapse, parser)
        check_timing(args.video, maxstart, maxlapse, parser)
    return args
 

if __name__ == '__main__':
    args = parse()

    video = args.video
    start = args.start
    timelapse = args.timestamp
    looper = args.looper
    
    if type(start) is float:
        start = [start]

    if type(timelapse) is float:
        timelapse = [timelapse]

    looper = json.dumps(execute(start, timelapse, looper))
    print(video.name)
    print("--looper")
    print(looper)
    
