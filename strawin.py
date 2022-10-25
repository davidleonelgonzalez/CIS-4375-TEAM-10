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

#------------------------------------------------------------------------------------------------------------------------------------------------------
#User Login and Password


authorizedusers = [
    {
        #default user
        'username': 'username',
        'password': 'password',
        'role': 'user'
    },
    {
        #admin user
        'username': 'strawin',
        'password': 'LithiumITConsulting4375',
        'role': 'admin'
    }

]



@app.route('/login', methods=['GET'])
def login():
    username = request.headers['username']
    password = request.headers['password']
    for au in authorizedusers:
        if au['username'] == username and au['password'] == password:
            return 'Authorized with priviledge of: ' + au['role']
    return 'YOU ARE NOT AUTHORIZED'




#----------------------------------------------------------------------------------------------------------------------------------------------------------------
#1
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


#does not work says object is not subscriptable
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

#-------------------------------------------------------------------------------------------------------------------------------------------------



#-------------------------------------------------------------------------------------------------------------------------------------------------
#2
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

#-----------------------------------------------------------------------------------------------------------------------------------------



#-----------------------------------------------------------------------------------------------------------------------------------------
#3
#state crud

@app.route('/state/all', methods=['GET'])
def api_all_state():
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    cursor = connection.cursor(dictionary=True)
    mysql = "SELECT * FROM state_providence"
    cursor.execute(mysql)
    rows = cursor.fetchall()
    state_results = []
    for state in rows:
        state_results.append(state)

    return jsonify(state_results)



@app.route('/state', methods=['GET'])
def api_state_id():
    if 'state_id' in request.args:
        state_id = int(request.args['state_id']) # making an id variable to save it locally when provided into endpoint
    else:
        return "Error: NO STATE ID IS INPUTTED!"

    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    cursor = connection.cursor(dictionary=True)
    mysql = "SELECT * FROM state_providence"
    cursor.execute(mysql)
    rows = cursor.fetchall()
    state_results = []
    for state in rows:
        if state["state_id"] == state_id:
            state_results.append(state)

    return jsonify(state_results)


@app.route('/addstate', methods=['POST'])
def addstate():
    request_data = request.get_json()
    state_providence_name = request_data['state_providence_name']
    country_id = request_data['country_id']
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    query = "INSERT INTO state_providence (state_providence_name, country_id) VALUES ('"+state_providence_name+"', '"+country_id+"')" 
    execute_query(connection, query)
    return "POST REQUEST IS GOOD!"


@app.route('/updatestate', methods=['PUT'])
def updatestate():
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    request_data = request.get_json()
    id_update_state = request_data['state_id']
    new_state_providence_name = request_data["state_providence_name"]
    id_update_country = request_data['country_id']
    update_state = """
    UPDATE state_providence 
    SET state_providence_name = %s, country_id = %s
    WHERE state_id = %s """ % (new_state_providence_name, id_update_country, id_update_state)
    execute_query(connection, update_state)
    return "PUT REQUEST IS GOOD!"


@app.route('/deletestate', methods=['DELETE'])
def deletestate():
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    request_data = request.get_json()
    id_state = request_data['state_id']
    delete_state = "DELETE FROM state_providence WHERE state_id = %s" % (id_state)
    execute_query(connection, delete_state)
    return "DELETE REQUEST IS GOOD!"

#-----------------------------------------------------------------------------------------------------------------------------------------



#------------------------------------------------------------------------------------------------------------------------------------------
#4
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
        vendor_id = int(request.args['vendor_id']) # making an id variable to save it locally when provided into endpoint
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

#------------------------------------------------------------------------------------------------------------------------------------------------------



#------------------------------------------------------------------------------------------------------------------------------------------------------
#5
#cloud server crud 

@app.route('/server/all', methods=['GET'])
def api_all_server():
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    cursor = connection.cursor(dictionary=True)
    mysql = "SELECT * FROM cloud_server"
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
        return "Error: NO SERVER ID IS INPUTTED!"

    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    cursor = connection.cursor(dictionary=True)
    mysql = "SELECT * FROM cloud_server"
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
    vm_type = request_data['vm_type']
    server_number = request_data['server_number']
    server_location = request_data['server_location']
    vendor_id = request_data['vendor_id']
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    query = "INSERT INTO cloud_server (vm_type, server_number, server_location, vendor_id) VALUES ('"+vm_type+"', '"+server_number+"', '"+server_location+"', '"+vendor_id+"')" 
    execute_query(connection, query)
    return "POST REQUEST IS GOOD!"



