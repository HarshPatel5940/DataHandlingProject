import csv
from os import listdir as ls

from config import admin_file_path, app_data_path, logger, user_file_path

try:
    from pandas import DataFrame as Df  # pip install pandas & numpy
    from termcolor import colored, cprint
except Exception as e:
    logger.exception(e)
    print("Environment Requirement Not satisfied. (install pandas and termcolor properly)")
    print("check audit.log if needed")


def color(text):
    color_text = colored(text, 'cyan')
    return color_text


def app_menu():
    x = f"""
{color("===================== MAIN APP MENU =====================")}
1) Login as user (normal member)
2) Login as super user (admin)
3) Register (signup)
4) Close App
What you want to do [1] [2] [3] [4] : """
    return x


def user_menu():
    x = f"""
{color("===================== Authorised User MENU =====================")}
1) Show all apps
2) Create new app tracking
3) Read tacking data of an app
4) Add tracking data to an existing app
5) {colored("Update User Password", 'magenta')}
6) Logout User
What you want to do [1] [2] [3] [4] [5] [6] : """
    return x


def owner_menu():
    x = f"""
{color("===================== Authorised Owner Menu! =====================")}
1) add admin
2) remove admin
3) Show all users data
4) update user password
5) Show All Admins
6) Show app tracked for the user
7) logout
What you want to do [1] [2] [3] [4] [5] [6] [7]: """
    return x


def admin_menu():
    x = f"""
{color("===================== Authorised Admin Menu! =====================")}
1) Show all users data
2) update user password
3) Show all Apps for a user 
4)logout
What you want to do [1] [2] [3] [4]: """
    return x


def invalid_option():
    cprint("Invalid option", "red")


def log_out(id1):
    cprint("Logging Out...", "cyan")
    logger.info(f"User {id1} Logged out.")


def closing():
    cprint("Closing...", "cyan")


def file_exsist_warning():
    x = colored("""
WARNING!!

-----The App Data For The Current User Has Already Been Created/Existing.
-----Creating it Again Leads to Loss of Data 

Do you want to continue? [y] or [n] : """, "red")
    return x


def show_all_users():
    with open(user_file_path, 'r') as f:
        reader = csv.reader(f)
        print(Df(reader, ))


def show_all_admins():
    with open(admin_file_path, 'r') as f:
        reader = csv.reader(f)
        print(Df(reader, ))


def user_count():
    with open(user_file_path, "r") as f:
        fr = csv.reader(f)
        print(f"Total Users = {len(list(fr))-1}")


def apps_count(id1):
    user_file = []
    app_list = []
    app_list_final = []
    file_list = ls(app_data_path)

    for data in file_list:
        if f"User{id1}" in data:
            user_file.append(data)

    for data in user_file:
        lst1 = data.split('-')
        app_list.append(lst1[1])

    for app in app_list:
        name = app.split('.')
        app_list_final.append(name[0])

    if not app_list_final:
        cprint("User is Invalid or User Has No Apps Tracked", "red")
    else:
        app_count = len(app_list_final)
        print(f"Total Apps Tracked For User{id1} = {app_count}\n The Apps Are ---> {app_list_final}")


def write_user(id11, name, password):
    with open(user_file_path, "a", newline="") as f:
        cprint("Data Is OK", 'green')
        file = csv.writer(f)
        user_row = [id11, name, password]
        file.writerow(user_row)


def app_data_read(id1, app_name):
    file_name = f"User{id1}-{app_name}.csv"
    found = False

    try:
        with open(f"{app_data_path}/{file_name}", 'r') as file_open:
            file_reader = csv.reader(file_open)
            opt = input(
                "Select The Task\n1) Read Full Data\n2) Read Particular Week\nYour Option [1]or[2] : ")
            if opt == "1":
                print(Df(file_reader, ))
            elif opt == "2":
                week_number = input("Enter the Week for which you want to view the data  : ")
                header = ["Week Number", "Usage Duration(mins)", "Battery Consumptions(%)", "Data Consumption(in MB)",
                          "Times Opened"]
                for row in file_reader:
                    if f"Week{week_number}" == row[0]:
                        print(Df(row, header))
                        found = True
                if found is False:
                    cprint("no such app found", 'red')
            else:
                invalid_option()

    except FileNotFoundError:
        print("No Such App was Found")


