import mysql.connector
import json

def connect_db():
    db_config = open("config/db_config.json")
    config = json.load(db_config)

    mysql_conn = mysql.connector.connect(
        host=config.get("host"),
        user=config.get("user"),
        passwd=config.get("passwd"),
        database=config.get("database")
    )

    return  mysql_conn