@app.route('/updateserver', methods=['PUT'])
def updateserver():
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    request_data = request.get_json()
    id_update_server = request_data['server_id']
    new_vm_type = request_data['vm_type']
    new_server_number = request_data['server_number']
    new_server_location = request_data['software_location']
    new_vendor_id = request_data['vendor_id']
    update_server = """
    UPDATE cloud_server 
    SET vm_type = %s, server_number = %s, server_location = %s
    WHERE server_id = %s """ % (new_vm_type, new_server_number, new_server_location,id_update_server)
    execute_query(connection, update_server)
    return "PUT REQUEST IS GOOD!"


@app.route('/deleteserver', methods=['DELETE'])
def deleteserver():
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    request_data = request.get_json()
    id_server = request_data['server_id']
    delete_server = "DELETE FROM cloud_server WHERE server_id = %s" % (id_server)
    execute_query(connection, delete_server)
    return "DELETE REQUEST IS GOOD!"

#----------------------------------------------------------------------------------------------------------------------------------------------------



#-----------------------------------------------------------------------------------------------------------------------------------------------------
#6
#product crud

@app.route('/product/all', methods=['GET'])
def api_all_product():
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    cursor = connection.cursor(dictionary=True)
    mysql = "SELECT * FROM product"
    cursor.execute(mysql)
    rows = cursor.fetchall()
    product_results = []
    for product in rows:
        product_results.append(product)

    return jsonify(product_results)



@app.route('/product', methods=['GET'])
def api_product_id():
    if 'product_id' in request.args:
        product_id = int(request.args['product_id']) # making an id variable to save it locally when provided into endpoint
    else:
        return "Error: NO PRODUCT ID IS INPUTTED!"

    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    cursor = connection.cursor(dictionary=True)
    mysql = "SELECT * FROM product"
    cursor.execute(mysql)
    rows = cursor.fetchall()
    product_results = []
    for product in rows:
        if product["product_id"] == product_id:
            product_results.append(product)

    return jsonify(product_results)


@app.route('/addproduct', methods=['POST'])
def addproduct():
    request_data = request.get_json()
    product_sku = request_data['product_sku']
    product_name = request_data['product_name']
    product_description = request_data['product_description']
    category = request_data['category']
    server_id = request_data['server_id']
    client_id = request_data['client_id']
    prospect_id = request_data['prospect_id']
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    query = "INSERT INTO product (product_sku, product_name, product_description, category, server_id, client_id, prospect_id) VALUES ('"+product_sku+"', '"+product_name+"', '"+product_description+"', '"+category+"', '"+server_id+"', '"+client_id+"', '"+prospect_id+"')" 
    execute_query(connection, query)
    return "POST REQUEST IS GOOD!"



@app.route('/updateproduct', methods=['PUT'])
def updateproduct():
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    request_data = request.get_json()
    id_update_product = request_data['product_id']
    new_product_sku = request_data['product_sku']
    new_product_name = request_data['product_name']
    new_product_description = request_data['product_description']
    new_category = request_data['category']
    new_server_id = request_data['server_id']
    new_client_id = request_data['client_id']
    new_prospect_id = request_data['prospect_id']
    update_product = """
    UPDATE product 
    SET product_sku = %s, product_name = %s, product_description = %s, category = %s, server_id = %s, client_id = %s, prospect_id = %s
    WHERE product_id = %s """ % (new_product_sku, new_product_name, new_product_description, new_category, new_server_id, new_client_id, new_prospect_id, id_update_product)
    execute_query(connection, update_product)
    return "PUT REQUEST IS GOOD!"


@app.route('/deleteproduct', methods=['DELETE'])
def deleteproduct():
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    request_data = request.get_json()
    id_product = request_data['product_id']
    delete_product = "DELETE FROM product WHERE product_id = %s" % (id_product)
    execute_query(connection, delete_product)
    return "DELETE REQUEST IS GOOD!"
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------------------------------------------------------------------------
#7
#department crud

