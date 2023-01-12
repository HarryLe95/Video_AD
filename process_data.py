import argparse 
import cv2 

def parse_args():
    parser = argparse.ArgumentParser("Video to Frame")
    parser.add_argument("--video","-v", help="Input video.", type=str,default="RawData/TimelapseVideo.mp4")
    parser.add_argument("--make_frames","-f",action='store_false')
    args = parser.parse_args()
    return args 

def split_frames(args):
    vidcap = cv2.VideoCapture(args.video)
    success,image = vidcap.read()
    count = 0
    while success:
        cv2.imwrite(f"RawData/Frames/frame{count}.jpg", image)     # save frame as JPEG file      
        success,image = vidcap.read()
        print(f'Make frame: {count}: {success}')
        count += 1
        
def main(args):
    if args.make_frames:
        split_frames(args)

if __name__ == "__main__":
    args = parse_args()
    main(args)
    