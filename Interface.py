import cv2
import numpy as np
from Leitor import Leitor


img = np.zeros((700, 1000, 3), dtype = np.uint8)

lojas = Leitor("lojas.txt")

# Create a named colour
red = [0,0,255]
blue = [255,0,0]
green = [0,255,0]

for i in range(len(lojas)):
    img = cv2.circle(img, (i+300,i+150), radius=5, color= red, thickness=-1)






# display the image using opencv
cv2.imshow('black image', img)
cv2.waitKey(0)

