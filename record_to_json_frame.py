import time
import json
import os
import cv2
import numpy as np
from TSPDecoder import *
from support_functions import AsciiDecoder, NumpyEncoder

data = []

# setup TSP Decoder
rows, columns = 27, 19
TSP = TSPDecoder(rows=rows, columns=columns)

# gobals
buffer_img = np.zeros((rows,columns))
separation = False
current_digit = 0

def save_to_json(time_stamp, label, separation, image):
    # maybe do a check if the values are of the correct type etc??

    """"We have to create a dictionary with our data"""
    # # Serializing json+
    # json_object = json.dumps(dictionary, indent=?????)
    #
    # # Writing to sample.json
    # with open("digits.json", "w") as outfile:
    #     outfile.write(json_object)

    # after saving reset the separation variable
    if(separation == True):
        separation = False


def start_new_digit(digit):
    global current_digit
    current_digit = digit

    separation = True
    buffer_img = get_empty_buffer()

def update_buffer_keep_max(img):
    """
    Overwrite image when pixel value is greater than the value in the buffer
    Returns: None
    """
    # loop through all pixels
    for row in range(rows - 1):
        for pixel in range(columns - 1):
            # when pixel value of img is greater than the buffer pixel -> overwrite buffer
            if img[row][pixel] > buffer_img[row][pixel]:
                buffer_img[row][pixel] = img[row][pixel]

            # return true when a new pixel has been drawn


def get_empty_buffer():
    """
    Set the buffer to an empty image
    Returns: Empty Array
    """
    return np.zeros([rows, columns])

while TSP.available():
    # update buffer
    update_buffer_keep_max(TSP.readFrame())

    # convert input to int8 and resize the buffer
    resized_buffer = cv2.resize(buffer_img.astype(np.uint8),(500,600))

    cv2.imshow("Cool visualizer", resized_buffer)
    key = cv2.waitKey(20)

    # handle inputs
    match AsciiDecoder(key):
        case 'q':
            # quit
            cv2.destroyAllWindows()
            exit()
        case 'c':
            # clear buffer
            buffer_img = get_empty_buffer()
        case '0':
            start_new_digit(0)
        case '1':
            start_new_digit(1)
        case '2':
            start_new_digit(2)
        case '3':
            start_new_digit(3)
        case '4':
            start_new_digit(4)
        case '5':
            start_new_digit(5)
        case '6':
            start_new_digit(6)
        case '7':
            start_new_digit(7)
        case '8':
            start_new_digit(8)
        case '9':
            start_new_digit(9)