@app.route('/department/all', methods=['GET'])
def api_all_department():
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    cursor = connection.cursor(dictionary=True)
    mysql = "SELECT * FROM department"
    cursor.execute(mysql)
    rows = cursor.fetchall()
    department_results = []
    for department in rows:
        department_results.append(department)

    return jsonify(department_results)



@app.route('/department', methods=['GET'])
def api_department_id():
    if 'department_id' in request.args:
        department_id = int(request.args['department_id']) # making an id variable to save it locally when provided into endpoint
    else:
        return "Error: NO DEPARTMENT ID IS INPUTTED!"

    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    cursor = connection.cursor(dictionary=True)
    mysql = "SELECT * FROM department"
    cursor.execute(mysql)
    rows = cursor.fetchall()
    department_results = []
    for department in rows:
        if department["department_id"] == department_id:
            department_results.append(department)

    return jsonify(department_results)


@app.route('/adddepartment', methods=['POST'])
def adddepartment():
    request_data = request.get_json()
    department_name = request_data['department_name']
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    query = "INSERT INTO department (department_name) VALUES ('"+department_name+"')" 
    execute_query(connection, query)
    return "POST REQUEST IS GOOD!"



@app.route('/updatedepartment', methods=['PUT'])
def updatedepartment():
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    request_data = request.get_json()
    id_update_department = request_data['department_id']
    new_department_name = request_data['department_name']
    update_department = """
    UPDATE department 
    SET department_name = %s
    WHERE department_id = %s """ % (new_department_name, id_update_department)
    execute_query(connection, update_department)
    return "PUT REQUEST IS GOOD!"


@app.route('/deletedepartment', methods=['DELETE'])
def deletedepartment():
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    request_data = request.get_json()
    id_department = request_data['department_id']
    delete_department = "DELETE FROM department WHERE department_id = %s" % (id_department)
    execute_query(connection, delete_department)
    return "DELETE REQUEST IS GOOD!"

#----------------------------------------------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------------------------------------------

#8
#employee status crud

@app.route('/employee_status/all', methods=['GET'])
def api_all_employee_status():
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    cursor = connection.cursor(dictionary=True)
    mysql = "SELECT * FROM employee_status"
    cursor.execute(mysql)
    rows = cursor.fetchall()
    employee_status_results = []
    for employee_status in rows:
        employee_status_results.append(employee_status)

    return jsonify(employee_status_results)



@app.route('/employee_status', methods=['GET'])
def api_employee_status_id():
    if 'employee_status_id' in request.args:
        employee_status_id = int(request.args['employee_status_id']) # making an id variable to save it locally when provided into endpoint
    else:
        return "Error: NO EMPLOYEE STATUS ID IS INPUTTED!"

    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    cursor = connection.cursor(dictionary=True)
    mysql = "SELECT * FROM employee_status"
    cursor.execute(mysql)
    rows = cursor.fetchall()
    employee_status_results = []
    for employee_status in rows:
        if employee_status["employee_status_id"] == employee_status_id:
            employee_status_results.append(employee_status)

    return jsonify(employee_status_results)


@app.route('/addemployee_status', methods=['POST'])
def addemployee_status():
    request_data = request.get_json()
    status_name = request_data['status_name']
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    query = "INSERT INTO employee_status (status_name) VALUES ('"+status_name+"')" 
    execute_query(connection, query)
    return "POST REQUEST IS GOOD!"



@app.route('/updateemployee_status', methods=['PUT'])
def updateemployee_status():
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    request_data = request.get_json()
    id_update_employee_status = request_data['employee_status_id']
    new_status_name = request_data['status_name']
    update_employee_status = """
    UPDATE employee_status 
    SET status_name = %s
    WHERE employee_status_id = %s """ % (new_status_name, id_update_employee_status)
    execute_query(connection, update_employee_status)
    return "PUT REQUEST IS GOOD!"


@app.route('/deleteemployee_status', methods=['DELETE'])
def deleteemployee_status():
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    request_data = request.get_json()
    id_employee_status = request_data['employee_status_id']
    delete_employee_status = "DELETE FROM employee_status WHERE employee_status_id = %s" % (id_employee_status)
    execute_query(connection, delete_employee_status)
    return "DELETE REQUEST IS GOOD!"

