class Login:
    def __init__(self, username, password):
        self.username = username
        self.password = password


lists = []
master_Password = "GTech"


def login():
    boo = True
    while boo:
        u = input("Please enter your username ")
        p = input("Please enter your password ")
        print("")
        if p == master_Password:
            print("Printing all login information... ")
            for name in lists:
                print(f"{name.username}, {name.password}")
            break
        for log in lists:
            if log.username == u and log.password == p:
                print("Login successful")
                print("")
                boo = False
                break
            else:
                print("Incorrect login. Try again")
                print("")
                break

def create():
    while True:
        user = input("Username ")
        pasw = input("Password ")
        print("")
        Login1 = Login(user, pasw)
        lists.append(Login1)
        decision = input("Would you like to enter another login? Type 0 for Yes and 1 for No ")
        if int(decision) == 1:
            break


print("Welcome to Hong Kong Enterprise!")
while True:
    choice = int(input("""
Please select an option
    1. Create Login
    2. Login
    3. Quit
    """))
    if choice == 1:
        create()
    elif choice == 2:
        if len(lists) == 0:
            print("There are no logins!")
        else:
            login()
    elif choice == 3:
        break
    else:
        print("Invalid Option")
print("")





login()





