import numpy as np
import cv2

img = cv2.imread('Lee-Minpic.jpg')
mask = cv2.imread('distortion.jpg',0)

dst = cv2.inpaint(img,mask,3,cv2.INPAINT_TELEA)
cv2.imshow('Extracted',dst)
cv2.imshow('Distorted',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
