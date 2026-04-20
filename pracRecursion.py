#sum of n natural numbers

# def sum(n):
#     if(n == 0):
#         return 0
#     return sum(n-1)+n

# print(sum(10))

#print all elements in a list
#using recursion

def printlist(list,index):
    if(index == len(list)):
        return 0
    print(list[index])
    printlist(list,index+1)


data = printlist([1,2,3,4,5,6,7],0)
