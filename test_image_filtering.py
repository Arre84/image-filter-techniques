"""
test_image_filtering.py
The following script implements functions from another py script to load and visualize an image
with the argparse and opencv library, also implementing a filter specified by the user, the filters 
can be: Averag, Median and gaussian, specifying the kernel_size for it, then it visualizes both the original
and filtered image.

Author: Emilio Arredondo Payán #628971
Contact: emilio.arredondop@udem.edu
Institution: Universidad de Monterrey
First created on saturday 09 2024
"""

import numpy as np
import argparse as arg
import cv2 
import cvlib as cv
from numpy.typing import NDArray

#Function to apply average filter
def average_filter(img:NDArray, kernel:int)->NDArray:
    average_image= cv2.blur(img,(kernel,kernel))
    return average_image

#Function to apply gaussian filter
def gaussian_filter(img:NDArray, kernel:int)->NDArray:
    gaussian_image = blur = cv2.GaussianBlur(img,(kernel,kernel),0)
    return gaussian_image

#Function to apply median filter
def meadian_filter(img:NDArray,kernel:int)->NDArray:
    median_image = cv2.medianBlur(img,kernel)
    return median_image

#Function to select filter
def filter(filter_name:str, img:NDArray, kernel_size:np.int_=5)->NDArray:
    assert kernel_size%2 == 1, "Incorrect, kernel size must be odd"  #We check for the kernel size to be odd so that the program doesn't crash

    match filter_name.lower(): #We match every possibility with lower case
        case "average":
            return average_filter(img,kernel_size)
        case "median":
            return meadian_filter(img,kernel_size)
        case "gaussian":
            return gaussian_filter(img,kernel_size)
        case _:                 #In case none of the cases matched the program will shut down 
            print("Not valid filter")
            exit(-1)


def pipeline():
    args = cv.parse_user_data()     #We ask for the filter,kernel size and image
    img = cv.load_image(args.input_image) #Load the image
    filtered_image = filter(args.filter,img,kernel_size=args.kernel_size) #select the filter to use
    cv.visualise_image(img,"Original image")
    cv.visualise_image(filtered_image,"Filtered image")
    cv.close_windows()
    return 0

if __name__ == "__main__":
    pipeline()
    print("Script ended succesfully")