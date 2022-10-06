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

create_region_table = """
CREATE TABLE IF NOT EXISTS region (
    region_id INT AUTO_INCREMENT PRIMARY KEY,
    region_name VARCHAR(50) NOT NULL
)"""

execute_query(connection, create_region_table)


create_country_table = """
CREATE TABLE IF NOT EXISTS country (
    country_id INT AUTO_INCREMENT PRIMARY KEY,
    country_name VARCHAR(50) NOT NULL,
    region_id INT,
    FOREIGN KEY (region_id) REFERENCES region(region_id)
)"""

execute_query(connection, create_country_table)

create_employee_status_table = """
CREATE TABLE IF NOT EXISTS employee_status (
    employee_status_id INT AUTO_INCREMENT PRIMARY KEY,
    status_name VARCHAR(100) NOT NULL
)"""

execute_query(connection, create_employee_status_table)

create_client_status_table = """
CREATE TABLE IF NOT EXISTS client_status (
    client_status_id INT AUTO_INCREMENT PRIMARY KEY,
    status_name VARCHAR(100) NOT NULL
)"""

execute_query(connection, create_client_status_table)

create_department_table = """
CREATE TABLE IF NOT EXISTS department (
    department_id INT AUTO_INCREMENT PRIMARY KEY,
    department_name VARCHAR(100) NOT NULL
)"""

execute_query(connection, create_department_table)


create_employee_table = """
CREATE TABLE IF NOT EXISTS employee (
    employee_id INT AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    phone_number VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES department(department_id),
    employee_status_id INT,
    FOREIGN KEY (employee_status_id) REFERENCES employee_status(employee_status_id),
    region_id INT,
    FOREIGN KEY (region_id) REFERENCES region(region_id)

)"""

execute_query(connection, create_employee_table)

create_airline_client_table = """
CREATE TABLE IF NOT EXISTS airline_client (
    client_id INT AUTO_INCREMENT PRIMARY KEY,
    airline_name VARCHAR(100) NOT NULL,
    phone_number VARCHAR(100) NOT NULL,
    client_status_id INT,
    FOREIGN KEY (client_status_id) REFERENCES client_status(client_status_id),
    country_id INT,
    FOREIGN KEY (country_id) REFERENCES country(country_id)

)"""

execute_query(connection, create_airline_client_table)
#messed up should have put phone number as 'INT'
create_airline_prospect_table = """
CREATE TABLE IF NOT EXISTS airline_prospect (
    prospect_id INT AUTO_INCREMENT PRIMARY KEY,
    airline_name VARCHAR(100) NOT NULL,
    phone_number VARCHAR(100) NOT NULL,
    client_status_id INT,
    FOREIGN KEY (client_status_id) REFERENCES client_status(client_status_id),
    country_id INT,
    FOREIGN KEY (country_id) REFERENCES country(country_id)

)"""

execute_query(connection, create_airline_prospect_table)

create_product_table = """
CREATE TABLE IF NOT EXISTS product (
    product_id INT AUTO_INCREMENT PRIMARY KEY,
    product_sku VARCHAR(100) NOT NULL,
    product_name VARCHAR(100) NOT NULL,
    product_description VARCHAR(100) NOT NULL,
    category VARCHAR(100) NOT NULL,
    client_id INT,
    FOREIGN KEY (client_id) REFERENCES airline_client(client_id),
    prospect_id INT,
    FOREIGN KEY (prospect_id) REFERENCES airline_prospect(prospect_id)

)"""

execute_query(connection, create_product_table)

