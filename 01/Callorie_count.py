f = open("./File1.txt")
arr=[]
for line in f:
    arr.append(line)
second=[]
elfTotal=0
for item in arr:
    if(item!='\n'):
        item.strip("\n")
        tmp= int(item)
        elfTotal+=tmp
    else:
        second.append(elfTotal)
        elfTotal=0
second.append(elfTotal)
max =0
max2=0
max3=0
for elfs in second:
    if(elfs>max):
        max3=max2
        max2=max
        max=elfs
    elif(elfs>max2):
        max3=max2
        max2=elfs
    elif(elfs>max3):
        max3=elfs

print(max)
print(max+max2+max3)