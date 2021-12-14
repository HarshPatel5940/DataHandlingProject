import csv

from DHP.context import cprint
from DHP.paths import user_file_path
from DHP.Utils.logger import logger
from DHP.Utils.create import write_user


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