#----------------------------------------------------------------------------------------------------------------------------------------



#-----------------------------------------------------------------------------------------------------------------------------------------
#9
#client status crud


@app.route('/client_status/all', methods=['GET'])
def api_all_client_status():
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    cursor = connection.cursor(dictionary=True)
    mysql = "SELECT * FROM client_status"
    cursor.execute(mysql)
    rows = cursor.fetchall()
    client_status_results = []
    for client_status in rows:
        client_status_results.append(client_status)

    return jsonify(client_status_results)



@app.route('/client_status', methods=['GET'])
def api_client_status_id():
    if 'client_status_id' in request.args:
        client_status_id = int(request.args['client_status_id']) # making an id variable to save it locally when provided into endpoint
    else:
        return "Error: NO CLIENT STATUS ID IS INPUTTED!"

    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    cursor = connection.cursor(dictionary=True)
    mysql = "SELECT * FROM client_status"
    cursor.execute(mysql)
    rows = cursor.fetchall()
    client_status_results = []
    for client_status in rows:
        if client_status["client_status_id"] == client_status_id:
            client_status_results.append(client_status)

    return jsonify(client_status_results)


@app.route('/addclient_status', methods=['POST'])
def addclient_status():
    request_data = request.get_json()
    status_name = request_data['status_name']
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    query = "INSERT INTO client_status (status_name) VALUES ('"+status_name+"')" 
    execute_query(connection, query)
    return "POST REQUEST IS GOOD!"



@app.route('/updateclient_status', methods=['PUT'])
def updateclient_status():
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    request_data = request.get_json()
    id_update_client_status = request_data['client_status_id']
    new_status_name = request_data['status_name']
    update_client_status = """
    UPDATE client_status 
    SET status_name = %s
    WHERE client_status_id = %s """ % (new_status_name, id_update_client_status)
    execute_query(connection, update_client_status)
    return "PUT REQUEST IS GOOD!"


@app.route('/deleteclient_status', methods=['DELETE'])
def deleteclient_status():
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    request_data = request.get_json()
    id_client_status = request_data['client_status_id']
    delete_client_status = "DELETE FROM client_status WHERE client_status_id = %s" % (id_client_status)
    execute_query(connection, delete_client_status)
    return "DELETE REQUEST IS GOOD!"

#--------------------------------------------------------------------------------------------------------------------------------------------



#---------------------------------------------------------------------------------------------------------------------------------------------
#10
#sales crud


@app.route('/sales/all', methods=['GET'])
def api_all_sales():
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    cursor = connection.cursor(dictionary=True)
    mysql = "SELECT * FROM sales"
    cursor.execute(mysql)
    rows = cursor.fetchall()
    sales_results = []
    for sales in rows:
        sales_results.append(sales)

    return jsonify(sales_results)



@app.route('/sales', methods=['GET'])
def api_sales_id():
    if 'sales_id' in request.args:
        sales_id = int(request.args['sales_id']) # making an id variable to save it locally when provided into endpoint
    else:
        return "Error: NO SALES ID IS INPUTTED!"

    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    cursor = connection.cursor(dictionary=True)
    mysql = "SELECT * FROM sales"
    cursor.execute(mysql)
    rows = cursor.fetchall()
    sales_results = []
    for sales in rows:
        if sales["sales_id"] == sales_id:
            sales_results.append(sales)

    return jsonify(sales_results)


@app.route('/addsales', methods=['POST'])
def addsales():
    request_data = request.get_json()
    employee_id = request_data['employee_id']
    prospect_id = request_data['prospect_id']
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    query = "INSERT INTO sales (employee_id, prospect_id) VALUES ('"+employee_id+"', '"+prospect_id+"')" 
    execute_query(connection, query)
    return "POST REQUEST IS GOOD!"



@app.route('/updatesales', methods=['PUT'])
def updatesales():
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    request_data = request.get_json()
    id_update_sales = request_data['sales_id']
    new_employee_id = request_data['employee_id']
    new_prospect_id = request_data['prospect_id']
    update_sales = """
    UPDATE sales 
    SET employee_id = %s, prospect_id = %s
    WHERE sales_id = %s """ % (new_employee_id, new_prospect_id, id_update_sales)
    execute_query(connection, update_sales)
    return "PUT REQUEST IS GOOD!"


