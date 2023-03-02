import random
import math

lower = 0
upper = int(input("Enter highest number: "))

x = random.randint(lower, upper)
print("\n\tYou have ",
       round(10),
      " chances to guess the integer!\n")

count = 0
while count <10:
    count +=1

    guess = int(input("Guess a number: "))

    if x == guess:
        print("WPlayed you did it in ",
              count, " tries")

        break
    elif x > guess:
        print("TOO LOW")
    elif x < guess:
        print("TOO HIGH")


if count >= (10):
    print("\nThe number is %d" % x)
    print("\t nt better luck next time!")