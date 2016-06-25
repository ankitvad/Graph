import shelve
import sys

class Atom(object):
    
    def __init__(self,label,id):
        self.label=label
        self.id=id
        self.properties=dict()
        self.relationships=dict()
        self.__save()
        
    def property(self,name,value):
        self.properties[name]=value
        self.__save()
    
    def relationship(self,name,value,y,direction=0):
        # 0 denotes that the relationship goes from this object to the another object(outgoing relation)
        # 1 denotes that the relationship comes from another object to this object(incoming relation)
        self.relationships[name]=(value,direction)
        #y.relationship(name,value,self,int(not direction))
        self.__save()
        
    def __save(self):
        self.stateChanged=True

    def showProperties(self):
        print "\n# Total Properties : ",len(self.properties)
        print "Atom Name - ",self.label
        print "Properties:"
        for x in self.properties:
            print x," -> ",self.properties[x]

    def getProperty(self,x):
        return self.properties[x]

    def showRelationships(self):
        print "\n# Total Relationships : ",len(self.relationships)
        for x in self.relationships:
            if self.relationships[x][1]==0:
                print x," -> ",(self.relationships[x][0],"Outgoing")
            elif self.relationships[x][1]==1:
                print x," -> ",(self.relationships[x][0],"Incoming")

        if len(self.relationships)==0:
            print "No relations"

    def getRelation(self,x):
        return self.relations[x]




class Graph(object):
    total_atoms=0
    
    def __init__(self,name):
        self.name=name
        self.atoms={}
        self.s=shelve.open(name) 
     
    def createAtom(self,label):
        Graph.total_atoms+=1
        id = "id"+str(Graph.total_atoms)
        tmp = Atom(label,id=id)
        self.s[id]=tmp
        return tmp

    def showAtoms(self):
        print "\n# Total Atoms : ",Graph.total_atoms
        for x in range(1,Graph.total_atoms+1):
            print x," -> ",self.s["id"+str(x)].label

    def editAtom(self,atom_id):
        return self.s["id"+str(atom_id)]

    def saveAtom(self,atom):
        self.s["id"+str(atom_id)] = atom

    def close(self):
        self.s.close()






if __name__=="__main__":
    try:
        print "\n\t\t\t Atom Graph Database\n"
        print "1. Create a database"
        print "2. Edit a database"
        print "3. Delete a database"
        print "4. Details of a database"
        print "5. Search through a database"
        print
        a = raw_input("Enter your choice :")
    except KeyboardInterrupt:
        sys.exit()
    