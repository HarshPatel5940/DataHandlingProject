from DHP.Utils.cursor import cursor
from DHP.context import warn, color
from DHP.Utils.logger import logger


def login():
    try:
        while True:
            id1 = input("Enter Your ID: ")
            password = input("Enter Your Password: ")
            auth = False

            QUERY = """SELECT * FROM UserData WHERE user_id=%s AND user_password=%s"""
            VAL = (id1, password)

            cursor.execute(QUERY, VAL)

            if len(cursor.fetchall()) == 1:
                auth = True

            if auth is True:
                print(color("Successfully Logged in!!"))
                logger.info(f"User {id1} has Logged In!")
                return id1
            if auth is False:
                warn("You Credentials Are Wrong!\nTRY AGAIN")
                chance = input("Do you want leave login page? [y] [n] : ")
                if chance == "y":
                    return None
                else:
                    print("Invalid option! continuing login process....")
    except Exception as e:
        logger.exception("login loop error \n", e)
        logger.exception(e)
    except KeyboardInterrupt:
        logger.warning("login - Loop closed due to Keyboard interrupt Error")
