from DHP.app.create import app_data_create
from DHP.app.insert import app_data_inserter
from DHP.app.read import app_data_read
from DHP.context import admin_menu, invalid_option, log_out, owner_menu, user_menu
from DHP.sudo.pwd import password_update_by_admin, password_update_by_user
from DHP.sudo.admin import add_admin, remove_admin
from DHP.Utils.show import (
    show_all_admins,
    show_all_users,
    show_apps_count,
    show_user_count,
)


def UserLoop(id1):
    if id1 != None:
        while True:
            task = input(user_menu())
            if task == "1":
                show_apps_count(id1)
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
                password_update_by_user(id1)
            elif task == "6":
                log_out(id1)
                break
            else:
                invalid_option()
                pass
    else:
        pass


def AdminLoop(id1):
    while True:
        ask1 = input(admin_menu())
        if ask1 == "1":
            show_user_count()
            show_all_users()
        elif ask1 == "2":
            password_update_by_admin(id1)
        elif ask1 == "3":
            try:
                id1 = int(input("Enter the user ID for which you want to show apps : "))
                show_apps_count(id1)
            except ValueError:
                print("Invalid id!!")
        elif ask1 == "4":
            log_out(id1)
            break
        else:
            invalid_option()
            pass


def OwnerLoop(id1):
    while True:
        ask1 = input(owner_menu())
        if ask1 == "1":
            add_admin(id1)
        elif ask1 == "2":
            remove_admin(id1)
        elif ask1 == "3":
            show_user_count()
            show_all_users()
        elif ask1 == "4":
            password_update_by_admin(id1)
        elif ask1 == "5":
            show_all_admins()
        elif ask1 == "6":
            try:
                id1 = int(input("Enter the user id you want to show apps : "))
                show_apps_count(id1)
            except ValueError:
                print("Invalid id")
        elif ask1 == "7":
            log_out(id1)
            break
        else:
            invalid_option()
            pass
