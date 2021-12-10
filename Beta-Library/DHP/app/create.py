import csv

from DHP.context import cprint
from DHP.paths import app_data_path
from DHP.Utils.logger import logger


def app_data_create(id1, app_name):
    file_list = ls(app_data_path)

    file_name = f"User{id1}-{app_name}.csv"
    with open(f"{app_data_path}/{file_name}", 'w', newline="") as f:
        fw = csv.writer(f)

        if file_name in file_list:
            opt = input(file_exsist_warning())
            if opt == 'y':
                column = ["Week Number", "Usage Duration(mins)", "Battery Consumptions(%)", "Data Consumption(in MB)",
                          "Times Opened"]
                fw.writerow(column)
                cprint("File Successfully Created! ", "green")
                logger.info(f"User {id1} Overwrite App tracking for {app_name}")

            else:
                cprint("--File Was Not Created--", "red")

        elif file_name not in file_list:
            column = ["Week Number", "Usage Duration(mins)", "Battery Consumptions(%)", "Data Consumption(in MB)",
                      "Times Opened"]
            fw.writerow(column)
            cprint("File Successfully Created! ", "green")
    logger.info(f"User {id1} Created App tracking for {app_name}")
