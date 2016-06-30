# Python module to view the data inside a shelve
# Usage : 
# Command : python shelveViewer.py testing.graph
# Pass the path of the file as an argument to this script.


import shelve
import sys
import os

filename = sys.argv[1]

if os.path.exists(filename):
    print "[*] File Exists : ",filename
    print "[*] Opening file"
    f = shelve.open(filename)
    print "\nShelve data : "
    for x in f:
        print x," -> ",f[x]
    print "\nTotal no. of items in shelve : ",len(f)

else:
    print "File does not exist : ",filename
