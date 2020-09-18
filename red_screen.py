import cv2
import numpy as np
from time import sleep
capture=cv2.VideoCapture(0)
background=cv2.imread("background.jpg")
while True:
    ret,frame=capture.read()
    background=cv2.resize(background,(frame.shape[1],frame.shape[0]))
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    lower_red1=np.array([0,120,70])
    upper_red1=np.array([10,255,255])
    lower_red2=np.array([150,120,70])
    upper_red2=np.array([180,255,255])
    mask1=cv2.inRange(hsv,lower_red1,upper_red1)
    mask2=cv2.inRange(hsv,lower_red2,upper_red2)
    mask3=mask2+mask1
    mask4=cv2.morphologyEx(mask3,cv2.MORPH_OPEN,np.ones((3,3),np.uint8))
    mask5 = cv2.morphologyEx(mask4, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8))
    mask6=cv2.bitwise_not(mask5)
    res=cv2.bitwise_and(frame,frame,mask=mask6)
    res1=cv2.bitwise_and(background,background,mask=mask5)
    final=cv2.addWeighted(res1,1,res,1,0)
    cv2.imshow("Frame",final)
    if cv2.waitKey(1)==13:
        break
capture.release()
cv2.destroyAllWindows()
# # importinh the modules
# import cv2,time,numpy as np
# # capturing the live video
# capture=cv2.VideoCapture(0)
# # storing the background
# background=0
# # sleep for 3 sec
# time.sleep(3)
# for i in range(30):
#     ret,background=capture.read()
# # storing the background details in background
# # running into the loop
# while True:
#     # reading the capture
#     ret,image=capture.read()
#     # converting into hsv
#     hsv=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
#     # all the range for red color
#     lower_red1=np.array([0,120,70])
#     upper_red1=np.array([10,255,255])
#     lower_red2=np.array([170,120,70])
#     upper_red2=np.array([180,255,255])
#     # creating the mask
#     mask1=cv2.inRange(hsv,lower_red1,upper_red1)
#     mask2=cv2.inRange(hsv,lower_red2,upper_red2)
#     mask=mask1+mask2
#     # overall mask
#     mask3=cv2.morphologyEx(mask,cv2.MORPH_OPEN,np.ones((3,3),np.uint8))
#     mask4=cv2.morphologyEx(mask3,cv2.MORPH_DILATE,np.ones((3,3),np.uint8))
#     # remove the red
#     mask5=cv2.bitwise_not(mask4)
#     # the whole new capture
#     res=cv2.bitwise_and(image,image,mask=mask5)
#     # extracting the background into the capture
#     res2=cv2.bitwise_and(background,background,mask=mask4)
#     # adding both the resolution
#     final=cv2.addWeighted(res2,1,res,1,0)
#     # showing the Frame
#     cv2.imshow("Abhinav's Frame",final)
#     if cv2.waitKey(1)==13:
#         break
# capture.release()
# cv2.destroyAllWindows()