@app.route('/deletesales', methods=['DELETE'])
def deletesales():
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    request_data = request.get_json()
    id_sales = request_data['sales_id']
    delete_sales = "DELETE FROM sales WHERE sales_id = %s" % (id_sales)
    execute_query(connection, delete_sales)
    return "DELETE REQUEST IS GOOD!"

#----------------------------------------------------------------------------------------------------------------------------------------------



#-----------------------------------------------------------------------------------------------------------------------------------------------
#11
#airline prospect crud


@app.route('/prospect/all', methods=['GET'])
def api_all_prospect():
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    cursor = connection.cursor(dictionary=True)
    mysql = "SELECT * FROM airline_prospect"
    cursor.execute(mysql)
    rows = cursor.fetchall()
    prospect_results = []
    for prospect in rows:
        prospect_results.append(prospect)

    return jsonify(prospect_results)



@app.route('/prospect', methods=['GET'])
def api_prospect_id():
    if 'prospect_id' in request.args:
        prospect_id = int(request.args['prospect_id']) # making an id variable to save it locally when provided into endpoint
    else:
        return "Error: NO PROSPECT ID IS INPUTTED!"

    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    cursor = connection.cursor(dictionary=True)
    mysql = "SELECT * FROM airline_prospect"
    cursor.execute(mysql)
    rows = cursor.fetchall()
    prospect_results = []
    for prospect in rows:
        if prospect["prospect_id"] == prospect_id:
            prospect_results.append(prospect)

    return jsonify(prospect_results)


@app.route('/addprospect', methods=['POST'])
def addprospect():
    request_data = request.get_json()
    airline_name = request_data['airline_name']
    address = request_data['address']
    zip_code = request_data['zip_code']
    state_id = request_data['state_id']
    country_id = request_data['country_id']
    region_id = request_data['region_id']
    client_status_id = request_data['client_status_id']
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    query = "INSERT INTO airline_prospect (airline_name, address, zip_code, state_id, country_id, region_id, client_status_id ) VALUES ('"+airline_name+"','"+address+"', '"+zip_code+"','"+state_id+"', '"+country_id+"', '"+region_id+"','"+client_status_id+"')" 
    execute_query(connection, query)
    return "POST REQUEST IS GOOD!"



@app.route('/updatprospect', methods=['PUT'])
def updateprospect():
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    request_data = request.get_json()
    id_update_prospect = request_data['prospect_id']
    new_airline_name = request_data['airline_name']
    new_address = request_data['address']
    new_zip_code = request_data['zip_code']
    new_state_id = request_data['state_id']
    new_country_id = request_data['country_id']
    new_region_id = request_data['region_id']
    new_client_status_id = request_data['client_status_id']
    update_prospect = """
    UPDATE airline_prospect 
    SET airline_name = %s, address = %s, zip_code = %s, state_id = %s, country_id = %s, region_id = %s, client_status_id = %s
    WHERE prospect_id = %s """ % (new_airline_name, new_address, new_zip_code, new_state_id, new_country_id, new_region_id, new_client_status_id, id_update_prospect)
    execute_query(connection, update_prospect)
    return "PUT REQUEST IS GOOD!"


@app.route('/deleteprospect', methods=['DELETE'])
def deleteprospect():
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    request_data = request.get_json()
    id_prospect = request_data['prospect_id']
    delete_prospect = "DELETE FROM airline_prospect WHERE prospect_id = %s" % (id_prospect)
    execute_query(connection, delete_prospect)
    return "DELETE REQUEST IS GOOD!"

#-------------------------------------------------------------------------------------------------------------------------------------------------



#-------------------------------------------------------------------------------------------------------------------------------------------------
#12
#airline client crud

@app.route('/client/all', methods=['GET'])
def api_all_client():
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    cursor = connection.cursor(dictionary=True)
    mysql = "SELECT * FROM airline_client"
    cursor.execute(mysql)
    rows = cursor.fetchall()
    client_results = []
    for client in rows:
        client_results.append(client)

    return jsonify(client_results)



