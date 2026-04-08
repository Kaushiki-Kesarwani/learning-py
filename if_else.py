unicode = u"\U0001f600\U0001f606\U0001f923"
print(unicode)

age = input("Enter your age :")
if int(age) < 18 :
    print("not eligible to vote")
elif int(age) >= 18 :
    print("eligible to vote")  
else: print("wrong")