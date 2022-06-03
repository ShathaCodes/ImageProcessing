
import cv2 as cv
import sys


sys.path.append("C:/Users/LENOVO/Desktop/my python/TP_ traitement d'img")

from filtre_moyen_filtre_median.bruit import bruit
from read_write_histogram.writePGM import writePGM
from  read_write_histogram.readPGM import readPGM
from filtre_moyen_filtre_median.filtre import medianFiltre, moyennefilter
path="C:/Users/LENOVO/Desktop/my python/TP_ traitement d'img/images/"

img1 = cv.imread(path+'coins.pgm') 
cv.imshow("Test", img1)
img,lx,ly=readPGM(path+'coins.pgm')
imgb=bruit(img,lx,ly)

writePGM(imgb, path+"bruit.pgm",lx,ly, "P2")
imgbruit = cv.imread(path+"bruit.pgm") 
cv.imshow("bruit.pgm", imgbruit)

imgm=moyennefilter(img,lx,ly,5)
writePGM(imgm, path+"filtermoyenne.pgm",lx,ly, "P2")
imgfiltermoy = cv.imread(path+"filtermoyenne.pgm") 
cv.imshow("filtermoyenne.pgm", imgfiltermoy)

new_img = medianFiltre(imgb,lx,ly,3)

writePGM(new_img, path+"new_img.pgm",lx,ly, "P2")
new_img_file = cv.imread(path+"new_img.pgm") 
cv.imshow("Median Filter", new_img_file)


cv.waitKey()