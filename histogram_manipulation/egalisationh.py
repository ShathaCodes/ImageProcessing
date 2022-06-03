import numpy as np
import sys

from read_write_histogram.histogram import histogram, histogramcumul
def egalisation(img,lx,ly):
    k=img.max()
    h=histogram(img,lx,ly)
    hc=histogramcumul(h,k)
    max=hc[k]
    hc=np.array(hc)
    n1 = np.trunc(k * hc/max)
    #print("n1=",n1)
    heg=[0 for i in range (img.max() +1)]
    for i in range (img.max() +1):
        for j in range (img.max() +1):
            if n1[j]== i:
                heg[i]+=h[j]
    return heg

def modif_image(img,lx,ly):
    imgn = np.copy(img)
    heg=egalisation(img,lx,ly)
    for i in range (ly):
        for j in range (lx):
            imgn[i][j]=heg[img[i][j]]
    return imgn



