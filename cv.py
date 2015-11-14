#!/usr/bin/env python

import cv2

# camera = cv2.VideoCapture(1)
# video  = cv2.VideoWriter('video.avi', -1, 25, (640, 480));
# while True:
#    f,img = camera.read()
#    video.write(img)
#    cv2.imshow("webcam",img)
#    if (cv2.waitKey(5) != -1):
#        break
# video.release()    

camera = cv2.VideoCapture(1)
i = 0
while True:
   f,img = camera.read()
   cv2.imshow("webcam",img)
   if (cv2.waitKey(5) != -1):
       break
   cv2.imwrite('images/{0:05d}.jpg'.format(i),img)
   i += 1