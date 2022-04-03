import numpy as np
import math

def analysepgm(img):
    moy = np.mean(img)
    var = math.sqrt(np.var(img))
    return moy, var