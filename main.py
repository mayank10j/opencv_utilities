import cv2
from image_utils import Image_Utils
import numpy as np

imutils = Image_Utils()

im = cv2.imread("lena.jpg")
cv2.imshow("im", im)
cv2.waitKey(0)

blank_image = np.zeros((1000,100,3), np.uint8)
blank_image[:]= (255,255,255)

result_image = imutils.combine_img_horz(im, blank_image)
cv2.imshow("result_image", result_image)
cv2.waitKey(0)
