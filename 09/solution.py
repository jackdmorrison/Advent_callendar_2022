f= open("File1.txt")
board=[]
size=2000
for x in range(0,size):
    board.append([])
    for y in range(0,size):
        board[x].append('.')

head=[size-1,0]
tail=[size-1,0]
board[tail[0]][tail[1]]='#'
for line in f:
    
    if(line[0]=='R'):
        val = int(line[2])
        for i in range(0,val):
            prev=head.copy()
            head[1]+=1
            if((head[1]-tail[1])>1):
                tail=prev.copy()
            board[tail[0]][tail[1]]='#'

    elif(line[0]=='L'):
        val = int(line[2])
        for i in range(0,val):
            prev=head.copy()
            head[1]-=1
            if((tail[1]-head[1])>1):
                tail=prev.copy()
            board[tail[0]][tail[1]]='#'
    elif(line[0]=='U'):
        val = int(line[2])
        for i in range(0,val):
            prev=head.copy()
            head[0]-=1
            if((tail[0]-head[0])>1):
                tail=prev.copy()
            board[tail[0]][tail[1]]='#'
                
    elif(line[0]=='D'):
        val = int(line[2])
        for i in range(0,val):
            prev=head.copy()
            head[0]+=1
            if((head[0]-tail[0])>1):
                tail=prev.copy()
                
            board[tail[0]][tail[1]]='#'
    # for x in board:
    #     print(x)
    # print('################################################################')
total=0
for x in board:
    for y in x:
        if(y=='#'):
            total+=1
   
print(total)