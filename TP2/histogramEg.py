import numpy as np
import matplotlib.pyplot as plt

from TP1.histogram import histogramC



def histogramEg(h):

    # histogramme cumule
    hc = histogramC(h)

    # histogramme plat
    P  = np.sum(h)  # Nbr pixels
    K = len(h)      # NdG
    R = P//K
    hp = np.ones(len(h))*R 

    # histogram eg
    # calcul probabilités cumulées
    pc = np.zeros(K)
    for i in range(0,K):
        pc[i] = hc[i]/P

    A = (K-1) * pc      # A=(K-1)xpc(n)
    n1 = np.trunc(A)    # n1 = Ent(A)

    yeg = np.zeros(K)
    c=0
    for i in range(0,K):
        while n1[c] == i:
            yeg[i] += h[c]
            c +=1
            if c > (K-1):   # à la derniere case (i=K-1), c = K or on a longeur de n1 est K ( donc n1[c] n'existe pas)
                break
    return yeg



