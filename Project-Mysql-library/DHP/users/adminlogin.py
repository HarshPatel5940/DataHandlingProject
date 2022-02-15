from DHP.Utils.cursor import cursor
from DHP.context import warn, color
from DHP.Utils.logger import logger


def admin_login():
    try:
        id1 = input("Enter Your ID: ")
        password = input("Enter Your Password: ")
        auth = False

        QUERY = (
            """SELECT user_power FROM UserData WHERE user_id=%s AND user_password=%s"""
        )
        VAL = (id1, password)

        cursor.execute(QUERY, VAL)

        power = str(cursor.fetchall())
        power = power[2] if len(power) > 4 else "1"

        auth = True if power == "2" or power == "3" else False

        if auth is True:
            logger.info(f"Super User {id1} has Logged In! Power: {power}")
            print(color(f"Super User {id1} has Logged In! Power: {power}"))
            return id1, power
        if auth is False:
            warn("You Don't Have Enough Power!! ( OR Wrong Credentials!!)")
            return None

    except Exception as e:
        logger.exception("admin login loop error \n", e)
        logger.exception(e)
    except KeyboardInterrupt:
        logger.warning("admin login - Loop closed due to Keyboard interrupt Error")
