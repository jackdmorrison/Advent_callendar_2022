f =open("Test.txt")
cycles=1
total=1
arr=[]
drawnRows=[]
spritePos=[]
position=1
print(len(spritePos))
for line in f:
    line = line.strip('\n')
    line = line.split(' ')
    if(line[0]=='noop'):
        cycles+=1
        if(cycles<=position+1 and cycles>=position-1):
            drawnRows.append('#')
        else:
            drawnRows.append('.')
        if(cycles==40 or cycles==80 or cycles==120 or cycles==160 or cycles==200 or cycles==240):
                arr.append(drawnRows)
                drawnRows=[]
        
    elif(line[0]=='addx'):
        for x in range(0,2):
            cycles+=1
            if(cycles<=position+1 and cycles>=position-1):
                drawnRows.append('#')
            else:
                drawnRows.append('.')
            if(cycles==40 or cycles==80 or cycles==120 or cycles==160 or cycles==200 or cycles==240):
                arr.append(drawnRows)
                drawnRows=[]
        position+=int(line[1])
for x in arr:
    print(x)
