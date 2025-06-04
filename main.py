# password manager
from cryptography.fernet import Fernet

pwd = input("Windows hello pin? Ans:- ")
if pwd == "190828":
    print("Signin In <^>")
else:
    print("Request Failed\nIncorrect Pin")
    quit()

def view():
    with open("password.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            name, password = data.split("|")
            print("Username: ", name, ", Password: ", password)

def add():
    name = input("Enter username: ")
    password = input("Enter your password: ")

    with open("password.txt", "a") as f:
        f.write(name+ " | "+ password+ "\n")


while True:
    mode = input("Would you like to add new ones or view the existing one, (add or view or q for quit)? Ans:- ").lower()
    if mode == "q":
        print("Have a good day")
        break
    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid Inputs")




# code is not complete yet. I'm just giving you the sample