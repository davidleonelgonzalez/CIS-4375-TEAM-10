import datetime
from datetime import date
import flask
from flask import jsonify
from flask import request, make_response
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


app = flask.Flask(__name__) # application was set up
app.config["DEBUG"] = True # setup config debug to see errors when calling endpoints

@app.route("/", methods=["GET"]) #default url with no routing with GET request
def home(): # calls function called home
    return "<h1> Welcome to StraWin</h1>"


#region crud

@app.route('/region/all', methods=['GET'])
def api_all_region():
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    cursor = connection.cursor(dictionary=True)
    mysql = "SELECT * FROM region"
    cursor.execute(mysql)
    rows = cursor.fetchall()
    region_results = []
    for region in rows:
        region_results.append(region)

    return jsonify(region_results)



@app.route('/region', methods=['GET'])
def api_region_id():
    if 'region_id' in request.args:
        region_id = int(request.args['region_id']) # making an id variable to save it locally when provided into endpoint
    else:
        return "Error: NO REGION ID IS INPUTTED!"

    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    cursor = connection.cursor(dictionary=True)
    mysql = "SELECT * FROM region"
    cursor.execute(mysql)
    rows = cursor.fetchall()
    region_results = []
    for region in rows:
        if region["region_id"] == region_id:
            region_results.append(region)

    return jsonify(region_results)


@app.route('/addregion', methods=['POST'])
def addregion():
    request_data = request.get_json()
    region_name = request_data['region_name']
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    query = "INSERT INTO region (region_name) VALUES ('"+region_name+"')" 
    execute_query(connection, query)
    return "POST REQUEST IS GOOD!"

#update does not work yet

@app.route('/updateregion', methods=['PUT'])
def updateregion():
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    request_data = request.get_json()
    id_update_region = request_data['region_id']
    new_region_name = request_data["region_name"]
    update_region = """
    UPDATE region 
    SET region_name = %s
    WHERE region_id = %s """ % (new_region_name, id_update_region)
    execute_query(connection, update_region)
    return "PUT REQUEST IS GOOD!"


@app.route('/deleteregion', methods=['DELETE'])
def deleteregion():
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    request_data = request.get_json()
    id_region = request_data['region_id']
    delete_region = "DELETE FROM region WHERE region_id = %s" % (id_region)
    execute_query(connection, delete_region)
    return "DELETE REQUEST IS GOOD!"




#country crud

@app.route('/country/all', methods=['GET'])
def api_all_country():
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    cursor = connection.cursor(dictionary=True)
    mysql = "SELECT * FROM country"
    cursor.execute(mysql)
    rows = cursor.fetchall()
    country_results = []
    for country in rows:
        country_results.append(country)

    return jsonify(country_results)



@app.route('/country', methods=['GET'])
def api_country_id():
    if 'country_id' in request.args:
        country_id = int(request.args['country_id']) # making an id variable to save it locally when provided into endpoint
    else:
        return "Error: NO COUNTRY ID IS INPUTTED!"

    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    cursor = connection.cursor(dictionary=True)
    mysql = "SELECT * FROM country"
    cursor.execute(mysql)
    rows = cursor.fetchall()
    country_results = []
    for country in rows:
        if country["country_id"] == country_id:
            country_results.append(country)

    return jsonify(country_results)


@app.route('/addcountry', methods=['POST'])
def addcountry():
    request_data = request.get_json()
    country_name = request_data['country_name']
    region_id = request_data['region_id']
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    query = "INSERT INTO country (country_name, region_id) VALUES ('"+country_name+"', '"+region_id+"')" 
    execute_query(connection, query)
    return "POST REQUEST IS GOOD!"

#country does not update

@app.route('/updatecountry', methods=['PUT'])
def updatecountry():
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    request_data = request.get_json()
    id_update_country = request_data['country_id']
    new_country_name = request_data["country_name"]
    id_update_region = request_data['region_id']
    update_country = """
    UPDATE country 
    SET country_name = %s, region_id = %s
    WHERE country_id = %s """ % (new_country_name, id_update_region, id_update_country)
    execute_query(connection, update_country)
    return "PUT REQUEST IS GOOD!"


@app.route('/deletecountry', methods=['DELETE'])
def deletecountry():
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    request_data = request.get_json()
    id_country = request_data['country_id']
    delete_country = "DELETE FROM country WHERE country_id = %s" % (id_country)
    execute_query(connection, delete_country)
    return "DELETE REQUEST IS GOOD!"




#vendor crud

@app.route('/vendor/all', methods=['GET'])
def api_all_vendor():
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    cursor = connection.cursor(dictionary=True)
    mysql = "SELECT * FROM vendor"
    cursor.execute(mysql)
    rows = cursor.fetchall()
    vendor_results = []
    for vendor in rows:
        vendor_results.append(vendor)

    return jsonify(vendor_results)



