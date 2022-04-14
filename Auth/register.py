import re

def validated_text(prompt_message):
    while True:
        user_name = input(prompt_message)
        if re.match("^[A-Za-z]+$", user_name):
            return user_name
        else:
            print("Only characters allowd")

def validated_email():
    while True:
        mail = input("Enter your mail: ")
        mail_regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if re.match(mail_regex, mail):
            return mail
        else:
            print("Invalid mail input!")

def validated_password():
    while True:
        password = input("Enter your password: ")
        password_confirmation = input("Re-Enter your password: ")
        if password != password_confirmation:
            print("password doesn't match")
            validated_password()
        passwor_regex = re.compile(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$')
        if re.match(passwor_regex, password):
            return password
        else:
            print("""
            Password must contain the following:
            lowercase
            uppercase
            special chatacter
            number
            minmum 6 characters in length
            """)


def validated_mobile():
    while True:
        mobile_number = input("Enter your mobile number: ")
        eg_phone_regex = re.compile(r'^01[0125][0-9]{8}$')
        if re.match(eg_phone_regex, mobile_number):
            return mobile_number
        else:
            print("You must enter an egyptain phone number")


def register():
    first_name = validated_text("Enter your first name: ")
    last_name = validated_text("Enter your last name: ")
    email = validated_email()
    password = validated_password()
    mobile = validated_mobile()
    users_file = open("Auth/users.text","a")
    user_data = f"{ email }:{ password }:{ first_name }:{ last_name }:{ mobile }\n"
    users_file.write(user_data)
    users_file.close()



