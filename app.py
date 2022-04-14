from Auth.register import register
from Auth.login import login
from project.project_menu import draw_prj_menu
from termcolor import colored

print("Fundrasing App")

main_menu_options = {
    1: 'Login',
    2: 'Register',
    3: 'Exit',
}

def draw_main_menu():
    for key,value in main_menu_options.items():
        print (f"{key}) {value}")

while(True):
    draw_main_menu()
    option = int(input(colored('Enter your choice: ',"blue")))
    if option == 1:
        print('Login')
        if login():
            draw_prj_menu()
        else:
            print(colored("Invalid Email or password", "red"))
    elif option == 2:
        print('Register your information')
        register()
    elif option == 3:
        print('Thanks For using our App')
        exit()
    else:
        print(colored('Invalid option.',"yellow"))