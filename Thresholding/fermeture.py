import numpy as np
import sys
sys.path.append("C:/Users/LENOVO/Desktop/my python/TP_ traitement d'img/")

from Thresholding.dilation import dilate_this
from Thresholding.erosion import erode_this

def fermeture(img, level=3):
    img_d = dilate_this(img, dilation_level=level)
    img_e = erode_this(img_d, erosion_level=level)
    return img_e