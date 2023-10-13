#!python3

'''
Create a number guessing game
There is a limit of 10 guesses
The program will ask the user to enter an integer from 1 to 100
The program will then tell the user if the number is too high, too low or correct.
If the number is correct, the program will end
If the 10 guesses are used up, the program will say that the user has lost
'''
anser = 46

for i in range(10):
    print(f"atempt {i + 1}.", end=" ")
    gess = int(input("enter a number less then 100: "))
    if gess == anser:
        print("you win!!")
        break
    elif gess > anser:
        print("to big")
    elif gess < anser:
        print("to small")
else:
    print("you have lost")