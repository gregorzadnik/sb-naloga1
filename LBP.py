import os, cv2
import numpy as np

# A function that receives a matrix of 1s and 0s,
# transforms its border elements into a binary vector starting at top left
# and returns the corresponding decimal value
def returnDecimalNumber(img, row, col, center, n):
    box = img[row:row+n, col:col+n]
    binary_matrix = (box >= box[center])*1.0
    vector = []
    vector.append(binary_matrix[center-1][center-1])
    vector.append(binary_matrix[center-1][center])
    vector.append(binary_matrix[center-1][center+1])
    vector.append(binary_matrix[center][center-1])
    vector.append(binary_matrix[center+1][center+1])
    vector.append(binary_matrix[center+1][center])
    vector.append(binary_matrix[center+1][center-1])
    vector.append(binary_matrix[center][center-1])
    print(box)
    print(binary_matrix)
    print(vector)
    

   


# A function that receives a path to an image and a radius as parameters
# and returns the computed LBP matrix
def returnLBP(image_path, radius):
    # First we read the image, convert it into grayscale and resize it to a 128x128 resolution
    image = cv2.imread(image_path)
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    img = cv2.resize(gray_image, (128, 128))

    # Then we initialize the LBP matrix that will be returned at the end.
    # Also convert the radius to the dimensions of the square we will actually use in the algorithm
    LBP_matrix = np.zeros_like(img)
    n = radius*2 + 1

    for i in range(60, 61):
        for j in range(60, 61):
            returnDecimalNumber(img, i, j, radius, n)
            # For each pixel compute the decimal digit and write it to the prepared matrix
            


    # Iterate through the pixels in the image
    #for i in range(0, img.shape[0] - n):
    #    for j in range(0, img.shape[1] - n):
    #        # For each pixel compute the decimal digit and write it to the prepared matrix
    #        box = img[i:i+n, j:j+n]
    #        center = img[radius][radius]

    
    #cv2.imshow('image', img)
    #cv2.waitKey(0)



path = ".\\awe\\001\\02.png"
returnLBP(path, 1)