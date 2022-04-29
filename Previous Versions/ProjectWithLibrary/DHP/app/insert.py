import csv
from os import listdir as ls
from DHP.context import cprint
from DHP.paths import app_data_path
from DHP.Utils.logger import logger


def app_data_inserter(id1, app_name):
    try:
        file_name = f"User{id1}-{app_name}.csv"
        with open(f"{app_data_path}/{file_name}", 'a', newline="") as f:
            fw = csv.writer(f)
            week_no = int(input("Enter The Week Number: "))

            try:
                usage_time = int(input(f"Enter the Usage Duration Of {app_name} for Week{week_no} (in minutes): "))
                battery_consumption = int(input(f"Enter the Battery Consumed by {app_name} for Week{week_no}: "))
                data_consumption = int(input(f"Enter the Data Consumed by {app_name} for Week{week_no} (in Megabytes): "))
                times_opened = int(input(f"Enter How Many Times You Opened {app_name} in Week{week_no}: "))
                row = [f"Week{week_no}", usage_time, battery_consumption, data_consumption, times_opened]
                fw.writerow(row)
            except ValueError:
                cprint("there was a value error", 'red')

            cprint(f"\n-----Data for Week{week_no} Has Been Successfully Added!-----\n\n", 'green')

            logger.info(f"User {id1} Added Data for {app_name} with Week-No {week_no}")

    except FileNotFoundError:
        cprint("File Not Found", 'red')
