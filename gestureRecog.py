#Program for creating training data

import numpy as np
import cv2
import os

cap = cv2.VideoCapture(0)
count = 0
inc = 0

dir_name = input("What character would you like to create a training data set for? Enter value: ")
try:
    os.mkdir(dir_name)
except OSError:
    print("ERROR: Unable to create directory for new character")
else:
    print("New character directory created.")

while(cap.isOpened()):
    # Capture frame-by-frame
    ret, frame, = cap.read()
    height, width, channels = frame.shape

    # Our operations on the frame come here
    picname = str(dir_name) + "/pic_" + str(inc) + ".png"

    if inc < 1:
        x1 = int((1/3)*width)
        y1 = int((2/3)*height)
        x2 = int((2/3)*width)
        y2 = int((1/3)*height)

    # Display the resulting frame
    cv2.rectangle(frame,(x1,y1),(x2, y2),(0,255,0),3)
    cv2.imshow('frame',frame)


    if cv2.waitKey(20) & 0xFF == ord('q'):
        break


    if (count % 30) == 0:
        cv2.imwrite(picname, frame)

    count = count + 1
    inc = inc + 1
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
