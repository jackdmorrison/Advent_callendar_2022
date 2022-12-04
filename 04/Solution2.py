f = open("./File1.txt")
arr=[]
total=0
for line in f:
    item=line.strip("\n")
    if(item!='\n'):
        validate=False
        arr=item.split(",")
        arr[0]=arr[0].split('-')
        arr[1]=arr[1].split('-')
        set1=set()
        for i in range(int(arr[0][0]),int(arr[0][1])+1):
            set1.add(i)
        set2=set()
        for i in range(int(arr[1][0]),int(arr[1][1])+1):
            set2.add(i)
        for x in set1:
            if(x in set2):
                validate=True
        if(validate):
            total+=1
print(total) 