import cv2

# find a face on the video and replace it with a cat picture

video=cv2.VideoCapture('video/video-sample.mp4')
success,frame=video.read()

#loading xml file for recognising faces
face_cascade=cv2.CascadeClassifier('faces.xml')
# param for video a new video from an existing one
height = frame.shape[0]
width = frame.shape[1]
# create an empty file/video
output=cv2.VideoWriter('video/output-blurred.avi',cv2.VideoWriter_fourcc(*'DIVX'),30,(width,height))
count_fr=0
while success:
    # find diff sizes of the face
    faces=face_cascade.detectMultiScale(frame,1.1,4) # based on the frames
    #place this cordinates on the img
    for (x,y,w,h) in faces:
        frame[y:y+h,x:x+w]=cv2.blur(frame[y:y+h,x:x+w],(50,50))
    output.write(frame)
    success,frame=video.read() # get the next frame/img
    count_fr+=1
    print(count_fr)

# generate video and store it on MAC
output.release()
video.release()
cv2.destroyAllWindows()

