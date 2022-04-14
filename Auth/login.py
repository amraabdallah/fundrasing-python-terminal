from termcolor import colored

def login():
    user_input_email = input("Email: ")
    user_input_password = input("Password: ")
    users_file = open("Auth/users.text","r")
    for line in users_file:
        user_list = line.split(":")
        file_email = user_list[0]
        file_password = user_list[1]
        file_username = user_list[2].capitalize()
        if user_input_email == file_email and file_password == user_input_password:
            loggedin_user_file = open("loggedin_user.text","w")
            loggedin_user_file.write(user_input_email)
            loggedin_user_file.close()
            print(colored(f"Welcome, {file_username} you are logged in!","green"))
            return True
    else:
        return False
