import cv2
import datetime
video=cv2.VideoCapture('video/video.mp4')

# given timestamp - 00:00:01.88 - then we're going to use FPS
fps=video.get(cv2.CAP_PROP_FPS)
nr_frames=video.get(cv2.CAP_PROP_FRAME_COUNT)
timestamp=input('Enter timestamp in hh:mm:ss format: ')

#convert timestamp into list having each value seperatly 
timestamp_list=timestamp.split(':')
hh,mm,ss=timestamp_list
# convert this values from str into floats
timestamp_list_floats=[float(i)for i in timestamp_list]
# put these values from the list timestamp_list_float into variables!!
hours,minutes,seconds=timestamp_list_floats

# create a formula where we can get frames based on a given time (s)
frame_nr=hours * 3600 * fps + minutes *60*fps+seconds*fps
#open the video but don't play it and set this video for this time
video.set(1,frame_nr)
succcess, frame=video.read()
cv2.imwrite(f'video/images/img_based_on_time/frame_at_{hh}:{mm}:{ss}.jpg',frame)