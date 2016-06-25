import graph

graph = graph.Graph("testing.graph")
a1 = graph.createAtom("Apoorva")
a1.property("Degree","Class 12th")
a1.property("Percentage in 12th","85%")
a1.showProperties()

del a1
a1 = graph.createAtom("Arpit")
a1.property("Degree","B Tech CS IT")
a1.property("Percentage in 12th","73%")
a1.relationship("is_brother",True,graph.editAtom(2))
a1.showRelationships()
graph.showAtoms()