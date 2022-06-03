def histogram(m,lx,ly):
    maxVal=m.max()
    h=[0 for i in range (maxVal +1)]
    for i in range (ly):
        for j in range (lx):
            h[m[i][j]]+=1
    return h 

def histogramcumul(h,maxVal):
    c=[h[i] for i in range (maxVal +1)]
    for i in range (1,maxVal+1):
        c[i]+=c[i-1]
    return c