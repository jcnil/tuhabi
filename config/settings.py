import os

import mysql.connector


def connect_db():
    """
    :return: connect
    """
    hostdb = os.getenv("MYSQL_HOST")
    port = os.getenv("MYSQL_PORT")
    user = os.getenv("MYSQL_USER")
    passwd = os.getenv("MYSQL_PASS")
    dbname = os.getenv("MYSQL_DATABASE")

    try:
        return mysql.connector.connect(
            host=f'{hostdb}',
            user= f'{user}',
            port=f'{port}', 
            passwd=f'{passwd}', 
            db=f'{dbname}'
        )       
    except Exception as e:
        raise e
