# Graph

A graph database made in Python

This is an impolementation of a simple graph database in python. The data is stored in a shelve file and is managed using the built-in python module called shelve.

The main file where the graph database is implemented is "graph.py".

## Classes in graph.py

 - **Atom** - Like there are nodes in a graph. Here we call these nodes as Atom. Atoms have similar attributes to that of a node. At present these atoms are relatively simple so they only have 3 attributes namely id, properties and relationships. The **id** attribute assigns a unique id for each atom so that they can be indentified. The **properties** attribute contain a dictionary of all the properties that an atom is assigned. The **relationships** attribute contains the relations of that atom with other atom. The relationships attribute is yet to be modified as the representation of relationship in between atoms is very bad at present.
