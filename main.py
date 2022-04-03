import matplotlib.pyplot as plt

from TP1.analysePGM import analysepgm
from TP1.histogram import histogram, histogramC
from TP1.readPGM import readpgm
from TP2.histogramEg import histogramEg


print("started")

img, lx, ly = readpgm('images/cours.pgm')

print("lx= ",lx , " ly= ", ly)
print(img)

moy, var = analysepgm(img)
print("moyenne = ",moy, " ecart type = ", var)

histo = histogram(img, lx, ly)
print(histo)

histoc = histogramC(histo)
print(histoc)

#------------------------------ TP 2 

histoeg = histogramEg(histo)
print(histoeg)

plt.figure()
plt.title('Grayscale Histogram')
plt.ylabel("Bins: interval of pixel intensity")
plt.xlabel('Nbr of pixels')
plt.plot(histo)
plt.plot(histoeg)
plt.show()