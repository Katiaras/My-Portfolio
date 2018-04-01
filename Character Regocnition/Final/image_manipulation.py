import numpy as np
import cv2
import os


# Loads the images / Checks if it exists
def LoadImage(name):
    # Read the Training Characters ##################################################################
    imgTrainingNumbers = cv2.imread(name)  # read in training numbers image
    print(imgTrainingNumbers)
    # checking for if read correctly
    if imgTrainingNumbers is None:  # if image was not read successfully
        print("error: image not read from file \n\n")  # print error message
        os.system("pause")  # pause so user can see error message
        return  # exit main function
    # end if

    return imgTrainingNumbers

# Returns a Trheshold copy of the image after Converting the img to GRAYSCALE and Blurred first
def ImageToThreshold(originalImage):
    imgGray = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)  # get grayscale image
    # cv2.imshow('Gray Scale', imgGray)

    imgBlurred = cv2.GaussianBlur(imgGray, (5, 5), 0)  # blur
    # cv2.imshow('Blurred', imgBlurred)

    # filter image from grayscale to black and white
    imgThresh = cv2.adaptiveThreshold(imgBlurred,  # input image
                                      255,  # make pixels that pass the threshold full white
                                      cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                      # use gaussian rather than mean, seems to give better results
                                      cv2.THRESH_BINARY_INV,
                                      # invert so foreground will be white, background will be black
                                      11,  # size of a pixel neighborhood used to calculate threshold value
                                      2)  # constant subtracted from the mean or weighted mean

    imgThreshCopy = imgThresh.copy()  # make a copy of the thresh image, this in necessary b/c findContours modifies
    # cv2.imshow('Black n White', imgThresh)
    return imgThreshCopy