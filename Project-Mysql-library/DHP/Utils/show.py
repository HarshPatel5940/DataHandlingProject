import csv
from os import listdir as ls

from DHP.paths import *
from DHP.Utils.logger import logger

try:
    from pandas import DataFrame as Df
except Exception as e:
    logger.exception(e)
    print("Pandas module not found. Please install it.")
    print("check audit.log if needed")


def show_all_users():
    with open(user_file_path, "r") as f:
        reader = csv.reader(f)
        print(
            Df(
                reader,
            )
        )


def show_all_admins():
    with open(admin_file_path, "r") as f:
        reader = csv.reader(f)
        print(
            Df(
                reader,
            )
        )


def show_user_count():
    with open(user_file_path, "r") as f:
        fr = csv.reader(f)
        print(f"Total Users = {len(list(fr))-1}")


def show_apps_count(id1):
    user_file = []
    app_list = []
    app_list_final = []
    file_list = ls(app_data_path)

    for data in file_list:
        if f"User{id1}" in data:
            user_file.append(data)

    for data in user_file:
        lst1 = data.split("-")
        app_list.append(lst1[1])

    for app in app_list:
        name = app.split(".")
        app_list_final.append(name[0])

    if not app_list_final:
        cprint("User is Invalid or User Has No Apps Tracked", "red")
    else:
        app_count = len(app_list_final)
        print(
            f"Total Apps Tracked For User{id1} = {app_count}\n The Apps Are ---> {app_list_final}"
        )
