import cv2 as cv
import numpy as np
import sys

sys.path.append("C:/Users/LENOVO/Desktop/my python/TP_ traitement d'img/")

path="C:/Users/LENOVO/Desktop/my python/TP_ traitement d'img/images/"
from Thresholding.histogram import histogram
from read_write_histogram.histogram import histogram as histo

def otsu(img):
    
    if len(img.shape) >2:
        (ly,lx,rgb) = img.shape
        # calcul histo
        h0, h1, h2 = histogram(img, lx, ly )
    
        # Normalisation de l’histogramme obtenu
        N = ly*lx 
        h0 = [h0[i] / N for i in range(256)]
        h1 = [h1[i] / N for i in range(256)]
        h2 = [h2[i] / N for i in range(256)]

        th0 = compute(h0)
        th1 = compute(h1)
        th2 = compute(h2)

        return [th0, th1, th2]
    else :
        (ly,lx) = img.shape
        hist = histo(img, lx, ly)
        N = ly*lx 
        hist = [hist[i] / N for i in range(256)]

        th = compute(hist)

        return th


def compute(hist):
    w = [compute_zero_order_cumulative_moment(hist, i) for i in range(256)]
    u = [compute_first_order_cumulative_moment(hist, i) for i in range(256)]
    uT = compute_first_order_cumulative_moment(hist, 256) 

    variance_class_separability_max = -1 
    best_threesold = 0 

    for i in range(256):
        vk = compute_variance_class_separability(uT, w[i], u[i]) 
        if (vk > variance_class_separability_max):
            variance_class_separability_max = vk 
            best_threesold = i 

    return best_threesold


def compute_zero_order_cumulative_moment(hist, k):
    zero_order_cumulative_moment = 0 
    for i in range(k):
        zero_order_cumulative_moment += hist[i] 
    return zero_order_cumulative_moment 

def compute_first_order_cumulative_moment(hist, k):
    first_order_cumulative_moment = 0
    for i in range(k):
        first_order_cumulative_moment += i*hist[i]
    return first_order_cumulative_moment

def compute_variance_class_separability( uT, wk,  uk):
    if (wk*(1-wk)) != 0:
        return pow((uT*wk-uk),2) / (wk*(1-wk))
    return 0
