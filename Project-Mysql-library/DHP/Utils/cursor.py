from DHP.Utils.logger import logger
from DHP.context import warn, color

try:
    from mysql import connector
except Exception():
    logger.warning("cursor.py: MySQl-connector is not installed")
    warn("cursor.py: MySQl-connector is not installed")


connection = connector.connect(
    host="localhost", user="root", passwd="1234", database="sys"
)


if connection.is_connected():
    logger.debug("Connected To DataBase | sys")
    print(color("Connected To DataBase"))

    cursor = connection.cursor()
