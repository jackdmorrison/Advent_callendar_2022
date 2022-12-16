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
    # index=0
    # if(len(left)>len(right)):
    #     length=len(right)
    #     result=False
    #     while (not result and index<length):
    #         if(isinstance(left[index],list) and isinstance(right[index],list)):
    #             result=checkArray(left[index],right[index])
    #         elif(isinstance(left[index],list) and isinstance(right[index],int)):
    #             result=checkArray(left[index],[right[index]])
    #         elif(isinstance(left[index],int) and isinstance(right[index],list)):
    #             result = checkArray([left[index]],right[index])
    #         else:
    #             if(left[index]<right[index]):
    #                 result=True
    #         index += 1
    # else:
    #     length=len(left)
    #     result=True
    #     while (result and index<length):
    #         if(isinstance(left[index],list) and isinstance(right[index],list)):
    #             result=checkArray(left[index],right[index])
    #         elif(isinstance(left[index],list) and isinstance(right[index],int)):
    #             result=checkArray(left[index],[right[index]])
    #         elif(isinstance(left[index],int) and isinstance(right[index],list)):
    #             result = checkArray([left[index]],right[index])
    #         else:
    #             if(left[index]>right[index]):
    #                 result=False
    #         index += 1
    # return result
pairs.append(tmp)
#print(pairs)
index=1
total=0
for pair in pairs:
    print(checkArray(pair[0],pair[1]))
    if(checkArray(pair[0],pair[1])<1):
        total+=index
    index+=1
print(total)