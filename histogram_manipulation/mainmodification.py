import cv2 as cv
import sys
sys.path.append("C:/Users/LENOVO/Desktop/my python/TP_ traitement d'img/")
from  read_write_histogram.readPGM import readPGM
from read_write_histogram.writePGM import writePGM
from modificationcontraste import contraste

path="C:/Users/LENOVO/Desktop/my python/TP_ traitement d'img/images/"


img1 = cv.imread(path+'example.pgm') 
cv.imshow("Test", img1)

img,lx,ly=readPGM(path+'example.pgm')

imgclair=contraste(img,lx,ly,[70,50],[120,100])
writePGM(imgclair, path+ "dilatationzoneclair.pgm",lx,ly, "P2")
imgclair = cv.imread(path+ "dilatationzoneclair.pgm") 
cv.imshow("dilatationzoneclair.pgm", imgclair)

imgsombre=contraste(img,lx,ly,[50,200],[200,240])
writePGM(imgsombre, path+"dilatationzonesombre.pgm",lx,ly, "P2")
imgsombre = cv.imread(path+"dilatationzonesombre.pgm") 
cv.imshow("dilatationzonesombre.pgm", imgsombre)

imgmilieu=contraste(img,lx,ly,[50,200],[200,240])
writePGM(imgsombre, path+ "dilatationzonesmilieu.pgm",lx,ly, "P2")
imgmilieu = cv.imread(path+"dilatationzonemilieu.pgm") 
cv.imshow("dilatationzonemilieu.pgm", imgsombre)

imginverse=contraste(img,lx,ly,[1,255],[254,0])
writePGM(imginverse, path+ "inversionimage.pgm",lx,ly, "P2")
imginverse = cv.imread(path+ "inversionimage.pgm") 
cv.imshow("inversionimage.pgm", imginverse)

cv.waitKey()