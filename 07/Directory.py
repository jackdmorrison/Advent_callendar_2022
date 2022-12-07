class Directory:
    def __innit__(self, name,parent):
        self.__parent=parent
        self.__children = set()
        self.__files = set()
        self.__name=name
        self.size=0
    def children(self):
        return self.__children
    def files(self):
        return self.__files
    def name(self):
        return self.__name
    def parent(self):
        return self.__parent
    def getSize(self):
        return self.size
    def addSize(self,value):
        self.size+=value
        if(self.__parent!=None):
            self.__parent.addSize(value)
    def addChild(self,child):
        self.__children.add(child)
    def addFile(self,file):
        self.addSize(file.value)
        self.__files.add(file)
    def listAll(self,space):
        print(self.size)
        print(space+self.__name)
        if(len(self.__children)!=0):
            for child in self.__children:
                child.listAll(space+'  ')
        for file in self.__files:
            print(space+'  '+file.name+' ')
    def findBelow(self,val,total):
        if(self.size<=val):
            total+=self.size
        if(len(self.__children)!=0):
            for child in self.__children:
                total=child.findBelow(val,total)
        return total
    def findAbove(self,val,smallest):
        if(len(self.__children)!=0):
            for child in self.__children:
                if(child.size<smallest ):
                    smallest=child.findAbove(val,smallest)
        if(smallest > self.size and self.size>val):
            smallest=self.size
        return smallest
    def getChild(self,name):
        for child in self.__children:
                if(child.name()==name):
                    return child
    def inFiles(self,name):
        for file in self.__files:
                if(file.name==name):
                    return True
        return False
    def inChildren(self,name):
        for child in self.__children:
                if(child.name()==name):
                    return True
        return False
                    
