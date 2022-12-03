f = open("./File1.txt")
arr=[]
for line in f:
    arr.append(line)
Total=0
for item in arr:
    if(item!='\n'):
        tarr= item.strip("\n").split(' ')
        if(tarr[1]=='X'):
            Total+=0
            if(tarr[0]=='A'):
                Total+=3
            elif(tarr[0]=='B'):
                Total+=1
            else:
                Total+=2
        elif(tarr[1]=='Y'):
            Total+=3
            if(tarr[0]=='A'):
                Total+=1
            elif(tarr[0]=='B'):
                Total+=2
            else:
                Total+=3  
        elif(tarr[1]=='Z'):
            Total+=6
            if(tarr[0]=='A'):
                Total+=2
            elif(tarr[0]=='B'):
                Total+=3
            else:
                Total+=1
print(Total)