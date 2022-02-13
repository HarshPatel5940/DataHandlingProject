import csv

from DHP.context import cprint
from DHP.paths import admin_file_path
from DHP.Utils.logger import logger


def admin_login():
    with open(admin_file_path, "r") as f:
        fr = csv.reader(f)
        while True:
            id1 = input("Enter Your ID: ")
            password = input("Enter Your Password: ")
            power = 1
            auth = False

            for row in fr:
                if id1 == row[0] and password == row[1]:
                    power = row[2]
                    print(f"You are Authorized as Level {power} Admin User!")
                    auth = True
                    break
            if auth is True:
                logger.info(f"Super User {id1} has logged in")
                return id1, power
            if auth is False:
                cprint("You Credentials Are Wrong!", "red")
                chance = input("Do you want leave login page? [y] [n] : ")
                if chance == "y":
                    return None
                else:
                    print("Continuing login process....")
