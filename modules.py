import csv
from pandas import DataFrame as Df
from os import listdir as ls
from termcolor import colored, cprint  # @nishanth & @ suraj ** REQUIRE : pip install termcolor **

user_file_path = "D:\Sindhi Model School (SMS)\HARSH\.PROGRAMS\School\project\data.csv"
admin_file_path = "D:\Sindhi Model School (SMS)\HARSH\.PROGRAMS\School\project\data_admin.csv"
app_data_path = "D:\Sindhi Model School (SMS)\HARSH\.PROGRAMS\School\project\data"


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


def log_out():
    cprint("Logging Out...", "cyan")


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
    file1 = open(user_file_path, 'r')
    reader = csv.reader(file1)
    print(Df(reader, ))
    file1.close()


def show_all_admins():
    file1 = open(admin_file_path, 'r')
    reader = csv.reader(file1)
    print(Df(reader, ))
    file1.close()


def user_count():
    f = open(user_file_path, "r")
    fr = csv.reader(f)
    users = 0
    for row in fr:
        users += 1

    users -= 1
    cprint(f" == > Number of Users Are {users}", "cyan")


def apps_count(id1):
    user_file = []
    app_list = []
    app_list_final = []
    file_list = ls(app_data_path)
    for data in file_list:
        if f"User{id1}" in data:
            user_file.append(data)
    for data in user_file:
        Lst1 = data.split('-')
        app_list.append(Lst1[1])

    for app in app_list:
        name = app.split('.')
        app_list_final.append(name[0])
    if app_list_final == []:
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


def app_data_create(id1, app_name):
    file_list = ls(app_data_path)

    file_name = f"User{id1}-{app_name}.csv"

    if file_name in file_list:
        opt = input(file_exsist_warning())
        if opt == 'y':
            f = open(f"{app_data_path}/{file_name}", 'w', newline="")
            fw = csv.writer(f)
            column = ["Week Number", "Usage Duration(mins)", "Battery Consumptions(%)", "Data Consumption(in MB)",
                      "Times Opened"]
            fw.writerow(column)
            cprint("File Successfully Created! ", "green")

        else:
            cprint("--File Was Not Created--", "red")

    elif file_name not in file_list:
        f = open(f"{app_data_path}/{file_name}", 'w', newline="")
        fw = csv.writer(f)
        column = ["Week Number", "Usage Duration(mins)", "Battery Consumptions(%)", "Data Consumption(in MB)",
                  "Times Opened"]
        fw.writerow(column)
        cprint("File Successfully Created! ", "green")


def app_data_inserter(id1, app_name):
    file_name = f"User{id1}-{app_name}.csv"
    f = open(f"{app_data_path}/{file_name}", 'a', newline="")
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


def app_data_read(id1, app_name):
    file_name = f"User{id1}-{app_name}.csv"
    found = False
    try:
        file_open = open(f"{app_data_path}/{file_name}", 'r')
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

        file1 = open(user_file_path, 'r')
        reader = csv.reader(file1)

        for row in reader:
            if row[0] == id1:
                cprint(f"ERROR IN (same id) ==> {row}", 'red')
                details_ok = False
            if row[1] == name:
                cprint(f"ERROR IN (same Name) ==> {row}", 'red')
                details_ok = False
        file1.close()

        if password == "":
            details_ok = False
            cprint("Password cannot be empty!!", 'red')

        if password == " ":
            details_ok = False
            cprint("Password cannot be space!!", 'red')

        if "," in password:
            details_ok=False
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
    while True:
        id1 = input("Enter Your ID: ")
        password = input("Enter Your Password: ")
        f = open(user_file_path, 'r')
        fr = csv.reader(f)
        auth = False
        for row in fr:
            if id1 in row and password in row:
                name = colored(f"=> {row[1]}", 'cyan')
                print(f"You are Authorized with has {name}!")
                auth = True
                break
        if auth is True:
            break
        if auth is False:
            cprint("You Credentials Are Wrong!\nTRY AGAIN", 'red')
            chance = input("Do you want leave login page? [y] [n] : ")
            if chance == "y":
                break
            else:
                print("Invalid option! continuing login process....")
    return id1


def admin_login():
    while True:
        f = open(admin_file_path, 'r')
        id1 = input("Enter Your ID: ")
        password = input("Enter Your Password: ")
        fr = csv.reader(f)
        power = 1
        auth = False

        for row in fr:
            if id1 in row and password in row:
                power = row[2]
                print(f"You are Authorized as Level {power} Admin User!")
                auth = True
                break
        if auth is True:
            break
        if auth is False:
            cprint("You Credentials Are Wrong!" , 'red')
            chance = input("Do you want leave login page? [y] [n] : ")
            if chance == "y":
                break
            else:
                print("Continuing login process....")
    return id1, power


def add_admin():
    id1 = int(input("Enter Admin ID : "))
    pwd = input("Enter Admin Password : ")
    power = "2"  # by default 2
    lst = [id1, pwd, power]

    f = open(admin_file_path, "a", newline="")
    file = csv.writer(f)
    file.writerow(lst)
    f.close()
    print(f"New Admin User With ID{id1} Has Been Added! ")


def remove_admin():
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

    print(f"Admin User With ID{id1} Has Been Removed! ")


def admin_password_update():
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

    f = open(user_file_path, 'r')
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
    elif not auth:
        cprint("Did not enter proper old password!!", 'red')
    else:
        print("Password was not update due to above errors")
