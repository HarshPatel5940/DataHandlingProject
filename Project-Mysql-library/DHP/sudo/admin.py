from DHP.context import warn, color
from DHP.Utils.cursor import cursor, connection
from DHP.Utils.logger import logger


def add_admin(id2):
    try:
        while True:
            details_ok = True
            empty = []

            id1 = input("PLEASE ENTER A 4 DIGIT ID!!! (No Less No More): ")

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
                warn("\nInvalid details were provided! \n")
                chance = input("Do you want leave add admin page? [y] [n] : ")
                if chance == "y":
                    break
                else:
                    print("Continuing Add Admin process....")

            elif details_ok is True:
                name = input("PLease Input a Name for the admin: ")
                passwd = input("Please Input a Password for the admin: ")
                q2_insert = "INSERT INTO UserData VALUES(%s, %s, %s, 2)"
                q2_value = (id1, name, passwd)
                cursor.execute(q2_insert, q2_value)
                connection.commit()
                print(color("New User Has Been Created Successfully !!"))
                logger.warning(f"New Admin Added {id1} | By {id2}")
                break
            else:
                logger.critical("Something Breaking loop | add admin")
                break

    except Exception as e:
        logger.exception("Add admin loop error \n", e)
        logger.exception(e)
    except KeyboardInterrupt:
        logger.warning("Add Admin - Loop closed due to Keyboard interrupt Error")


def remove_admin(id2):
    try:
        while True:
            details_ok = True
            empty = []

            id1 = input("PLEASE ENTER A 4 DIGIT ID!!!: ")

            Q1_userid = "SELECT user_id from UserData WHERE user_id=%s"
            cursor.execute(Q1_userid, (id1,))
            F1_userid = cursor.fetchall()

            details_ok = False if F1_userid != empty else True
            if details_ok == True:
                warn(f"ID: {id1} is Not Being Used | Please try a Existing ID")

                warn("\nInvalid ID was provided! \n")
                chance = input("Do you want leave remove admin page? [y] [n] : ")
                if chance == "y":
                    break
                else:
                    print("Continuing Remove Admin process....")
            elif details_ok is False:
                q2_insert = "DELETE FROM UserData where user_id=%s"
                cursor.execute(q2_insert, (id1,))
                connection.commit()
                print(color("User Has Been Deleted Successfully !!"))
                logger.warning(f"New Admin Added {id1} | By {id2}")
                break
            else:
                logger.critical("Something Breaking loop | add admin")
                break

    except Exception as e:
        logger.exception("remove admin loop error \n", e)
        logger.exception(e)
    except KeyboardInterrupt:
        logger.warning("remove Admin - Loop closed due to Keyboard interrupt Error")
