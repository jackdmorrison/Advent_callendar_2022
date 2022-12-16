f = open("File1.txt")
pairs=[]
class stupid:
    def __init__(self,arr,index):
        self.index = index
        self.arr = arr
def StartArray(line,index):
    stuff=stupid([],index)
    #print(stuff.arr)
    stuff.index+=1
    currentThing=''
    while(line[stuff.index]!=']' ):
        #print(stuff.arr)
        #print(stuff.index)
        if(line[stuff.index]=='['):
            stup=StartArray(line,stuff.index)
            currentThing=stup.arr
            stuff.index=stup.index
        elif(line[stuff.index]==','):
            try:
                int(currentThing)
                stuff.arr.append(int(currentThing))
            except:
                stuff.arr.append(currentThing)
            currentThing=''
            stuff.index+=1
        else:
            currentThing+=line[stuff.index]
            stuff.index+=1
    if(currentThing!=''):
        try:
            int(currentThing)
            stuff.arr.append(int(currentThing))
        except:
            stuff.arr.append(currentThing)
    if(stuff.index<len(line)-1):
        stuff.index+=1
    return stuff
        


tmp=[]
for line in f:
    
    i=0
    end=False
    if(line[:2]!='\n'):
        line=line.strip('\n')
        stup=StartArray(line,0)
        #print(stup.arr)
        tmp.append(stup.arr)
    else:
        pairs.append(tmp)
        tmp=[]
def checkInt(x,y)->int:
    if(x==y):
        return 0
    elif(x>y):
        return 1
    else:
        return -1
def checkArray(left,right):
    index=0
    while index<len(left) and index<len(right):
        x=left[index]
        y=right[index]
        result=0
        if(isinstance(x,int) and isinstance(y,int)):
            result = checkInt(x,y)
        else:
            if(isinstance(x,int) ):
                x=[x]
            if(isinstance(y,int)):
                y=[y]
            result=checkArray(x,y)
        if result !=0:
            return result
        index+=1
    if(index == len(left) and i == len(right)):
        return 0
    elif(index == len(left)):
        return -1
    else:
        return 1
pairs.append(tmp)
#print(pairs)

total=0
sorted=[[2],[6]]
for pair in pairs:
    sorted.append(pair[0])
    sorted.append(pair[1])
changes=True

while changes==True:
    changes=False
    for index in range(0,len(sorted)-1):
        if(checkArray(sorted[index],sorted[index+1])>-1):
            tmp=sorted[index].copy()
            sorted[index]=sorted[index+1].copy()
            sorted[index+1]=tmp.copy()
            changes=True
i=1
lol=[]
for items in sorted:
    if(items==[2] or items==[6]):
        lol.append(i)
    i+=1
print(lol[0]*lol[1])