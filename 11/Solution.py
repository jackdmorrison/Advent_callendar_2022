f = open("./File1.txt")
class Monkey:
    def __init__(self,startingItems,operator,value2,test,true,false)->None:
        self.startingItems = []
        for x in startingItems:
            self.startingItems.append(int(x))
        self.operator = operator
        self.value2=value2
        self.test= test
        self.true=true
        self.false=false
        self.inspected=0
line=f.readline()
line=line.split()
newMonkey=True
monkeys=[]
Myitems=set()
while (newMonkey):
    startingItems=f.readline().strip('Starting items:').strip('\n').split(',')
    Mitems=[]
    for startingItem in startingItems:
        Mitems.append(int(startingItem))
        if(int(startingItem) not in Myitems):
            Myitems.add(int(startingItem))
    #print(Mitems)
    operation=f.readline().strip("Operation: new").strip('\n').split(' ')
    #print(operation)
    
    operator=operation[2]
    value2=operation[3]
    Test=f.readline().strip('Test: divisible by ').strip('\n').split(' ')
    #print(int(Test[0]))
    Ttrue=f.readline().strip('If true: throw to monkey').strip('\n').strip(' ')
    Tfalse=f.readline().strip('If false: throw to monkey').strip('\n').strip(' ')
    #print(Ttrue,Tfalse)
    line=f.readline()
    line=f.readline().split(' ')
    newMonkey = Monkey(startingItems,operator,value2,int(Test[0]),int(Ttrue),int(Tfalse))
    monkeys.append(newMonkey)
    if(line[0]!='Monkey'):
        newMonkey=False
x=0
while x<10000:
    if(x%1000==0):
        print(x)
    for monkey in monkeys:
        inHand=monkey.startingItems.copy()
        for item in inHand:
            val=0
            if(monkey.operator=='*'):
                #print('*')
                if(monkey.value2=='old'):
                        val=item*item
                else:
                    val = item*int(monkey.value2)
            elif(monkey.operator=='+'):
                #print('+')
                #print(monkey.value2)
                if(monkey.value2=='old'):
                        val=item+item
                else:
                    val = item+int(monkey.value2)
            #print(val)
            
            #val=int(val/3)
            monkey.startingItems.remove(item)
            monkey.inspected+=1
            if(val%monkey.test==0):
                monkeys[monkey.true].startingItems.append(val)
            else:
                monkeys[monkey.false].startingItems.append(val)
    x+=1
max1=0
max2=max1
for monkey in monkeys:
    #print(monkey.startingItems)
    if(monkey.inspected>max1):
        max2=max1
        max1=monkey.inspected
    elif(monkey.inspected>max2):
        max2=monkey.inspected
print(max1*max2)