import cv2

# get webcam video - 0 - meaning 1st webcam accessed from my MAC
video=cv2.VideoCapture(0)
success,frame=video.read()

#loading xml file for recognising faces
face_cascade=cv2.CascadeClassifier('faces.xml')
# param for video a new video from an existing one
height = frame.shape[0]
width = frame.shape[1]
# create an empty file/video
output=cv2.VideoWriter('video/output.avi',cv2.VideoWriter_fourcc(*'DIVX'),30,(width,height))
while success:
    # find diff sizes of the face
    faces=face_cascade.detectMultiScale(frame,1.1,4) # based on the frames
    #place this cordinates on the img
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),4)
    output.write(frame)
    success,frame=video.read() # get the next frame/img

# generate video and store it on MAC
output.release()


