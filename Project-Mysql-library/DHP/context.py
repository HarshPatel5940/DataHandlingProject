from DHP.Utils.logger import logger

try:
    from termcolor import colored, cprint
except Exception as e:
    logger.exception(e)
    print("Termcolor module not found. Please install it.")
    print("check audit.log if needed")


def color(text):
    color_text = colored(text, "cyan")
    return color_text

def warn(text):
    color_text = colored(text, "red")
    print(color_text)

def start_project():
    logger.info("Project has Been Started")
    print(color("xxxxxxxxxxxxxxxx DEVICE USAGE TRACKER xxxxxxxxxxxxxxxx\n\n"))

def app_menu():
    x = f"""
{color("===================== MAIN APP MENU =====================")}
1) Login as user (normal member)
2) Login as super user (admin)
3) Register (signup)
4) Close App
What you want to do [1] [2] [3] [4] : """
    return x


def user_menu():
    x = f"""
{color("===================== Authorised User MENU =====================")}
1) Show all apps
2) Create new app tracking
3) Read tacking data of an app
4) Add tracking data to an existing app
5) {colored("Update User Password", 'magenta')}
6) Logout User
What you want to do [1] [2] [3] [4] [5] [6] : """
    return x


def owner_menu():
    x = f"""
{color("===================== Authorised Owner Menu! =====================")}
1) add admin
2) remove admin
3) Show all users data
4) update user password
5) Show All Admins
6) Show app tracked for the user
7) logout
What you want to do [1] [2] [3] [4] [5] [6] [7]: """
    return x


def admin_menu():
    x = f"""
{color("===================== Authorised Admin Menu! =====================")}
1) Show all users data
2) update user password
3) Show all Apps for a user 
4)logout
What you want to do [1] [2] [3] [4]: """
    return x


def file_exsist_warning():
    x = colored(
        """
WARNING!!

-----The App Data For The Current User Has Already Been Created/Existing.
-----Creating it Again Leads to Loss of Data 

Do you want to continue? [y] or [n] : """,
        "red",
    )
    return x


def invalid_option():
    cprint("Invalid option", "red")


def log_out(id1):
    cprint("Logging Out...", "cyan")
    logger.info(f"User {id1} Logged out.")


def closing():
    cprint("Closing...", "cyan")
