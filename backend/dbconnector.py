import datetime
from datetime import date
import mysql.connector
from mysql.connector import Error

def create_connection(host_name, user_name, user_password, database_name):
    connection = None
    # try blocks are used for perfect code in case it crashes, and reduces performance

    try:
        connection = mysql.connector.connect(
            host = host_name,
            user = user_name,
            password = user_password,
            database = database_name
        )
        print("Connection is Good!")
    except Error as e:
        print(f"The error '{e}' happened!")

    return connection
# try block initiates the mysql connector with the four variable string 
# then printing statment to see if connection was successful with return connection
# or if error was present with error statement


# Second function was created to excute querys on the database that connection was established on
# with function signature connection and query
def execute_query(connection, query):
    cursor = connection.cursor()
    # establish a cursor that points to database connection
    try:
        cursor.execute(query)
        connection.commit()
        print("Query is Good!")
    except Error as e:
        print(f"The error '{e}' happened!")
# then try block is created to allow cursor to execute and commit data
# with print statement showing if query was succesful
# or an error was present with an error statement


# Third function was created to read query with same function signature
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    # create the cursor again with connection
    # result yet to be processed
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' happened!")
# try block was once again created to execute query in cursor
# result from cursor to be fetched
# result is then returned
# if error is present then print error statement

connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
# created the connection object for the function create_connection to establish connection
# using my specifc information for accessing mysql the values from create_connection function allowed for proper format to represent information
# connection is then made allowing to manage mysql from vs studio continue to manipulate 