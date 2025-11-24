# Login
pwd = input("Windows Hello PIN? Ans: ")
if pwd == "190828":
    print("Signing in...\n")
else:
    print("Request Failed\nIncorrect PIN\nTry Again!")
    quit()


# Function
def view():
    try:
        with open("password.txt", "r") as f:
            lines = f.readlines()

            if not lines:
                print("No passwords saved yet.")
                return

            print("\nSaved Passwords:")
            print("-----------------")
            for line in lines:
                name, password = line.strip().split("||")
                print(f"Username: {name} | Password: {password}")
            print()
    except FileNotFoundError:
        print("No password file found. Add some passwords first!\n")


def add():
    name = input("Enter username: ")
    password = input("Enter password: ")

    with open("password.txt", "a") as f:
        f.write(f"{name}||{password}\n")

    print("Password saved!\n")


# Main Loop
while True:
    mode = input("Add, View, or q to Quit? Ans: ").lower()

    if mode == "q":
        print("Have a good day!")
        break
    elif mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid input, try again...\n")


