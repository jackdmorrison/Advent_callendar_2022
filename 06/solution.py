f = open("./File1.txt")
arr=[]
total=0
for line in f:
    buffer=[]
    count=0
    num=0
    for x in line:
        count+=1
        
        if(x in buffer):
            bool=False
            tmp=buffer.copy()
            buffer.clear()
            
            for i in tmp:
                if(bool):
                    buffer.append(i)
                if(i==x):
                    bool=True
                
            buffer.append(x)
        else:
            buffer.append(x)
        if(len(buffer)==4):
            num=count
            break
    print(num)
