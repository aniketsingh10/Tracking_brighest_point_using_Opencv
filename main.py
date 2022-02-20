#This Program is to find the location of brightest point in an given image in pixels

#Importing the necessary modules
import cv2
import matplotlib.pyplot as plt
import numpy as np

print("\n|| *******---------------Finding Brighest Star---------------------****** ||")

#Reading of image and converting into a gray scale image
img=cv2.imread('sky.jpg',0)
#print(img)
cv2.imshow('output',img)
print("\n")

#Converting image into an array using numpy
img_array=np.array(img)
print("Array formed due to the given image:- ")
print(img_array,"\n")

#Using cv2MinMaxLoc to find the location of darkest and brightest point
final_img=cv2.minMaxLoc(img_array)
print("Output after using cv2MinMaxLoc :-",final_img)
print(" ")

#Image size in Pixel
print("The Total image size in Pixels :-",img_array.shape)
print(" ")

#Location of the brightest point
print("The location of the brightest point in pixels is :-",final_img[3])
print(" ")

#Intensity of the brightest point
print("The intensity of the brightest point is :-",final_img[1])

#plotting image
plt.imshow(img, cmap="gray")
plt.show()

#Closure of all the tasks performed
cv2.waitKey(0)
cv2.destroyAllWindows()

print("\n||++++----------------- || Thank You || -----------------++++||")
print("\n||####_________________ || Visit again || _______________####||")