@app.route('/client', methods=['GET'])
def api_client_id():
    if 'client_id' in request.args:
        client_id = int(request.args['client_id']) # making an id variable to save it locally when provided into endpoint
    else:
        return "Error: NO AIRLINE CLIENT ID IS INPUTTED!"

    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    cursor = connection.cursor(dictionary=True)
    mysql = "SELECT * FROM airline_client"
    cursor.execute(mysql)
    rows = cursor.fetchall()
    client_results = []
    for client in rows:
        if client["client_id"] == client_id:
            client_results.append(client)

    return jsonify(client_results)


@app.route('/addclient', methods=['POST'])
def addclient():
    request_data = request.get_json()
    airline_name = request_data['airline_name']
    address = request_data['address']
    zip_code = request_data['zip_code']
    state_id = request_data['state_id']
    country_id = request_data['country_id']
    region_id = request_data['region_id']
    client_status_id = request_data['client_status_id']
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    query = "INSERT INTO airline_client (airline_name, address, zip_code, state_id, country_id, region_id, client_status_id ) VALUES ('"+airline_name+"','"+address+"', '"+zip_code+"','"+state_id+"', '"+country_id+"', '"+region_id+"','"+client_status_id+"')" 
    execute_query(connection, query)
    return "POST REQUEST IS GOOD!"



@app.route('/updatclient', methods=['PUT'])
def updateclient():
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    request_data = request.get_json()
    id_update_client = request_data['client_id']
    new_airline_name = request_data['airline_name']
    new_address = request_data['address']
    new_zip_code = request_data['zip_code']
    new_state_id = request_data['state_id']
    new_country_id = request_data['country_id']
    new_region_id = request_data['region_id']
    new_client_status_id = request_data['client_status_id']
    update_client = """
    UPDATE airline_client 
    SET airline_name = %s, address = %s, zip_code = %s, state_id = %s, country_id = %s, region_id = %s, client_status_id = %s
    WHERE client_id = %s """ % (new_airline_name, new_address, new_zip_code, new_state_id, new_country_id, new_region_id, new_client_status_id, id_update_client)
    execute_query(connection, update_client)
    return "PUT REQUEST IS GOOD!"


@app.route('/deleteclient', methods=['DELETE'])
def deleteclient():
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    request_data = request.get_json()
    id_client = request_data['client_id']
    delete_client = "DELETE FROM airline_client WHERE client_id = %s" % (id_client)
    execute_query(connection, delete_client)
    return "DELETE REQUEST IS GOOD!"


#---------------------------------------------------------------------------------------------------------------------------------------------



#----------------------------------------------------------------------------------------------------------------------------------------------
#13
#airline client employee crud


@app.route('/client_employee/all', methods=['GET'])
def api_all_client_employee():
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    cursor = connection.cursor(dictionary=True)
    mysql = "SELECT * FROM client_employee"
    cursor.execute(mysql)
    rows = cursor.fetchall()
    client_employee_results = []
    for client_employee in rows:
        client_employee_results.append(client_employee)

    return jsonify(client_employee_results)



@app.route('/client_employee', methods=['GET'])
def api_client_employee_id():
    if 'client_employee_id' in request.args:
        client_employee_id = int(request.args['client_employee_id']) # making an id variable to save it locally when provided into endpoint
    else:
        return "Error: NO CLIENT EMPLOYEE ID IS INPUTTED!"

    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    cursor = connection.cursor(dictionary=True)
    mysql = "SELECT * FROM client_employee"
    cursor.execute(mysql)
    rows = cursor.fetchall()
    client_employee_results = []
    for client_employee in rows:
        if client_employee["client_employee_id"] == client_employee_id:
            client_employee_results.append(client_employee)

    return jsonify(client_employee_results)


@app.route('/addclient_employee', methods=['POST'])
def addclient_employee():
    request_data = request.get_json()
    client_id = request_data['client_id']
    employee_id = request_data['employee_id']
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    query = "INSERT INTO client_employee (client_id, employee_id) VALUES ('"+client_id+"', '"+employee_id+"')" 
    execute_query(connection, query)
    return "POST REQUEST IS GOOD!"



@app.route('/updatclient_employee', methods=['PUT'])
def updateclient_employee():
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    request_data = request.get_json()
    new_client_id = request_data['client_id']
    new_employee_id = request_data['employee_id']
    update_client_employee = """
    UPDATE client_employee 
    SET client_id = %s, employee_id = %s
    WHERE client_id = %s AND employee_id = %s """ % (new_client_id, new_employee_id)
    execute_query(connection, update_client_employee)
    return "PUT REQUEST IS GOOD!"