def sign_up():
    while True:
        details_ok = True
        pwd = True
        id1 = input("Enter your id : ")
        name = input("Enter your name : ")
        password = input("Enter your Password : ")

        with open(user_file_path, 'r') as file1:
            reader = csv.reader(file1)

            for row in reader:
                if row[0] == id1:
                    cprint(f"ERROR (same id Provided) ==> {row}", 'red')
                    details_ok = False
                if row[1] == name:
                    cprint(f"ERROR (same Name Provided) ==> {row}", 'red')
                    details_ok = False

        if password == "":
            details_ok = False
            cprint("Password cannot be empty!!", 'red')

        if " " in password:
            details_ok = False
            cprint("Password cannot be space!!", 'red')

        if "," in password:
            details_ok = False
            cprint("You Cannot Use Comma In Password as it will mess up the database", 'red')

        if len(password) < 8:
            pwd = False

        if details_ok is True:
            write_user(id1, name, password)
            cprint("New User Has Been Created Successfully !!", 'cyan')
            if pwd is False:
                cprint("We Recommend you Updating password to minimum 8 characters!!!", 'red')
            break
        if details_ok is False:
            cprint("\nInvalid details provided! \n", 'red')
            chance = input("Do you want leave sign-up page? [y] [n] : ")
            if chance == "y":
                break
            else:
                print("Invalid option! Continuing Sign-up process....")


def login():
    with open(user_file_path, 'r') as f:
        fr = csv.reader(f)
        while True:
            id1 = input("Enter Your ID: ")
            password = input("Enter Your Password: ")
            auth = False
            for row in fr:
                if id1 in row and password in row:
                    name = colored(f"=> {row[1]}", 'cyan')
                    print(f"You are Authorized with has {name}!")
                    auth = True
                    break
            if auth is True:
                logger.info(f"User {id1} has logged in")
                return id1
            if auth is False:
                cprint("You Credentials Are Wrong!\nTRY AGAIN", 'red')
                chance = input("Do you want leave login page? [y] [n] : ")
                if chance == "y":
                    break
                else:
                    print("Invalid option! continuing login process....")


def admin_login():
    with open(admin_file_path, 'r') as f:
        fr = csv.reader(f)
        while True:
            id1 = input("Enter Your ID: ")
            password = input("Enter Your Password: ")
            power = 1
            auth = False

            for row in fr:
                if id1 in row and password in row:
                    power = row[2]
                    print(f"You are Authorized as Level {power} Admin User!")
                    auth = True
                    break
            if auth is True:
                logger.info(f"Super User {id1} has logged in")
                return id1, power
            if auth is False:
                cprint("You Credentials Are Wrong!", 'red')
                chance = input("Do you want leave login page? [y] [n] : ")
                if chance == "y":
                    break
                else:
                    print("Continuing login process....")


def add_admin(id2):
    id1 = int(input("Enter Admin ID : "))
    pwd = input("Enter Admin Password : ")
    power = "2"  # by default 2
    lst = [id1, pwd, power]

    with open(admin_file_path, "a", newline="") as f:
        file = csv.writer(f)
        file.writerow(lst)
    logger.warning(f"{id2} Added New Admin with ID {id1}")
    print(f"New Super User (Admin) has been added, ID: {id1}")


def remove_admin(id2):
    id1 = input("Enter The ID Of The Admin You Want To Remove : ")
    before = []

    with open(admin_file_path, "r", newline="") as f:
        file = csv.reader(f)

        for row in file:
            if row[0] != id1:
                before.append(row)

    with open(admin_file_path, "w", newline="") as f:
        file = csv.writer(f)
        file.writerows(before)

    logger.warning(f"{id2} Removed Admin with ID {id1}")
    print(f"Super User (Admin) has been Removed, ID: {id1}")


