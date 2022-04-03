from numpy import array, int32

def readpgm(filename):
    f = open(filename,'r')

    # Read header info
    line = f.readline()
    magicNum = line.strip()
    if magicNum != 'P2' and magicNum != 'P5':
        f.close()
        print ('Not a valid PGM file')
        exit()

    comment = True
    while comment == True:
        line = f.readline()
        if line[0] != '#':
              comment = False

    [lx, ly] = (line.strip()).split()
    lx = int(lx)
    ly = int(ly)

    line = f.readline()
    maxVal = int(line.strip())
      
    # Read pixels information
    img = []
    buf = f.read()
    elem = buf.split()
    for i in range(ly):
        tmpList = []
        for j in range(lx):
          tmpList.append(int(elem[i*lx+j]))
        img.append(tmpList)
    return (array(img), lx, ly)

