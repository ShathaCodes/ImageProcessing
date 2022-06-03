
import numpy as np
import sys
sys.path.append("C:/Users/LENOVO/Desktop/my python/TP_ traitement d'img/")
from read_write_histogram.histogram import histogram, histogramcumul
from  read_write_histogram.readPGM import readPGM
from egalisationh import egalisation


path="C:/Users/LENOVO/Desktop/my python/TP_ traitement d'img/images/"

img , lx ,ly =readPGM(path+"cours.pgm")
heg=egalisation(img,lx,ly)
print("histogramme egalisé=")
print(heg)