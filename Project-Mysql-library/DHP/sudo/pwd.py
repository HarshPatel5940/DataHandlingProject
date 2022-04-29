from DHP.Utils.cursor import cursor, connection
from DHP.context import warn
from DHP.Utils.logger import logger


def password_update_by_user(id1):
    auth = False
    pass1 = True
    cprint(
        """
Note:
    Password cannot be empty
    Password can't start with a space
    Password cannot contain commas
    Password should be minimum 8 characters""",
        "red",
    )

    old_password = input("Enter the old password : ")
    pwd = input("Enter the new password : ")
    confirm = input("Confirm the new password : ")

    with open(user_file_path, "r") as f:
        fr = csv.reader(f)

        for row in fr:
            if id1 in row and old_password in row:
                auth = True

    if not auth:
        cprint("Did not enter proper old password!!", "red")
    elif auth:
        if confirm != pwd:
            cprint("Password did not match", "red")
            pass1 = False

        if pwd == "":
            pass1 = False
            cprint("Password cannot be empty!!", "red")

        if " " in pwd:
            pass1 = False
            cprint("Password cannot contain space!!", "red")

        if "," in pwd:
            pass1 = False
            cprint(
                "You Cannot Use Comma In Password as it will mess up the database",
                "red",
            )

        if len(pwd) < 8:
            cprint("Password should be minimum 8 characters", "red")
            pass1 = False

        if auth is True and pass1 is True:
            before = []

            with open(user_file_path, "r") as f:
                fr = csv.reader(f)

                for row in fr:
                    if row[0] == id1:
                        row[2] = pwd
                        before.append(row)
                    else:
                        before.append(row)

            with open(user_file_path, "w", newline="") as f:
                file = csv.writer(f)
                file.writerows(before)

            cprint("User Password Updated Successfully", "green")
            logger.warning(
                f"User {id1} Has Changed password. [from: {old_password} to: {pwd}]"
            )
        else:
            print("Password was not update due to above errors")
    else:
        logger.info("Something went wrong!!!")


def password_update_by_admin(id2):
    id1 = input("Enter id of the user u wanna update password : ")
    pwd = input("Enter the new password for the user : ")
    before = []

    with open(user_file_path, "r", newline="") as f:
        file = csv.reader(f)

        for row in file:
            if row[0] == id1:
                row[2] = pwd
                before.append(row)
            else:
                before.append(row)

    with open(user_file_path, "w", newline="") as f:
        file = csv.writer(f)
        file.writerows(before)

    cprint("User Password Updated Successfully", "green")
    logger.warning(f"{id2} Has Changed password of {id1} to {pwd}")
