def findSmaller(val,arr):
    for i in arr:
        if(val<=i):
            return False
    return True
def revSmaller(val,arr):
    for i in reversed(arr):
        if(val<=i):
            return False
    return True
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
for iy in range(0, yLen):
    for ix in range(0, xLen):
        val= y[iy][ix]
        if(findSmaller(val,x[ix][iy+1:]) or revSmaller(val,x[ix][:iy]) or findSmaller(val,y[iy][ix+1:]) or revSmaller(val,y[iy][:ix])):
            visible+=1
print(visible)
