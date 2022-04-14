from datetime import datetime
import re
from termcolor import colored

def validated_text(prompt_message):
    while True:
        text = input(prompt_message)
        if re.match("^[A-Za-z ]+$", text):
            return text
        else:
            print("Only characters allowd")

def validated_number(prompt_message):
    while True:
        number = input(prompt_message)
        if number.isnumeric():
            return int(number)
        else:
            print("Only numbers allowed")

def validated_date(date_prompt_message):
    while True:
        date = input(date_prompt_message)
        try:
            date_time_format = datetime.strptime(date, '%d-%m-%Y')
            return datetime.date(date_time_format)
        except:
            print("Invalid date format")

def get_project_creator():
    logged_user_file = open("loggedin_user.text","r")
    return logged_user_file.read()


def create_new_project():
    project_title = validated_text("Enter project Title: ")
    project_details = validated_text("Enter project details: ")
    project_target = validated_number("Project target in EGP: ")
    start_date = validated_date("start date (dd-mm-yyyy): ")
    end_date = validated_date("end date (dd-mm-yyyy): ")
    project_creator = get_project_creator()
    project_data = f"{project_title}:{project_details}:{project_target}:{start_date}:{end_date}:{project_creator}\n"

    project_file = open("projects.text","a")
    project_file.write(project_data)
    project_file.close()
    print(colored("sucess","green"))

#============================
def show_all_projects():
    projects = open("projects.text","r")
    for project in projects:
        prj_list = project.split(":")
        print(f"""
        Project title:      {prj_list[0]}
        Project details:    {prj_list[1]}
        Project target:     {prj_list[2]}EGP
        Start date:         {prj_list[3]}
        End date:           {prj_list[4]}
        Creator:            {prj_list[5]}
        """)

#============================
def show_user_projects():
    user = get_project_creator()
    file = open("projects.text","r")
    content = file.readlines()
    for project in content:
        if project.count(user):
            prj_list = project.split(":")
            print(f"""
            Project title:      {prj_list[0]}
            Project details:    {prj_list[1]}
            Project target:     {prj_list[2]} EGP
            Start date:         {prj_list[3]}
            End date:           {prj_list[4]}
            Creator:            {prj_list[5]}""")
            
# ================================
def project_exists(project_name):
    file = open("projects.text","r+")
    for project in file:
        prj_list = project.split(":")
        if project_name == prj_list[0]:
            return True
    else:
        return False

# ===============================

def delete_project(project_name):
    if not project_exists(project_name):
        print("Project Not found!")
    else:
        user = get_project_creator()
        file = open("projects.text","r+")
        content = file.readlines()
        for project in content:
            if project.count(user) and project.count(project_name):
                file.seek(0)
                for i in content:
                    if i != project:
                        file.write(i)
        file.truncate()
        
#===============================
def edit_project(project_name):
    if not project_exists(project_name):
        print("Project Not found!")
    else:
        delete_project(project_name)
        create_new_project()
        print("Project has been updated sucessfully")



