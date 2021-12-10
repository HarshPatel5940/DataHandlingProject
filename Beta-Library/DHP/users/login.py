from csv import reader

from DHP.context import colored, cprint
from DHP.paths import user_file_path
from DHP.Utils.logger import logger


def login():
    with open(user_file_path, "r") as f:
        fr = reader(f)
        while True:
            id1 = input("Enter Your ID: ")
            password = input("Enter Your Password: ")
            auth = False
            for row in fr:
                if id1 in row and password in row:
                    name = colored(f"=> {row[1]}", "cyan")
                    print(f"You are Authorized with has {name}!")
                    auth = True
                    break
            if auth is True:
                logger.info(f"User {id1} has logged in")
                return id1
            if auth is False:
                cprint("You Credentials Are Wrong!\nTRY AGAIN", "red")
                chance = input("Do you want leave login page? [y] [n] : ")
                if chance == "y":
                    break
                else:
                    print("Invalid option! continuing login process....")
