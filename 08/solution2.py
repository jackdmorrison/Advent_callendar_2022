def findSmaller(val,arr):
    i=0
    d=1
    while i< len(arr)-1:
        if(val<=arr[i]):
            return d
        i+=1
        d+=1
    return d
def revSmaller(val,arr):
    i=len(arr)-1
    d=1
    while i > 0:
        if(val<=arr[i]):
            return d
        i-=1
        d+=1
    return d
f= open("File1.txt")
visible=0
arr=[]
x={}
y={}
iterator=0
line=f.readline()
line = line.strip('\n')
xLen=len(line)
y[iterator]=[]
for i in range(0, xLen):
     x[i]=[int(line[i])]
     y[iterator].append(int(line[i]))
iterator+=1
line=f.readline()
line = line.strip('\n')
while len(line)==xLen:
    y[iterator]=[]
    for i in range(0, xLen):
        x[i].append(int(line[i]))
        y[iterator].append(int(line[i]))
    line=f.readline()
    line = line.strip('\n')
    iterator+=1
yLen=iterator
topscenicScore=0
for iy in range(0, yLen):
    for ix in range(0, xLen):
        val= y[iy][ix]
        scenicScore=findSmaller(val,x[ix][iy+1:]) * revSmaller(val,x[ix][:iy]) * findSmaller(val,y[iy][ix+1:]) * revSmaller(val,y[iy][:ix])
        if(scenicScore>topscenicScore):
            topscenicScore=scenicScore
print(topscenicScore)