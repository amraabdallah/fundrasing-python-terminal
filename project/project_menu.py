from project.helpers import *
def draw_prj_menu():

    project_menu_options = {
    1: 'Create a new project',
    2: 'Show All Projects',
    3: 'Delete a project',
    4: 'Edit my Projects',
    5: 'Log out',
    6: 'Exit'
    }

    def draw_menu():
        for key,value in project_menu_options.items():
            print (f"{key}) {value}")

    while(True):
        draw_menu()
        option = int(input('Enter your choice: '))
        if option == 1:
            print('Enter your project info')
            create_new_project()
        elif option == 2:
            print('All projects')
            show_all_projects()
        elif option == 3:
            print('Choose a project to delete')
            show_user_projects()
            project_name_delete = input("Enter name of the project you want to delete: ")
            delete_project(project_name_delete)
        elif option == 4:
            print('Choose a project to edit')
            show_user_projects()
            project_name_edit = input("Enter the title of the project you want to Edit: ")
            edit_project(project_name_edit)
        elif option == 5:
            print("You are logged out!")
            break
        elif option == 6:
            print("Thanks for using our App")
            exit()
        else:
            print('Invalid option.')