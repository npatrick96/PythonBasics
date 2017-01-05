''' Test code for using the command line to pass arguments, storing them in a list, and using a for loop to print them. '''

import sys

argLst = sys.argv

for i in argLst[1:]:
    print(i)
    
