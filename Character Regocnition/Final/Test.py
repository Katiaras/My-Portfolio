import cv2
import numpy as np
import operator
import os
import KNN as knn
import constants as c
import Contour as cont



###################################################################################################
class ContourWithData():
    # member variables ############################################################################
    contour = None  # contour
    boundingRect = None  # bounding rect for contour
    intRectX = 0  # bounding rect top left corner x location
    intRectY = 0  # bounding rect top left corner y location
    intRectWidth = 0  # bounding rect width
    intRectHeight = 0  # bounding rect height
    fltArea = 0.0  # area of contour

    def calculateRectTopLeftPointAndWidthAndHeight(self):  # calculate bounding rect info
        [intX, intY, intWidth, intHeight] = self.boundingRect
        self.intRectX = intX
        self.intRectY = intY
        self.intRectWidth = intWidth
        self.intRectHeight = intHeight

    def checkIfContourIsValid(self):  # this is oversimplified, for a production grade program
        if self.fltArea < c.MIN_CONTOUR_AREA: return False  # much better validity checking would be necessary
        return True


def main():
    print("*************************************Main Starts*******************************")
    # Empty Variables for storing contours
    allContoursWithData = []  # declare empty lists,
    validContoursWithData = []  # we will fill these shortly

    # Loading Training Classifications
    try:
        npaClassifications = np.loadtxt("classifications.txt", np.float32)  # read in training classifications

    except:
        print("error, unable to open classifications.txt, exiting program\n")
        os.system("pause")
        return
    # end try

    # Loading Training Images
    try:
        npaFlattenedImages = np.loadtxt("flattened_images.txt", np.float32)  # read in training images
    except:
        print("error, unable to open flattened_images.txt, exiting program\n")
        os.system("pause")
        return
    # end try

    # converting to numpy array
    npaClassifications = npaClassifications.reshape((npaClassifications.size, 1))
    # print(npaClassifications)

    # Create a dictionary variable from the training data
    dataset = knn.knn_dictionary_converter(npaClassifications, npaFlattenedImages)
    print(dataset.keys())

    # Reading the testing image
    imgTestingNumbers = cv2.imread("test2.jpg")  # read in testing numbers image
    if imgTestingNumbers is None:  # if image was not read successfully
        print("error: image not read from file \n\n")  # print error message to std out
        os.system("pause")  # pause so user can see error message
        return  # and exit function (which exits program)
    # end if

    imgGray = cv2.cvtColor(imgTestingNumbers, cv2.COLOR_BGR2GRAY)  # get grayscale image
    imgBlurred = cv2.GaussianBlur(imgGray, (5, 5), 0)  # blur

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
    # the image

    imgContours, contours, npaHierarchy = cv2.findContours(imgThreshCopy,
                                                              # input image, make sure to use a copy since the
                                                              # function will modify this image in the course of
                                                              # finding contours
                                                              cv2.RETR_EXTERNAL,  # retrieve the outermost contours only
                                                              cv2.CHAIN_APPROX_SIMPLE)  # compress horizontal,
    # vertical, and diagonal segments and leave only their end points

    for contour in contours:  # for each contour
        contourWithData = cont.Contour()  # instantiate a contour with data object
        contourWithData.contour = contour  # assign contour to contour with data
        contourWithData.boundingRect = cv2.boundingRect(contourWithData.contour)  # get the bounding rect
        contourWithData.calculateRectTopLeftPointAndWidthAndHeight()  # get bounding rect info
        contourWithData.fltArea = cv2.contourArea(contourWithData.contour)  # calculate the contour area
        allContoursWithData.append(contourWithData)  # add contour with data object to list of all contours with data
    # end for

    for contourWithData in allContoursWithData:  # for all contours
        if contourWithData.checkIfContourIsValid():  # check if valid
            validContoursWithData.append(contourWithData)  # if so, append to valid contour list
        # end if
    # end for

    validContoursWithData.sort(key=operator.attrgetter("intRectX"))  # sort contours from left to right

    strFinalString = ""  # declare final string, this will have the final number sequence by the end of the program

    for contourWithData in validContoursWithData:  # for each contour
        # draw a green rect around the current char
        cv2.rectangle(imgTestingNumbers,  # draw rectangle on original testing image
                      (contourWithData.intRectX, contourWithData.intRectY),  # upper left corner
                      (contourWithData.intRectX + contourWithData.intRectWidth,
                       contourWithData.intRectY + contourWithData.intRectHeight),  # lower right corner
                      (0, 255, 0),  # green
                      2)  # thickness

        imgROI = imgThresh[contourWithData.intRectY: contourWithData.intRectY + contourWithData.intRectHeight,
                 # crop char out of threshold image
                 contourWithData.intRectX: contourWithData.intRectX + contourWithData.intRectWidth]

        imgROIResized = cv2.resize(imgROI, (c.RESIZED_IMAGE_WIDTH,
                                            c.RESIZED_IMAGE_HEIGHT))  # resize image, this will be more consistent for recognition and storage

        npaROIResized = imgROIResized.reshape(
            (1, c.RESIZED_IMAGE_WIDTH * c.RESIZED_IMAGE_HEIGHT))  # flatten image into 1d numpy array

        npaROIResized = np.float32(npaROIResized)  # convert from 1d numpy array of ints to 1d numpy array of floats
        # print(npaROIResized)
        CharResult = knn.k_nearest_neighbors(dataset, npaROIResized, k=4)  # get character from results
        print("Character is: " + CharResult)
        strFinalString = strFinalString + CharResult  # append current char to full string
    # end for

    print("\n" + strFinalString + "\n")  # show the full string

    cv2.imshow("imgTestingNumbers", imgTestingNumbers)  # show input image with green boxes drawn around found digits

    cv2.waitKey(0)  # wait for user key press
    print("*************************************Main Ends*******************************")


main()
