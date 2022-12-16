import math
f= open("Test.txt")
class coordinate:
    def __init__(self,x,y,value):
        self.x = x
        self.y = y
        self.value=value
    def getCoordinate(self):
        return {"x":self.x, "y":self.y}
    def getValue(self):
        return self.value
class path:
    def __init__(self,cost_to_end,estimate,coordinates):
        self.cost_to_end = cost_to_end
        self.estimate = estimate
        self.coordinates=coordinates
        
        
grid=[]
i=0
for l in f:
    tmp=[]
    i2=0
    l=l.strip('\n')
    for r in l:
        coor=coordinate(i,i2,r)
        tmp.append(coor)
        i2+=1
    grid.append(tmp)
    i+=1

def find_goal(arr,value)->coordinate:
    for x in arr:
        for y in x:
            if(y.value==value):
                return y
currentPos=find_goal(grid,'S')
currentPos.value='a'
goalPos=find_goal(grid,'E')
def estimate_Cost(Pos,goalPos)->int:
    if(Pos.x>goalPos.x):
        b=Pos.x-goalPos.x
    else:
        b=goalPos.x-Pos.x
    if(Pos.y>goalPos.y):
        a=Pos.y-goalPos.y
    else:
        a=goalPos.y-Pos.y
    return int(math.sqrt((a**2)+(b**2)))
reached=False

def can_move_to(currentPos, goal_pos):
    val=ord(currentPos.value)-ord(goal_pos.value)
    if(val<2 and val>-2):
        return True
    else:
        return False
paths=set()
paths.add(path(0,estimate_Cost(currentPos,goalPos),[currentPos]))
while not reached:
    next_paths=set()
    for pathobj in paths:
        curr=pathobj.coordinates.pop()
        if(curr.value=='E'):
            reached=True
            print("reached")
            print(pathobj.cost_to_end)
            break
        if(can_move_to(grid[curr.x+1][curr.y],curr)):
            tmp=pathobj.coordinates.copy()
            tmp.append(curr)
            tmp.append(grid[curr.x+1][curr.y])
            next_paths.add(path(pathobj.cost_to_end+1,estimate_Cost(curr,goalPos),tmp))
        if(can_move_to(grid[curr.x-1][curr.y],curr)):
            tmp=pathobj.coordinates.copy()
            tmp.append(curr)
            tmp.append(grid[curr.x-1][curr.y])
            next_paths.add(path(pathobj.cost_to_end+1,estimate_Cost(curr,goalPos),tmp))
        if(can_move_to(grid[curr.x][curr.y+1],curr)):
            tmp=pathobj.coordinates.copy()
            tmp.append(curr)
            tmp.append(grid[curr.x][curr.y+1])
            next_paths.add(path(pathobj.cost_to_end+1,estimate_Cost(curr,goalPos),tmp))
        if(can_move_to(grid[curr.x][curr.y-1],curr)):
            tmp=pathobj.coordinates.copy()
            tmp.append(curr)
            tmp.append(grid[curr.x-1][curr.y-1])
            next_paths.add(path(pathobj.cost_to_end+1,estimate_Cost(curr,goalPos),tmp))
        print(next_paths)
    for Npath in next_paths:
        paths.add(Npath)