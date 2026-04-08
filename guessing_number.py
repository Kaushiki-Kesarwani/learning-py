import random
jackpot = random.randint(1,100)

guess = int(input("guess the number:"))
count = 1

while guess!=jackpot:
    if guess>jackpot:
        print("guess lower")
    else:
        print("guess higher")

    guess = int(input("guess the number:"))
    count+=1

print("congratulations!you guess the correct number.")
print("you took",count,"attempts")