def admin_password_update(id2):
    id1 = input("Enter id of the user u wanna update password : ")
    pwd = input("Enter the new password for the user : ")
    before = []

    with open(user_file_path, "r", newline="") as f:
        file = csv.reader(f)

        for row in file:
            if row[0] == id1:
                row[2] = pwd
                before.append(row)
            else:
                before.append(row)

    with open(user_file_path, "w", newline="") as f:
        file = csv.writer(f)
        file.writerows(before)

    cprint("User Password Updated Successfully", 'green')


def user_password_update(id1):
    auth = False
    pass1 = True
    cprint("""
Note:
    Password cannot be empty
    Password can't start with a space
    Password cannot contain commas
    Password should be minimum 8 characters""", 'red')

    old_password = input("Enter the old password : ")
    pwd = input("Enter the new password : ")
    confirm = input("Confirm the new password : ")

    with open(user_file_path, 'r') as f:
        fr = csv.reader(f)

        for row in fr:
            if id1 in row and old_password in row:
                auth = True

    if confirm != pwd:
        cprint("Password did not match", 'red')
        pass1 = False

    if pwd == "":
        pass1 = False
        cprint("Password cannot be empty!!", 'red')

    if pwd.startswith(" "):
        pass1 = False
        cprint("Password cannot be start with space!!", 'red')

    if "," in pwd:
        pass1 = False
        cprint("You Cannot Use Comma In Password as it will mess up the database", 'red')

    if len(pwd) < 8:
        cprint("Password should be minimum 8 characters", 'red')
        pass1 = False

    if auth is True and pass1 is True:
        before = []

        for row in fr:
            if row[0] == id1:
                row[2] = pwd
                before.append(row)
            else:
                before.append(row)

        with open(user_file_path, "w", newline="") as f:
            file = csv.writer(f)
            file.writerows(before)

        cprint("User Password Updated Successfully", 'green')
        logger.warning(f"User {id1} Has Changed password.")
    elif not auth:
        cprint("Did not enter proper old password!!", 'red')
    else:
        print("Password was not update due to above errors")
    f.close()


def app_data_create(id1, app_name):
    file_list = ls(app_data_path)

    file_name = f"User{id1}-{app_name}.csv"
    with open(f"{app_data_path}/{file_name}", 'w', newline="") as f:
        fw = csv.writer(f)

        if file_name in file_list:
            opt = input(file_exsist_warning())
            if opt == 'y':
                column = ["Week Number", "Usage Duration(mins)", "Battery Consumptions(%)", "Data Consumption(in MB)",
                          "Times Opened"]
                fw.writerow(column)
                cprint("File Successfully Created! ", "green")
                logger.info(f"User {id1} Overwrite App tracking for {app_name}")

            else:
                cprint("--File Was Not Created--", "red")

        elif file_name not in file_list:
            column = ["Week Number", "Usage Duration(mins)", "Battery Consumptions(%)", "Data Consumption(in MB)",
                      "Times Opened"]
            fw.writerow(column)
            cprint("File Successfully Created! ", "green")
    logger.info(f"User {id1} Created App tracking for {app_name}")


def app_data_inserter(id1, app_name):
    try:
        file_name = f"User{id1}-{app_name}.csv"
        with open(f"{app_data_path}/{file_name}", 'a', newline="") as f:
            fw = csv.writer(f)
            week_no = int(input("Enter The Week Number: "))

            try:
                usage_time = int(input(f"Enter the Usage Duration Of {app_name} for Week{week_no} (in minutes): "))
                battery_consumption = int(input(f"Enter the Battery Consumed by {app_name} for Week{week_no}: "))
                data_consumption = int(input(f"Enter the Data Consumed by {app_name} for Week{week_no} (in Megabytes): "))
                times_opened = int(input(f"Enter How Many Times You Opened {app_name} in Week{week_no}: "))
                row = [f"Week{week_no}", usage_time, battery_consumption, data_consumption, times_opened]
                fw.writerow(row)
            except ValueError:
                cprint("there was a value error", 'red')

            cprint(f"\n-----Data for Week{week_no} Has Been Successfully Added!-----\n\n", 'green')

            logger.info(f"User {id1} Added Data for {app_name} with Week-No {week_no}")

    except FileNotFoundError:
        cprint("File Not Found", 'red')
