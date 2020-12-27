print("""
**************************************************
WELCOME TO GUESSING THE GAME!!!
-Try to gues the number.
-You have 10 chance.
-You will get some hints.
-GUESS BEFORE DIE!!!
**************************************************
""")
name=input("Enter your name:")
print( f"Hi! Welcome {name}!")
import random
number=random.randint(0,100)
chance=10
while True:
    guess = int(input("Enter Your Guess:"))
    if guess<number:
        print("Enter bigger number!")
        chance-=1
    elif guess>number:
        print("Enter smaller number!")
        chance -= 1
    else:
        print("YOU WIN!! GOODBYE!!")
        break
    if chance==0:
        print("FAIL!!YOU DIED!! GOODBYE!!")
        break




