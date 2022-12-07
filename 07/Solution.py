from File import File 
from Directory import Directory
#f=open("TEsTelSQPey##}}[{MM}dSkMvM.txt")
f=open("file1.txt")

home= Directory()
home.__innit__('/',None)
currentDir=home
for line in f:
    #print("line:",line)
    command=line.strip('\n').split(' ')
    if command[0]=='$':
        listing=False
        if(command[1] == "cd" ):
            if(command[2]=='..'):
                if(currentDir.parent()!=None):
                    currentDir=currentDir.parent()
                else:
                    print("exited Out too far")
            elif(command[2]=='/'):
                currentDir=home
            else:
                if(not currentDir.inChildren(command[2])):
                    print("file not in system directory")
                else:
                    currentDir=currentDir.getChild(command[2])
                    
        if(command[1]=='ls'):
            listing=True
            
    elif(listing==True):
        if(command[0]=='dir'):
            name=command[1]
            if(not currentDir.inChildren(name)):
                    tmp= Directory()
                    tmp.__innit__(name,currentDir)
                    currentDir.addChild(tmp) 
        else:
            if(not currentDir.inFiles(command[1])):
                tmp= File()
                tmp.__innit__(command[1],int(command[0]))
                currentDir.addFile(tmp) 
            
total=0  
val=home.getSize()
#print(val)
unused=70000000-val
#print(unused)
freeup=30000000-unused
print(freeup)
print(home.findAbove(freeup,val))
            


                        

            
            # if(line.splice(' ')[1]=='system-update'):
            #     if(line.splice(' ')[1]=='--'):
            #         difTmp=line.splice
            #         if()

