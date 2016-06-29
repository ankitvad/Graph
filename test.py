import graph

graph = graph.Graph("testing.graph")
a1 = graph.createAtom("Harry")
a1.property("Degree","Class 12th")
a1.property("Percentage in 12th","85%")
a1.relationship("is_brother",True,a1)
a1.about()
#a1.showProperties()


a2 = graph.createAtom("Sunny")
a2.property("Degree","B Tech CS IT")
a2.property("Percentage in 12th","73%")
a2.relationship("is_brother",True,a1)
#a2.showRelationships()
a2.about()

a3 = graph.createAtom("Bunny")
a3.property("Degree",["B. Sc.","M. Sc.","Ph. D"])
a3.property("Percentage in 12th","63")
a3.relationship("is_mother",True,a1)
a3.relationship("is_mother",True,a2)


a4 = graph.createAtom("Tiger")
a4.property("Degree",["B. Sc.","M. Sc.","Ph. D"])
a4.property("Percentage in 12th","72")
a4.relationship("is_father",True,a1)
a4.relationship("is_father",True,a2)

graph.showAtoms()
