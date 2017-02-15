# copying lists in python is not as easy as one may think

lst1 = [1,1,1]
print(lst1)
lst2 = lst1 # until recently I thought this would create a copy but it does not
lst2[1] = 0 # the above line creates a new reference to lst1,
            # changing lst2 actually also changes lst1
print (lst1)

lst1 = [1,1,1]
# to create a new copy, try any of the following:
lst3 = lst1[:] # slicing works but it is bad syntax!
lst3[1] = 0
print (lst1)

lst4 = list(lst1)
lst4[1] = 0
print(lst1)

import copy
lst5 = copy.copy(lst1) # slower than list()
lst5[1] = 0
print(lst1)

lst6 = copy.deepcopy(lst1) # even more slower
                        #but necessary when copying a list of objects
lst6[1] = 0
print(lst1)


