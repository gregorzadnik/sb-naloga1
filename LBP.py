import os, cv2
import numpy as np


# A function that receives a path to an image and a radius as parameters
# and returns the computed LBP matrix
def returnLBP(image_path, radius):
    # First we read the image, convert it into grayscale and resize it to a 128x128 resolution
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(gray_image, (128, 128))

    print(img.shape)
    # Then we initialize the LBP matrix that will be returned at the end.
    # Also convert the radius received to the dimensions of the square we will use in the algorithm
    LBP_matrix = np.zeros_like(img)
    n = radius*2 + 1
    for i in range(0, img.shape[0] - n):
        for j in range(0, img.shape[1] - n):
            print(f"{img[i][j]} ", end="")

        print()
    
    #cv2.imshow('image', img)
    #cv2.waitKey(0)



path = ".\\awe\\001\\02.png"
returnLBP(path, 1)