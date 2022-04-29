from time import sleep
from DHP.context import warn, color
from DHP.Utils.cursor import connection, cursor
from DHP.Utils.logger import logger

cursor.execute("SHOW DATABASES;")
DataBases = cursor.fetchall()


def CreateTableUser():
    cursor.execute(
        """
    CREATE TABLE UserData(
        user_id SMALLINT PRIMARY KEY,
        user_name VARCHAR(20) NOT NULL,
        user_password VARCHAR(20) NOT NULL,
        user_power TINYINT NOT NULL
    )
    """
    )
    logger.warning("TABLE NOT FOUND | Created New Table UserData")
    warn(">> TABLE NOT FOUND | Created New Table UserData")

    cursor.execute(
        "INSERT INTO UserData values('5940', 'Harsh Patel', 'abcd1234',  '3');"
    )
    connection.commit()
    print(cursor.rowcount, "Record Inserted!!")
    sleep(1)


def CreateDataBase():
    cursor.execute("CREATE DATABASE SchoolMysqlProject")
    logger.warning("DataBase Not Found | Created New Database SchoolMysqlProject")
    warn(">> DataBase Not Found | Created New Database SchoolMysqlProject")

    sleep(1)

    cursor.execute("USE SchoolMysqlProject;")

    cursor.execute("SHOW TABLES;")
    Tables = cursor.fetchall()
    print(Tables)

    sleep(3)

    if ("UserData",) not in Tables:
        CreateTableUser()

    cursor.execute("SELECT * FROM UserData")
    TableData = cursor.fetchall()

    print(TableData)


def SetupUser():
    if ("schoolmysqlproject",) not in tuple(DataBases):
        print(tuple(DataBases))
        CreateDataBase()
    else:
        cursor.execute("use schoolmysqlproject;")
        cursor.execute("SELECT * FROM UserData")

        TableData = cursor.fetchall()
        if len(TableData) == 0:
            logger.critical(
                "TABLE FOUND EMPTY | ADDING DEFAULT VALUES | BUT HOW THE HELL THIS HAPPEN???"
            )
            cursor.execute("DROP TABLE UserData")
            CreateTableUser()

        print(color("DataBase Setup Done!"))
        logger.debug("INITIALIZATION OF DATABASE COMPLETE")
        logger.info("DB Changed | sys => schoolmysqlproject")
