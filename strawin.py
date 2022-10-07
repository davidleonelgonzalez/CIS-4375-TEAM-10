import dbconnector
import flask
from flask import jsonify
from flask import request, make_response
import mysql.connector
from mysql.connector import Error



#First thing needed to do was to set a name for application

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
    region_id_update = request_data['region_id']
    new_region_name = request_data['region_name']
    update_region = """
    UPDATE region 
    SET region_name = %s
    WHERE region_id = %s """ % (new_region_name, region_id_update)
    execute_query(connection, update_region)
    return "PUT REQUEST IS GOOD!"

#delete works

@app.route('/deleteregion', methods=['DELETE'])
def deleteregion():
    connection = create_connection("cis4375.cgatajvkx1pb.us-east-1.rds.amazonaws.com", "team10", "Strawin_cis4375!", "cis4375db")
    request_data = request.get_json()
    id_region = request_data['region_id']
    delete_region = "DELETE FROM region WHERE region_id = %s" % (id_region)
    execute_query(connection, delete_region)
    return "DELETE REQUEST IS GOOD!"



def create_connection(host_name, user_name, user_password, database_name):
    connection = None
    
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

def execute_query(connection, query):
    cursor = connection.cursor()

    try:
        cursor.execute(query)
        connection.commit()
        print("Query is Good!")
    except Error as e:
        print(f"The error '{e}' happened!")


app.run()

