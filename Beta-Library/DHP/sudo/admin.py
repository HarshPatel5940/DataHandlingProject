import csv

from DHP.context import cprint
from DHP.paths import admin_file_path
from DHP.Utils.logger import logger


def add_admin(id2):

    try:
        id1 = int(input("Enter Admin ID : "))
    except ValueError:
        cprint("ID Must Be An Integer", "red")
        return

    pwd = input("Enter Admin Password : ")
    power = "2"  # by default 2
    lst = [id1, pwd, power]

    with open(admin_file_path, "a", newline="") as f:
        file = csv.writer(f)
        file.writerow(lst)
    logger.warning(f"{id2} Added New Admin - ID {id1}")
    cprint(f"New Super User (Admin) has been added, ID: {id1}", "green")


def remove_admin(id2):
    try:
        id1 = input("Enter The ID Of The Admin You Want To Remove : ")
    except ValueError:
        cprint("ID Must Be An Integer", "red")
        return
    before = []

    with open(admin_file_path, "r", newline="") as f:
        file = csv.reader(f)

        for row in file:
            if row[0] != id1:
                before.append(row)

    with open(admin_file_path, "w", newline="") as f:
        file = csv.writer(f)
        file.writerows(before)

    logger.warning(f"{id2} Removed Admin with ID - {id1}")
    cprint(f"Super User (Admin) has been Removed, ID: {id1}", "green")
