city = ["delhi","mumbai","paris","russia","chennai"]

# def count(cities):
#     return len(cities)


# def printing(list):
#     for item in list:
#         print(item,end=", ")

# printing(city)

#factorial
def factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    return fact
    

print(factorial(6))