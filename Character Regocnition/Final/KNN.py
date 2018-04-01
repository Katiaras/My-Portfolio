import warnings
import numpy as np
import cv2
from math import sqrt
import operator
import os
from collections import Counter


# dataset = {'k': [[1, 2], [2, 3], [3, 1]], 'r': [[6, 5], [7, 7], [8, 6]]}
# print(type(dataset))
# new_features = [1, 3]

def k_nearest_neighbors(data, predict, k=3):
    # print(len(data))
    k= len(data) +1
    if len(data)>= k:
        warnings.warn('K is set to a value less than total voting groups!')

    distances = []
    for group in data:
        for features in data[group]:
            # Euclidean Algorithm
            #   euclidean_distance = sqrt((features[0]-predict[0])**2 + (features[1]-predict[1])**2)

            # Dynamic Algorithm: Using Numpy Arrays
            #   np_euclidean_distance = np.sqrt(np.sum((np.array(features)-np.array(predict))**2))

            # Faster Version: Using Numpy Linear Algebra Algorithm
            ln_euclidean_distance = np.linalg.norm(np.array(features)-np.array(predict))

            # Appending the distances
            distances.append([ln_euclidean_distance, group])

    # print(distances)
    # print(sorted(distances))

    votes = [i[1] for i in sorted(distances)[:k]]
    # print(Counter(votes).most_common(1))
    # votes_result = Counter(votes).most_common(1)[0][0]

    return votes[0]


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
        npaFlattenedImages = np.loadtxt("flattened_images.txt", delimiter=" ")  # read in training images
    except:
        print("error, unable to open flattened_images.txt, exiting program\n")
        os.system("pause")
        return
    # end try


    # converting to numpy array
    npaClassifications = npaClassifications.reshape((npaClassifications.size, 1))

    # print("npaClassification")
    # print(npaClassifications)

    # print("npaFlattenedImages")
    # print(npaFlattenedImages)

    # print(npaFlattenedImages[0])

    # print(type(npaFlattenedImages))
    cv2.waitKey()
    print("*************************************Main Ends*******************************")

    dataset = {}
    counter = -1
    # dataset["kostas"] = [npaFlattenedImages[0]]
    # print(dataset)
    # dataset["kostas"].append(npaFlattenedImages[1])


    for i in npaClassifications:
        # Setting up a counter for accessing the Flattened Images
        counter += 1

        # Create a temporary character from the corresponding Classification
        tempChar = chr(i)

        # print(tempChar)
        # If key in the dataset exist, just append to its list
        # else instantiate a new key/value in the dictionary
        if tempChar in dataset.keys():
            dataset[tempChar].append(npaFlattenedImages[counter])
        else:
            dataset[tempChar] = [npaFlattenedImages[counter]]


    # print(dataset.keys())
    new_features = dataset["b"][0]
    result = k_nearest_neighbors(dataset, new_features, k=4)
    print(result)
print ("KNN is Imported")
# main()
def knn_dictionary_converter(Classifications, FlattenedImages):
    # declaring an empty dictionary
    dataset = {}
    counter = -1
    for i in Classifications:
        # Setting up a counter for accessing the Flattened Images
        counter += 1

        # Create a temporary character from the corresponding Classification
        tempChar = chr(i)

        # print(tempChar)
        # If key in the dataset exist, just append to its list
        # else instantiate a new key/value in the dictionary
        if tempChar in dataset.keys():
            dataset[tempChar].append(FlattenedImages[counter])
        else:
            dataset[tempChar] = [FlattenedImages[counter]]
    return dataset