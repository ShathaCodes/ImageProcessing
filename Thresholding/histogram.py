def histogram(m,lx,ly):
    maxVal=m.max()
    h0=[0 for i in range (maxVal +1)]
    h1=[0 for i in range (maxVal +1)]
    h2=[0 for i in range (maxVal +1)]
    for i in range (lx):
        for j in range (ly):
                h0[m[i][j][0]]+=1
                h1[m[i][j][1]]+=1
                h2[m[i][j][2]]+=1
    return h0,h1,h2 