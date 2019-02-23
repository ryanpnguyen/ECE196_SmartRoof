# USAGE
# python bright.py --image images/retina.png --radius 41
# python bright.py --image images/retina-noise.png --radius 41
# python bright.py --image images/moon.png --radius 61

# import the necessary packages
import numpy as np
import argparse
import cv2
import pygame

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", help = "path to the image file")
ap.add_argument("-r", "--radius", type = int,
	help = "radius of Gaussian blur; must be odd")
args = vars(ap.parse_args())

# load the image and convert it to grayscale
image = cv2.imread(args["image"])
orig = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

img = pygame.image.load(args["image"])
width = img.get_width()
height = img.get_height()
middle = int(width/2)
#print(width)
#print(height)

## perform a naive attempt to find the (x, y) coordinates of
## the area of the image with the largest intensity value
#(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
#cv2.circle(image, maxLoc, 5, (255, 0, 0), 2)
#
## display the results of the naive attempt
#cv2.imshow("Naive", image)

# apply a Gaussian blur to the image then find the brightest
# region
gray = cv2.GaussianBlur(gray, (args["radius"], args["radius"]), 0)
(minVal, maxVal, minLoc, maxLoc) = cv2.minMaxLoc(gray)
image = orig.copy()
cv2.circle(image, maxLoc, args["radius"], (255, 0, 0), 2)
#cv2.line(image,(0,0),(511,511),(255,0,0),5)
print(maxLoc) #Print location of the sun
print(type(maxLoc))
x = maxLoc[0]
print(x)
print(middle)
cv2.line(image,(x, 0),(x, height),(255,0,0),2) #x position of sun line
cv2.line(image,(middle, 0),(middle, height),(0,255,0),2) #middle line
distance = x - middle
print(distance)


# display the results of our newly improved method
cv2.imshow("Image", image)
cv2.waitKey(0)