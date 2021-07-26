# split video into single images
# Fire1.mp4
import cv2
vidcap = cv2.VideoCapture('data/Fire1.mp4')
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("data/fire/Fire1_frame%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1
 
# Fire2.mp4
vidcap = cv2.VideoCapture('data/Fire2.mp4')
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("data/fire/Fire2_frame%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1
  
# NoFire.mp4
vidcap = cv2.VideoCapture('data/NoFire.mp4')
success,image = vidcap.read()
count = 0
while success:
  cv2.imwrite("data/nofire/NoFire_frame%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = vidcap.read()
  print('Read a new frame: ', success)
  count += 1
