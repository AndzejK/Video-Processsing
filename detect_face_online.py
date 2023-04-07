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
output=cv2.VideoWriter('video/output_3.avi',cv2.VideoWriter_fourcc(*'DIVX'),10,(width,height)) # 15 number of frames per sec; however each camera is different and thus based on the camera type this number needs to be adjusted
count=0
while success:
    # find diff sizes of the face
    faces=face_cascade.detectMultiScale(frame,1.1,4) # based on the frames
    #place this cordinates on the img
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,255,255),4)
    # display video ONLINE
    cv2.imshow('Recording',frame)
    key=cv2.waitKey(1) # 1 ms
    # Setting a key "Q" to close/stop the video
    if key == ord('q'):
        break
    output.write(frame)
    success,frame=video.read() # get the next frame/img
    count+=1
    print(count)
# generate video and store it on MAC
output.release()
video.release()
cv2.destroyAllWindows()