@app.route('/vendor', methods=['GET'])
def api_vendor_id():
    if 'vendor_id' in request.args:
        vendor_id = int(request.args['country_id']) # making an id variable to save it locally when provided into endpoint
    else:
        return "Error: NO VENDOR ID IS INPUTTED!"

    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    cursor = connection.cursor(dictionary=True)
    mysql = "SELECT * FROM vendor"
    cursor.execute(mysql)
    rows = cursor.fetchall()
    vendor_results = []
    for vendor in rows:
        if vendor["vendor_id"] == vendor_id:
            vendor_results.append(vendor)

    return jsonify(vendor_results)


@app.route('/addvendor', methods=['POST'])
def addvendor():
    request_data = request.get_json()
    vendor_name = request_data['vendor_name']
    vendor_phone = request_data['vendor_phone']
    vendor_email = request_data['vendor_email']
    software_type = request_data['software_type']
    hardware_type = request_data['hardware_type']
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    query = "INSERT INTO vendor (vendor_name, vendor_phone, vendor_email, software_type, hardware_type) VALUES ('"+vendor_name+"', '"+vendor_phone+"', '"+vendor_email+"', '"+software_type+"', '"+hardware_type+"')" 
    execute_query(connection, query)
    return "POST REQUEST IS GOOD!"

#vendor does not update

@app.route('/updatevendor', methods=['PUT'])
def updatevendor():
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    request_data = request.get_json()
    id_update_vendor = request_data['vendor_id']
    new_vendor_name = request_data['vendor_name']
    new_vendor_phone = request_data['vendor_phone']
    new_vendor_email = request_data['vendor_email']
    new_software_type = request_data['software_type']
    new_hardware_type = request_data['hardware_type']
    update_vendor = """
    UPDATE vendor 
    SET vendor_name = %s, vendor_phone = %s, vendor_email = %s, software_type = %s, hardware_type = %s
    WHERE vendor_id = %s """ % (new_vendor_name, new_vendor_phone, new_vendor_email,new_software_type,new_hardware_type,id_update_vendor)
    execute_query(connection, update_vendor)
    return "PUT REQUEST IS GOOD!"


@app.route('/deletevendor', methods=['DELETE'])
def deletevendor():
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    request_data = request.get_json()
    id_vendor = request_data['vendor_id']
    delete_vendor = "DELETE FROM vendor WHERE vendor_id = %s" % (id_vendor)
    execute_query(connection, delete_vendor)
    return "DELETE REQUEST IS GOOD!"


#cloud server crud

@app.route('/server/all', methods=['GET'])
def api_all_server():
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    cursor = connection.cursor(dictionary=True)
    mysql = "SELECT * FROM server"
    cursor.execute(mysql)
    rows = cursor.fetchall()
    server_results = []
    for server in rows:
        server_results.append(server)

    return jsonify(server_results)



@app.route('/server', methods=['GET'])
def api_server_id():
    if 'server_id' in request.args:
        server_id = int(request.args['server_id']) # making an id variable to save it locally when provided into endpoint
    else:
        return "Error: NO server ID IS INPUTTED!"

    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    cursor = connection.cursor(dictionary=True)
    mysql = "SELECT * FROM server"
    cursor.execute(mysql)
    rows = cursor.fetchall()
    server_results = []
    for server in rows:
        if server["server_id"] == server_id:
            server_results.append(server)

    return jsonify(server_results)


@app.route('/addserver', methods=['POST'])
def addserver():
    request_data = request.get_json()
    vendor_id = request_data['vendor_id']
    vm_type = request_data['vm_type']
    server_number = request_data['server_number']
    server_location = request_data['software_location']
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    query = "INSERT INTO server (vendor_id, vm_type, server_number, server_location) VALUES ('"+vendor_id+"', '"+vm_type+"', '"+server_number+"', '"+server_location+"', '"+hardware_type+"')" 
    execute_query(connection, query)
    return "POST REQUEST IS GOOD!"

#vendor does not update

@app.route('/updatevendor', methods=['PUT'])
def updatevendor():
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    request_data = request.get_json()
    id_update_server = request_data['server_id']
    new_vm_type = request_data['vm_type']
    new_server_number = request_data['server_number']
    new_server_location = request_data['software_location']
    update_server = """
    UPDATE server 
    SET vm_type = %s, server_number = %s, server_location = %s
    WHERE server_id = %s """ % (new_vm_type, new_server_number, new_server_location,id_update_server)
    execute_query(connection, update_server)
    return "PUT REQUEST IS GOOD!"


@app.route('/deleteserver', methods=['DELETE'])
def deleteserver():
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    request_data = request.get_json()
    id_server = request_data['server_id']
    delete_server = "DELETE FROM server WHERE server_id = %s" % (id_server)
    execute_query(connection, delete_server)
    return "DELETE REQUEST IS GOOD!"




app.run()

