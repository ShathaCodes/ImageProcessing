import numpy as np
import sys
sys.path.append("C:/Users/LENOVO/Desktop/my python/TP_ traitement d'img/")

from Thresholding.dilation import dilate_this
from Thresholding.erosion import erode_this

def ouverture(img, level=3):
    img_e = erode_this(img, erosion_level=level)
    img_d = dilate_this(img_e, dilation_level=level)
    return img_d