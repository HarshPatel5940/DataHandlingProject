import csv
from DHP.Utils.logger import logger
from DHP.context import cprint
from DHP.paths import app_data_path
try: 
    from pandas import DataFrame as Df
except Exception as e:
    logger.exception(e)
    print("Pandas module not found. Please install it.")
    print("check audit.log if needed")


def app_data_read(id1, app_name):
    file_name = f"User{id1}-{app_name}.csv"
    found = False

    try:
        with open(f"{app_data_path}/{file_name}", 'r') as file_open:
            file_reader = csv.reader(file_open)
            opt = input(
                "Select The Task\n1) Read Full Data\n2) Read Particular Week\nYour Option [1]or[2] : ")
            if opt == "1":
                print(Df(file_reader, ))
            elif opt == "2":
                week_number = input("Enter the Week for which you want to view the data  : ")
                header = ["Week Number", "Usage Duration(mins)", "Battery Consumptions(%)", "Data Consumption(in MB)",
                          "Times Opened"]
                for row in file_reader:
                    if f"Week{week_number}" == row[0]:
                        print(Df(row, header))
                        found = True
                if found is False:
                    cprint("no such app found", 'red')
            else:
                invalid_option()

    except FileNotFoundError:
        print("No Such App was Found")
