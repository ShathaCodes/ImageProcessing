import numpy as np
import cv2 as cv
import sys
from matplotlib import pyplot as plt


sys.path.append("C:/Users/LENOVO/Desktop/my python/TP_ traitement d'img/")
from Thresholding.auto_threshholding import otsu
from Thresholding.manual_thresholding import manual_threshholding

def dilate_this(img, dilation_level=3):
    # setting the dilation_level
    dilation_level = 3 if dilation_level < 3 else dilation_level
    
    # obtain the kernel by the shape of (dilation_level, dilation_level)
    structuring_kernel = np.full(shape=(dilation_level, dilation_level), fill_value=255)
    th = otsu(img)
    image_src = manual_threshholding(img, s=th)

    orig_shape = image_src.shape
    pad_width = dilation_level - 2
    
    # pad the image with pad_width
    image_pad = np.pad(array=image_src, pad_width=pad_width, mode='constant')
    pimg_shape = image_pad.shape
    h_reduce, w_reduce = (pimg_shape[0] - orig_shape[0]), (pimg_shape[1] - orig_shape[1])
    
    # obtain the submatrices according to the size of the kernel
    flat_submatrices = np.array([
        image_pad[i:(i + dilation_level), j:(j + dilation_level)]
        for i in range(pimg_shape[0] - h_reduce) for j in range(pimg_shape[1] - w_reduce)
    ])
    
    # replace the values either 255 or 0 by dilation condition
    image_dilate = np.array([255 if (i == structuring_kernel).any() else 0 for i in flat_submatrices])
    # obtain new matrix whose shape is equal to the original image size
    image_dilate = image_dilate.reshape(orig_shape)
    
    return image_dilate