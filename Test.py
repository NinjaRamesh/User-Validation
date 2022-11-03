import re


def register():
    email = input("Enter email address: ")
    regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

    if re.fullmatch(regex, email):
        print("Valid Emaildgfdsgdfzs")
    else:
        print("Invalid Email")
        return

    pwd = input("Enter password: ")
    specialCharacters = ["$", "#", "@", "!", "*"]
    if len(pwd) < 5 or len(pwd) > 16:
        print(
            "Make sure your password is has min 6 characters and max of 12 characters"
        )
        return
    elif re.search("[0-9]", pwd) is None:
        print("Make sure your password has a number in it")
    elif re.search("[a-z]", pwd) is None:
        print("Make sure your password has a small letter in it")
    elif re.search("[A-Z]", pwd) is None:
        print("Make sure your password has a capital letter in it")
    elif re.search("[specialCharacters]", pwd) is None:
        print("Make sure your password has a special character in it")
    else:
        print("Your password seems fine")
        # details = {email: pwd}
        with open("sample.txt", "w") as f:
            # f.write(str(details))
            f.write(email + "\n")
            f.write(pwd + "\n")
        f.close()


def user_login():
    email = input("Enter username:")
    pwd = input("Enter password:")
    d = {email: pwd}

    with open("sample.txt", "r") as f:
        credentials = f.read().split("\n")
        check_dict = {credentials[0]: credentials[1]}

    if d.get(email) == check_dict.get(credentials[0]) and d.get(pwd) == check_dict.get(
        credentials[1]
    ):
        print("Logged in Successfully")
    else:
        print("Wrong username/password")


def forget_password():
    email = input("Enter username:")
    email_input = "{'" + email + "'}"
    with open("sample.txt", "r") as f:
        credentials = f.read().split("\n")
        check_dict = {credentials[0]}

    if str(email_input) == str(check_dict):
        print(
            "Username gets matched, Do you want to retrieve the Original Password (or) Provide a new password"
        )
        print("1. Retrieve the Original Password")
        print("2. Provide a new password")
        ch = int(input("Enter your choice: "))
        if ch == 1:
            print("Your original password is: " + credentials[1])
        else:
            new_password = input("Enter password: ")
            specialCharacters = ["$", "#", "@", "!", "*"]
            if len(new_password) < 5 or len(new_password) > 16:
                print(
                    "Make sure your password is has min 6 characters and max of 12 characters"
                )
                return
            elif re.search("[0-9]", new_password) is None:
                print("Make sure your password has a number in it")
            elif re.search("[a-z]", new_password) is None:
                print("Make sure your password has a small letter in it")
            elif re.search("[A-Z]", new_password) is None:
                print("Make sure your password has a capital letter in it")
            elif re.search("[specialCharacters]", new_password) is None:
                print("Make sure your password has a special character in it")
            else:
                print("Your password seems fine")
            with open("sample.txt", "r") as f:
                credentials = f.read().split("\n")
                check_dict = {credentials[1]}
                check_dict = new_password
            with open("sample.txt", "w") as f:
                f.write(email + "\n")
                f.write(new_password + "\n")
            f.close()
            print("Your Password has been updated")
    else:
        print("Wrong username/password")


while 1:
    print("********** Login System **********")
    print("1.Signup")
    print("2.Login")
    print("3.Forget Password")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        register()
    elif ch == 2:
        user_login()
    elif ch == 3:
        forget_password()
    elif ch == 4:
        break
    else:
        print("Wrong Choice!")
