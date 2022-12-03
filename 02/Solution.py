f = open("./File1.txt")
arr=[]
for line in f:
    arr.append(line)
Total=0
for item in arr:
    if(item!='\n'):
        tarr= item.strip("\n").split(' ')
        print(tarr)
        if(tarr[1]=='Y'):
            Total+=2
            if(tarr[0]=='A'):
                Total+=6
            elif(tarr[0]=='B'):
                Total+=3
        elif(tarr[1]=='X'):
            Total+=1
            if(tarr[0]=='C'):
                Total+=6
            elif(tarr[0]=='A'):
                Total+=3    
        elif(tarr[1]=='Z'):
            Total+=3
            if(tarr[0]=='B'):
                Total+=6
            elif(tarr[0]=='C'):
                Total+=3
print(Total)