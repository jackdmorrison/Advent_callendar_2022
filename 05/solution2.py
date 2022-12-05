f = open("./File1.txt")
arr=[]
total=0
line=f.readline()
while(line!='\n'):
    arr.append(line)
    line=f.readline()
y=1
z=0
stackArr=[]
for x in arr[len(arr)-1]:
    try:
        if(int(x)==y):
            tmp=[]
            for d in reversed(arr):
                if(d[z]!=' ' and d!=arr[len(arr)-1]):
                    tmp.append(d[z])
            stackArr.append(tmp)
            y+=1
        z+=1
    except:
        z+=1

commands=[]
tmp=f.readline()
while(tmp !=''):
    t=tmp.split(' ')
    tt=[]
    tt.append(int(t[1]))
    tt.append(int(t[3]))
    tt.append(int(t[5]))
    commands.append(tt)
    tmp=f.readline()

for x in commands:
    t=[]
    for i in range(0,x[0]):
        t.append(stackArr[x[1]-1].pop())
    for b in reversed(t):
        stackArr[x[2]-1].append(b)
for finallydone in stackArr:
    print(finallydone.pop())
