import serial
import cv2
import numpy as np

from support_functions import AsciiDecoder, NumpyEncoder
from TSPDecoder import *

rows, columns = 27, 19
TSP = TSPDecoder(rows=rows, columns=columns)

# make an empty buffer image
buffer_img = np.zeros([rows, columns])


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
    if AsciiDecoder(key) == 'q':
        cv2.destroyAllWindows()
        exit()
    if AsciiDecoder(key) == 'c':
        buffer_img = get_empty_buffer()
