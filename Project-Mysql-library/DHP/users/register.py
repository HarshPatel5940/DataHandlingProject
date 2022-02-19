from DHP.Utils.cursor import cursor, connection
from DHP.context import warn, color
from DHP.Utils.logger import logger


def sign_up():
    try:
        while True:
            details_ok = True
            pwd = True
            empty = []

            id1 = input("PLEASE ENTER A 4 DIGIT ID!!! (No Less No More)")

            if len(id1) != 4:
                warn("PLEASE ENTER A 4 DIGIT ID!!! (No Less No More)")
                pass

            Q1_userid = "SELECT user_id from UserData WHERE user_id=%s"
            cursor.execute(Q1_userid, (id1,))
            F1_userid = cursor.fetchall()

            details_ok = False if F1_userid != empty else True
            if details_ok == False:
                warn(
                    f"ID: {id1} is Already Being in Already Being Used | Please try a New ID"
                )
                pass

            name = input("Enter your name : ")
            warn(
                """
Note:
    Password cannot be empty
    Password can't start with a space
    Password cannot contain commas
    Password should be minimum 8 characters
    
    """
            )
            password = input("Enter your Password : ")

            if password == "":
                details_ok = False
                warn("Password cannot be empty!!")

            if " " in password:
                details_ok = False
                warn("Password cannot contain space!!")

            if "," in password:
                details_ok = False
                warn(
                    "You Cannot Use Comma In Password",
                    "red",
                )

            if len(password) < 8:
                pwd = False

            if details_ok is True:
                q2_insert = "INSERT INTO UserData VALUES(%s, %s, %s, 1)"
                q2_value = (id1, name, password)
                cursor.execute(q2_insert, q2_value)
                connection.commit()
                print(color("New User Has Been Created Successfully !!"))

                if pwd is False:
                    warn(
                        "\nWe Recommend you Updating password to minimum 8 characters!!!\n\n"
                    )
                break

            if details_ok is False:
                warn("\nInvalid details were provided! \n")
                chance = input("Do you want leave sign-up page? [y] [n] : ")
                if chance == "y":
                    break
                else:
                    print("Continuing Sign-up process....")
    except Exception as e:
        logger.exception("signup loop error \n", e)
        logger.exception(e)
    except KeyboardInterrupt:
        logger.warning("Signup - Loop closed due to Keyboard interrupt Error")
