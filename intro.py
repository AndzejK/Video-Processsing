# frames think of them as images
# if the video's duration is 3 sec and video has 90 imgs/frames that means this video has 30 frames per sec (90/3=30frames/s) = fps [frames per second]
import cv2
video=cv2.VideoCapture('video/video.mp4')
# General Info about video.mp4
width=int(video.get(cv2.CAP_PROP_FRAME_WIDTH)) # 1920.0
height=int(video.get(cv2.CAP_PROP_FRAME_HEIGHT)) # 1080
nr_frames=video.get(cv2.CAP_PROP_FRAME_COUNT) # 90 
fps=video.get(cv2.CAP_PROP_FPS) # 30 

# we're going to extract those 90 images which are stuck in the video
print(video.read()) # tuple-> 3 values: 1- Boolean, 2- List, 3-dtype

# write these imgs
success,frame=video.read()
count=1
while success:
    cv2.imwrite(f'video/images/{count}.jpg',frame)
    success,frame=video.read()
    count+=1

