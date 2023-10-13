#!python3

"""
Similar to task2.py
Program will ask the user to enter their username and password
If the username is a match, see if the password is the correct one
annie's password is 12345
betty's is password
etc.

"""

users = ["annie","betty","charles","doug","eddie","flon"]
passwords = ["12345","password","iloveyou","mom","default","0"]

for i in range(3):
    print(f"atepts left {3 - i}")
    enteredUsername = input("enter Username: ")
    enteredPassword = input("enter the password: ")
    if enteredUsername in users and enteredPassword == passwords[users.index(enteredUsername)]:
        print("acses granted")
        break
    else:
        print("acses denied")
        continue
else:
    print("no more atepts")