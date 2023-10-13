#!python3
'''
The program will ask the user for a username and a password
If the user name and password are correct, the program will
exit and say "Access Granted".
If they are not correct, the program will say "Access Denied".
There will be a maximum of 3 guesses allowed
'''

expectedUsername = "systemadmin"
expectedPassword = "master"

for i in range(3):
    print(f"atemps left {3 - i}")
    enteredUsername = input("enter Username: ")
    enteredPassword = input("enter the password: ")
    if enteredUsername == expectedUsername and enteredPassword == expectedPassword:
        print("acses granted")
        break
    else:
        print("acses denied")
        continue
else:
    print("no more gesses")