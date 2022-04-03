import numpy as np

def histogram(img, lx, ly):
    histo = np.zeros(np.max(img)+1, dtype=int) # init histogram of all possible grey values to all zero
    for i in range(ly):
        for j in range(lx):
            histo[img[i][j]] += 1
    return histo


def histogramC(histo):
    hc = np.copy(histo)
    for i in range(1,len(histo)):
        hc[i] += hc[i-1]
    return hc