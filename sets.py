sets = {1,2,2,3,4,5,6,'hello','hello'} #duplicates are not allowed
sets.add(8) #set is mutable but elements are not 
sets.remove(2)
sets.add((11,22,33))
# sets.clear()
print("popped val : ",sets.pop())
print(sets)

#set methods
set1 = {2,4,5,6,7}
set2 = {1,3,8,6,2,0}

set  = set1.union(set2)
print("union of two sets : ",set)

set3  = set1.intersection(set2)
print("Intersection of two sets :",set3)
