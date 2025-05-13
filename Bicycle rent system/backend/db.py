import mysql.connector

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="*******",
            database="bisiklet"
        )
        print("Connection to MySQL DB successful")
        return connection

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
