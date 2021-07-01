
#from __future__ import print_function

import numpy as np
import cv2
from matplotlib import pyplot as plt

save_shape = (300, 100)


i = 1
if i==1:
  # load png file
  img = cv2.imread('car_030.png', 0)
  img = cv2.flip(img, 1)
  #if img is None:
    #break
  resized_img = cv2.resize(img, save_shape)
  resized_img = -(resized_img/255.0) + 1

  # write to txt file
  f1=open('car_030.txt', 'w+')
  f1.write(str(save_shape[0]) + ' ')
  f1.write(str(save_shape[1]) + ' ')
  for x in range(save_shape[0]):
    f1.write( '\n')
    for y in range(save_shape[1]):
      if resized_img[y,x] > .5:
        f1.write(str(1) + ' ')
      if resized_img[y,x] < .5:
        f1.write(str(0) + ' ')

  i += 1



