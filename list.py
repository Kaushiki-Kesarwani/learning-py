list = [1,2,3,4,5,6,7,8]
print(list)
print(list[0:6])#slicing
list.append(9)
print(list)

lists = [7,1,6,3,7,3,9]
lists.sort()
print(lists)

lists.sort(reverse=True)
print(lists)


list.reverse()
print(list)

list.insert(2,0)
print(list)

str = ['a','f','g','n','m']
# str.append('e')
# str.reverse()
# str.sort(reverse=True)
# str.insert(2,'t')
# str.remove(str[0])
str.pop(1)
print(str)