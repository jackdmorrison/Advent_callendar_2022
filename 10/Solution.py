f =open("File1.txt")
cycles=0
total=1
arr=[]
str=''
for line in f:
    
    line = line.strip('\n')
    line = line.split(' ')
    if(line[0]=='noop'):
        cycles+=1
        if(cycles==20 or cycles==60 or cycles==100 or cycles==140 or cycles==180 or cycles==220):
                arr.append(total*cycles)
    elif(line[0]=='addx'):
        for x in range(0,2):
            cycles+=1
            if(cycles==20 or cycles==60 or cycles==100 or cycles==140 or cycles==180 or cycles==220):
                arr.append(total*cycles)
        total+=int(line[1])
    
    #print(total)
print(arr)
print(arr[0]+arr[1]+arr[2]+arr[3]+arr[4]+arr[5])