import os, cv2
import numpy as np
from glob import glob

# A function that receives the image, the row and column of the current pixel,
# the radius as the center index and the size of the square we are looking at.
# The function transforms its border elements into a binary vector starting at top left
# and returns the corresponding decimal value
def return_decimal_number(img, row, col, center, n):
    box = img[row:row+n, col:col+n]
    binary_matrix = (box >= box[center])*1.0

    vector = []
    value = 0
    # If the center (radius or R) is 1, look at the 8 surrounding pixels
    if(center == 1):
        vector.append(binary_matrix[center-1][center-1]) # Top left
        vector.append(binary_matrix[center-1][center]) # Top
        vector.append(binary_matrix[center-1][center+1]) # Top right
        vector.append(binary_matrix[center][center-1]) # Right 
        vector.append(binary_matrix[center+1][center+1]) # Bottom right
        vector.append(binary_matrix[center+1][center]) # Bottom
        vector.append(binary_matrix[center+1][center-1]) # Bottom left
        vector.append(binary_matrix[center][center-1]) # Left

        for i in range(0, len(vector)):
            add = 2**i * vector[i]
            value += add
            #print(add)

    # If the radius is 2, look at the 16 surrounding pixels
    # and normalize the value to between 0 and 255
    elif(center == 2):
        # Top row
        vector.append(binary_matrix[center-2][center-2])
        vector.append(binary_matrix[center-2][center-1])
        vector.append(binary_matrix[center-2][center])
        vector.append(binary_matrix[center-2][center+1])
        vector.append(binary_matrix[center-2][center+2])
        # Right side
        vector.append(binary_matrix[center-1][center+2])
        vector.append(binary_matrix[center][center+2])
        vector.append(binary_matrix[center+1][center+2])
        # Bottom row
        vector.append(binary_matrix[center+2][center+2])
        vector.append(binary_matrix[center+2][center+1])
        vector.append(binary_matrix[center+2][center])
        vector.append(binary_matrix[center+2][center-1])
        vector.append(binary_matrix[center+2][center-2])
        # Left side
        vector.append(binary_matrix[center+1][center-2])
        vector.append(binary_matrix[center][center-2])
        vector.append(binary_matrix[center-1][center-2])

        for i in range(0, len(vector)):
            add = 2**i * vector[i]
            value += add
            #print(add)
        # Divide the value by 256 to normalize
        value //= 256
    
    #print(box)
    #print(binary_matrix)
    #print(vector)
    #print(value)

    return value



# A function that receives a path to an image and a radius as parameters
# and returns the computed LBP matrix
def return_LBP(image_path, radius):
    # First we read the image, convert it into grayscale and resize it to a 128x128 resolution
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(gray_image, (128, 128))

    # Then we initialize the LBP matrix that will be returned at the end.
    # Also convert the radius to the dimensions of the square we will actually use in the algorithm
    LBP_matrix = np.zeros_like(img)
    n = radius*2 + 1

    #for i in range(60, 61):
    #    for j in range(60, 61):
    #        LBP_matrix[i+radius][j+radius] = returnDecimalNumber(img, i, j, radius, n)
    #        # For each pixel compute the decimal digit and write it to the prepared matrix
            


    # Iterate through the pixels in the image
    for i in range(0, img.shape[0] - n):
        for j in range(0, img.shape[1] - n):
            # For each pixel compute the decimal digit and write it to the prepared matrix
            LBP_matrix[i+radius][j+radius] = return_decimal_number(img, i, j, radius, n)
    # concatenate image Horizontally
    #Hori = np.concatenate((img, LBP_matrix), axis=1)
    #cv2.imshow('HORIZONTAL', Hori)
    #cv2.waitKey(0)
    return LBP_matrix

# A function that receives the computed LBP matrix as input and
# returns a histogram (vector of length 256) of the values
def return_histogram(image_path):
    LBP_matrix = return_LBP(image_path, 1)
    histogram = np.zeros(256)
    for i in range(len(LBP_matrix)):
        for j in range(len(LBP_matrix[0])):
            value = LBP_matrix[i][j]
            histogram[value] += 1
    return histogram



def return_all_images(path):
    return [y for x in os.walk(path) for y in glob(os.path.join(x[0], '*.png'))]

