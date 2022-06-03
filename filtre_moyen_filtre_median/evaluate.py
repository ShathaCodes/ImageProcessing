import numpy as np
import math

def calculateSignalToNoiseRatio(img,new_img):
    moyenne = np.mean(img)
    s1 = np.sum((img-moyenne)**2)
    s2 = np.sum((new_img-img)**2)
    sb = math.sqrt(s1/s2)
    print(sb)
    return sb