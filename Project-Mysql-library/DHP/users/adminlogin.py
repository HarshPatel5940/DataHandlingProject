from DHP.Utils.cursor import cursor
from DHP.context import warn
from DHP.Utils.logger import logger


def admin_login():
    id1 = input("Enter Your ID: ")
    password = input("Enter Your Password: ")
    auth = False

    QUERY = """SELECT user_power FROM UserData WHERE user_id=%s AND user_password=%s"""
    VAL = (id1, password)

    cursor.execute(QUERY, VAL)

    power = cursor.fetchall()
    print(f"--> {power}")

    if len(cursor.fetchall()) == 1:
        auth = True

    if auth is True:
        logger.info(f"Super User {id1} has Logged In! Power: {power}")
        return id1, power
    if auth is False:
        warn("You Credentials Are Wrong!\nTRY AGAIN")
        chance = input("Do you want leave login page? [y] [n] : ")
        if chance == "y":
            return None
        else:
            print("Invalid option! continuing login process....")
