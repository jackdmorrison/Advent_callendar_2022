f = open("File1.txt")
cycles=0
position=1
instructions= f.readline().strip('\n').split(' ')
line=[]
arr=[]
val=0
add=False
count=0
def drawPixel(iterator,position)->str:
    if(position-1<=iterator%40<=position+1):
        return '#'
    else:
        return '.'
while cycles<241:
    line.append(drawPixel(cycles,position))
    if(add==True):
        add=False
        position+=val
        instructions= f.readline().strip('\n').split(' ')
    elif(instructions[0]=='noop'):
        instructions= f.readline().strip('\n').split(' ')
    elif(instructions[0]=='addx'):
        val=int(instructions[1])
        add=True
    cycles+=1
    if(cycles%40==0):
        arr.append(line)
        line=[]

f2 = open("output.txt", "w")
for x in arr:
    str=""
    i=0
    for y in x:
        str+=y
    f2.write(str+'\n')
#print(arr)