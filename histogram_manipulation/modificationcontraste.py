import numpy as np
def function(A,B):
    a1=(0-A[1])/(0-A[0])
    b1=0
    print("L'équation réduite de (AB1) est : y1 = {}x1 + {}".format(a1,b1))
    a2=(B[1]-A[1])/(B[0]-A[0])
    b2=A[1]-a2*A[0]
    print("L'équation réduite de (AB2) est : y2 = {}x2 + {}".format(a2,b2))
    a3=(B[1]-255)/(B[0]-255)
    b3=255-a3*255
    print("L'équation réduite de (AB3) est : y3 = {}x3 + {}".format(a3,b3))
    return(a1,b1,a2,b2,a3,b3)



def contraste (img,lx,ly,A,B):
    new_img = np.copy(img)
    (a1,b1,a2,b2,a3,b3)=function(A,B)
    LUT=[0 for i in range (256)]
    for i in range (256):
        if i < A[0] :
            LUT[i]=a1*i+b1
        elif i < B[0] :
             LUT[i]=a2*i+b2
        else :
             LUT[i]=a3*i+b3
    for i in range (ly):
        for j in range (lx):
            new_img[i][j]=LUT[new_img[i][j]]
    return new_img 


