from os import system

from DHP.context import app_menu, closing, invalid_option, start_project
from DHP.helperloops import AdminLoop, OwnerLoop, UserLoop
from DHP.users.adminlogin import admin_login
from DHP.users.login import login
from DHP.users.register import sign_up
from DHP.Utils.logger import logger


def LibProject():
    try:
        system("")
        start_project()

        while True:
            ask1 = input(app_menu())
            if ask1 == "1":
                id1 = login()
                UserLoop(id1)
            elif ask1 == "2":
                tup = admin_login()
                if tup != None:
                    id2 = tup[0]
                    power = tup[1]
                    if power == "2":
                        AdminLoop(id2)
                    if power == "3":
                        OwnerLoop(id2)
            elif ask1 == "3":
                sign_up()
            elif ask1 == "4":
                closing()
                break
            else:
                invalid_option()

    except Exception as e:
        print(e)
        logger.exception("Main Loop Error\n", e)
    except KeyboardInterrupt:
        logger.warning("Main Loop closed due to Keyboard interrupt Error")
