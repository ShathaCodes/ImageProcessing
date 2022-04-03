from numpy import int32, max

def writepgm(filename, img, lx, ly):
    maxVal = max(img)
    img = int32(img).tolist()
    f = open(filename,'w')

    magicNum = 'P2'
    f.write(magicNum + '\n')

    f.write(str(lx) + ' ' + str(ly) + '\n')

    f.write(str(maxVal) + '\n')

    for i in range(ly):
        count = 1
        for j in range(lx):
            f.write(str(img[i][j]) + ' ')
            if count >= 17:
            # No line should contain gt 70 chars (17*4=68)
            # Max three chars for pixel plus one space
                count = 1
                f.write('\n')
            else:
                count = count + 1
        f.write('\n')
    f.close()