from collections import OrderedDict
f = open("./File1.txt")
key={ 'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 'z':26, 'A':27, 'B':28, 'C':29, 'D':30, 'E':31, 'F':32, 'G':33, 'H':34, 'I':35, 'J':36, 'K':37, 'L':38, 'M':39, 'N':40, 'O':41, 'P':42, 'Q':43, 'R':44, 'S':45, 'T':46, 'U':47, 'V':48, 'W':49, 'X':50, 'Y':51, 'Z':52}
arr=[]
for line in f:
    arr.append(line.strip("\n"))
total=0
ticker=0
tmp=[]
for i in range(len(arr)):
    if(ticker==0):
        tmp.append(arr[i])
        ticker+=1
    elif(ticker==1):
        tmp.append(arr[i])
        ticker+=1
    else:
        ticker=0
        tmp.append(arr[i])
        first="".join(OrderedDict.fromkeys(tmp[0]))
        second="".join(OrderedDict.fromkeys(tmp[1]))
        third="".join(OrderedDict.fromkeys(tmp[2]))
        temp=first+second
        shared=""
        dup=""
        for i in temp:
            if(i in dup):
                shared=shared+i
            else:
                dup=dup+i

        temp2=shared+third
        shared2=""
        dup2=""
        for i in temp2:
            if(i in dup2):
                shared2=shared2+i
            else:
                dup2=dup2+i
        total+=key[shared2]
        tmp=[]
print(total)