@app.route('/deleteclient_employee', methods=['DELETE'])
def deleteclient_employee():
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    request_data = request.get_json()
    id_client = request_data['client_id']
    id_employee = request_data['employee_id']
    delete_client_employee = "DELETE FROM client_employee WHERE client_id = %s AND employee_id = %s"  % (id_client, id_employee)
    execute_query(connection, delete_client_employee)
    return "DELETE REQUEST IS GOOD!"

#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------



#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#14
#employee crud


@app.route('/employee/all', methods=['GET'])
def api_all_employee():
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    cursor = connection.cursor(dictionary=True)
    mysql = "SELECT * FROM employee"
    cursor.execute(mysql)
    rows = cursor.fetchall()
    employee_results = []
    for employee in rows:
        employee_results.append(employee)

    return jsonify(employee_results)



@app.route('/employee', methods=['GET'])
def api_employee_id():
    if 'employee_id' in request.args:
        employee_id = int(request.args['employee_id']) # making an id variable to save it locally when provided into endpoint
    else:
        return "Error: NO EMPLOYEE ID IS INPUTTED!"

    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    cursor = connection.cursor(dictionary=True)
    mysql = "SELECT * FROM employee"
    cursor.execute(mysql)
    rows = cursor.fetchall()
    employee_results = []
    for employee in rows:
        if employee["employee_id"] == employee_id:
            employee_results.append(employee)

    return jsonify(employee_results)


@app.route('/addemployee', methods=['POST'])
def addemployee():
    request_data = request.get_json()
    first_name = request_data['first_name']
    last_name = request_data['last_name']
    phone_number = request_data['phone_number']
    email = request_data['email']
    address = request_data['address']
    zip_code = request_data['zip_code']
    state_id = request_data['state_id']
    country_id = request_data['country_id']
    region_id = request_data['region_id']
    department_id = request_data['department_id']
    employee_status_id = request_data['employee_status_id']
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    query = "INSERT INTO employee (first_name, last_name, phone_number, email, address, zip_code, state_id, country_id, region_id, department_id, employee_status_id) VALUES ('"+first_name+"', '"+last_name+"', '"+phone_number+"', '"+email+"', '"+address+"', '"+zip_code+"', '"+state_id+"', '"+country_id+"', '"+region_id+"', '"+department_id+"', '"+employee_status_id+"' )" 
    execute_query(connection, query)
    return "POST REQUEST IS GOOD!"



@app.route('/updatemployee', methods=['PUT'])
def updateemployee():
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    request_data = request.get_json()
    id_update_employee = request_data['employee_id']
    new_first_name = request_data['first_name']
    new_last_name = request_data['last_name']
    new_phone_number = request_data['phone_number']
    new_email = request_data['email']
    new_address = request_data['address']
    new_zip_code = request_data['zip_code']
    new_state_id = request_data['state_id']
    new_country_id = request_data['country_id']
    new_region_id = request_data['region_id']
    new_department_id = request_data['department_id']
    new_employee_status_id = request_data['employee_status_id']
    update_employee = """
    UPDATE employee 
    SET first_name = %s, last_name = %s, phone_number = %s, email = %s, address = %s, zip_code = %s, state_id = %s, country_id = %s, region_id = %s, department_id = %s, employee_status_id = %s
    WHERE client_employee_id = %s """ % (new_first_name, new_last_name, new_phone_number, new_email, new_address, new_zip_code, new_state_id, new_country_id, new_region_id, new_department_id, new_employee_status_id, id_update_employee)
    execute_query(connection, update_employee)
    return "PUT REQUEST IS GOOD!"


@app.route('/deleteemployee', methods=['DELETE'])
def deleteemployee():
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    request_data = request.get_json()
    id_employee = request_data['employee_id']
    delete_employee = "DELETE FROM employee WHERE employee_id = %s" % (id_employee)
    execute_query(connection, delete_employee)
    return "DELETE REQUEST IS GOOD!"


#---------------------------------------------------------------------------------------------------------------------------------------------

app.run()

