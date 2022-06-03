import cv2 as cv
import numpy as np
import sys

sys.path.append("C:/Users/LENOVO/Desktop/my python/TP_ traitement d'img/")

from Thresholding.manual_thresholding import manual_threshholding
from Thresholding.auto_threshholding import otsu
from Thresholding.dilation import dilate_this
from Thresholding.erosion import erode_this
from Thresholding.ouverture import ouverture
from Thresholding.fermeture import fermeture
from read_write_histogram.readPGM import readPGM
from read_write_histogram.writePGM import writePGM

path="C:/Users/LENOVO/Desktop/my python/TP_ traitement d'img/images/"

#---------------------------------------------------------- Manual threshholding
img = cv.imread(path+'snail.ppm') 
cv.imshow("landscape", img)
new_img = manual_threshholding(img, 150, 150, 150)
cv.imshow("M Th", new_img)

#new_img_and = manual_threshholding(img, 150,150,150,"AND")
#cv.imshow("M Th AND", new_img_and)

#new_img_or = manual_threshholding(img, 100,150,150,"OR")
#cv.imshow("M Th OR", new_img_or)

#---------------------------------------------------------- Auto threshholding
[th0, th1, th2] = otsu(img)
print(th0," ", th1," ", th2) # 129   142   162
img2 = manual_threshholding(img, th2, th1, th0 )
cv.imshow("Auto th", img2)

#---------------------------------------------------------- 
image_src, lx, ly = readPGM(path+'coins.pgm')


img_d = dilate_this(np.copy(image_src), dilation_level=3)
writePGM(img_d,path+ "dilated.pgm",lx,ly,"P2")
dilated_img = cv.imread(path+ "dilated.pgm")
cv.imshow("Dilated ", dilated_img)

img_e = erode_this(np.copy(image_src), erosion_level=3)
writePGM(img_e,path+ "eroded.pgm",lx,ly,"P2")
eroded_img = cv.imread(path+ "eroded.pgm")
cv.imshow("Eroded ", eroded_img)

img_o = ouverture(np.copy(image_src), 9)
writePGM(img_o, path+ "ouverture.pgm",lx,ly,"P2")
ouvert_img = cv.imread(path+ "ouverture.pgm")
cv.imshow("Ouveture ", ouvert_img)

# Check idempotence
#img_o2 = ouverture(np.copy(image_src), 9)
#writePGM(img_o2, path+ "ouverture2.pgm",lx,ly,"P2")
#ouvert_img2 = cv.imread(path+ "ouverture2.pgm")
#cv.imshow("Ouveture2 ", ouvert_img2)

img_f = fermeture(np.copy(image_src), 9)
writePGM(img_f, path+ "fermeture.pgm",lx,ly,"P2")
fermeture_img = cv.imread(path+ "fermeture.pgm")
cv.imshow("Fermeture ", fermeture_img)

cv.waitKey()