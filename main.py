from modules import *
import os


os.system("")
print(color("xxxxxxxxxxxxxxxx DEVICE USAGE TRACKER xxxxxxxxxxxxxxxx\n\n"))


while True:
    ask1 = input(app_menu())
    if ask1 == "1":
        id1 = login()
        while True:
            task = input(user_menu())
            if task == "1":
                apps_count(id1)
            elif task == "2":
                app = input("Enter the name of the app you want to create : ")
                app_data_create(id1, app)
            elif task == "3":
                app = input("Enter the name of the app you want to read data: ")
                app_data_read(id1, app)
            elif task == "4":
                app = input("Enter the name of the app you want to add data: ")
                app_data_inserter(id1, app)
            elif task == "5":
                user_password_update(id1)
            elif task == "6":
                log_out()
                break
            else:
                invalid_option()
                pass
    elif ask1 == "2":
        tup = admin_login()
        id1 = tup[0]
        power = tup[1]

        if power == "3":
            while True:
                ask1 = input(owner_menu())
                if ask1 == "1":
                    add_admin()
                elif ask1 == "2":
                    remove_admin()
                elif ask1 == "3":
                    user_count()
                    show_all_users()
                elif ask1 == "4":
                    admin_password_update()
                elif ask1 == "5":
                    show_all_admins()
                elif ask1 == "6":
                    try:
                        id1 = int(input("Enter the user id you want to show apps : "))
                        apps_count(id1)
                    except ValueError:
                        print("Invalid id")
                elif ask1 == "7":
                    log_out()
                    break
                else:
                    invalid_option()
                    pass

        elif power == "2":
            while True:
                ask1 = input(admin_menu())
                if ask1 == "1":
                    user_count()
                    show_all_users()
                elif ask1 == "2":
                    admin_password_update()
                elif ask1 == "3":
                    try:
                        id1 = int(input("Enter the user ID for which you want to show apps : "))
                        apps_count(id1)
                    except ValueError:
                        print("Invalid id!!")
                elif ask1 == "4":
                    log_out()
                    break
                else:
                    invalid_option()
                    pass
        else:
            invalid_option()
    elif ask1 == "3":
        sign_up()
    elif ask1 == "4":
        closing()
        break
    else:
        invalid_option()
        pass
