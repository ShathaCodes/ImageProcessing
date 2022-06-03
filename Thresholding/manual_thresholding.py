import numpy as np

def manual_threshholding(img, r=0, g=0 , b=0, option=None, s=0):
    threshhold = [b, g, r]
    img_s = np.copy(img)
    if (len(img_s.shape) ==2):
        (lx , ly ) = img_s.shape
    else:
        (lx , ly , rgb) = img_s.shape
    for i in range(lx):
        for j in range(ly):
            if(len(img_s.shape) ==2):
                if (img_s[i][j] < s):
                        img_s[i][j] = 0
                else : 
                    img_s[i][j] = 255
            elif ( option == "AND" and 
            (img_s[i][j][0] > threshhold[0] and 
            img_s[i][j][1] > threshhold[1] and 
            img_s[i][j][2] > threshhold[2] )):
                pass #conserver
            elif ( option == "OR" and 
            (img_s[i][j][0] > threshhold[0] or 
            img_s[i][j][1] > threshhold[1] or 
            img_s[i][j][2] > threshhold[2] )):
                pass #conserver

            else:
                for k in range(3):
                    if (img_s[i][j][k] < threshhold[k]):
                        img_s[i][j][k] = 0
                    else : 
                        img_s[i][j][k] = 255

    return img_s