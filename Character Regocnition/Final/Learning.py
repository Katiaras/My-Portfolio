# Name: Kostas Giouzakov
# Senior Project: Character Recognition

import sys
import numpy as np
import cv2
import os
from math import sqrt
import constants as c
import image_manipulation as ip

print("Learning Started")
def main():
    # Read the Training Characters
    imgTrainingCharacters = ip.LoadImage("learning.jpg")  # read in training numbers image
    # Show the Image
    # cv2.imshow('Original', imgTrainingCharacters)

    # the idea is to get accurate number of contours
    # for that, some pre=processing has to be done to the image first: GrayScale-Blur...

    imgThresh = ip.ImageToThreshold(imgTrainingCharacters)  # make a copy of the thresh image, this in necessary b/c
    # findContours() modifies the image

    imgContours, npaContours, npaHierarchy = cv2.findContours(imgThresh,
                                                              # input image, make sure to use a copy since the
                                                              # function will modify this image in the course of
                                                              # finding contours
                                                              cv2.RETR_EXTERNAL,  # retrieve the outermost contours only
                                                              cv2.CHAIN_APPROX_SIMPLE)  # compress horizontal,
    # vertical, and diagonal segments and leave only their end points

    print("Number of detected contours  %d " % len(npaContours))

    # declare empty numpy array, we will use this to write to file later
    # zero rows, enough cols to hold all image data
    npaFlattenedImages = np.empty((0, c.RESIZED_IMAGE_WIDTH * c.RESIZED_IMAGE_HEIGHT))

    intClassifications = []  # declare empty classifications list, this will be our list of how we are classifying
    # our chars from user input, we will write to file at the end

    # possible chars we are interested: All characters (eventually)
    intValidChars = c.VALID_CHARS

    # counter is used for pictures labeling
    counter = 0
    for npaContour in npaContours:  # for each contour detected
        if cv2.contourArea(npaContour) > c.MIN_CONTOUR_AREA:  # if contour is big enough to consider
            [intX, intY, intW, intH] = cv2.boundingRect(npaContour)  # get and break out bounding rect

            counter += 1

            # draw rectangle around each contour as we ask user for input
            cv2.rectangle(imgTrainingCharacters,  # draw rectangle on original training image
                          (intX, intY),  # upper left corner
                          (intX + intW, intY + intH),  # lower right corner
                          (0, 0, 255),  # red
                          2)  # thickness

            imgROI = imgThresh[intY:intY + intH, intX:intX + intW]  # crop char out of threshold image
            imgROIResized = cv2.resize(imgROI, (c.RESIZED_IMAGE_WIDTH,
                                                c.RESIZED_IMAGE_HEIGHT))  # resize image, this will be more consistent
            # for recognition and storage

            cv2.imshow("imgROI", imgROI)  # show cropped out char for reference
            cv2.imshow("imgROIResized", imgROIResized)  # show resized image for reference
            cv2.imshow("Training Characters.png",
                       imgTrainingCharacters)  # show training numbers image, this will now have red rectangles drawn on it

            intChar = cv2.waitKey(0)  # get key press

            if intChar == 27:  # if esc key was pressed
                sys.exit()  # exit program
            elif intChar in intValidChars:  # else if the char is in the list of chars we are looking for . . .

                intClassifications.append(
                    intChar)  # append classification char to integer list of chars (we will convert to float later
                # before writing to file)

                npaFlattenedImage = imgROIResized.reshape((1,
                                                           c.RESIZED_IMAGE_WIDTH * c.RESIZED_IMAGE_HEIGHT))  # flatten
                # image to 1d numpy array so we can write to file later
                npaFlattenedImages = np.append(npaFlattenedImages, npaFlattenedImage,
                                               0)  # add current flattened impage numpy array to list of flattened
                # image numpy arrays

            # end if
        # end if
    # end for

    print("\n\nTraining complete!!\n")
    print("\n\nSaving...\n")

    fltClassifications = np.array(intClassifications,
                                  np.float32)  # convert classifications list of ints to numpy array of floats

    npaClassifications = fltClassifications.reshape(
        (fltClassifications.size, 1))  # flatten numpy array of floats to 1d so we can write to file later
    cv2.waitKey(0)

    np.savetxt("classifications.txt", npaClassifications)  # write flattened images to file
    np.savetxt("flattened_images.txt", npaFlattenedImages)  #

    cv2.destroyAllWindows()  # remove windows from memory

    print("\n\nSave Complete!!\n")


    cv2.waitKey(0)
    return
main()
