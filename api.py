import mysql.connector
import flask
from flask import request, jsonify
import json

#mySQL connection
config = {
  'user': 'adriana',
  'password': 'abc123',
  'host': '127.0.0.1',
  'database': 'programming_assignment_db',
  'raise_on_warnings': True
}

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# default info page
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Frequent Commenters API</h1>'''


#return details for each user(poster) using id 
#http://127.0.0.1:5000/api/v1/posters?id=21
@app.route('/api/v1/posters', methods=['GET'])
def api_userid():

    # change configuration not to sort keyes in alphabetically
    app.config['JSON_SORT_KEYS'] = False

    cnx = mysql.connector.connect(**config)

    # set to False if no parameters are provided
    params = True
    #based on username or id passed as parameter build SQL
    if 'id' in request.args:
       id = int(request.args['id'])
       sql = "SELECT poster_id, poster_username, poster_lat, poster_lng, commenter_id, commenter_username, commenter_lat, commenter_lng, nr_of_times_commented FROM v_users_commenters WHERE poster_id = " + str(id)
    elif 'username' in request.args:
       username = str(request.args['username'])
       sql = "SELECT poster_id, poster_username, poster_lat, poster_lng, commenter_id, commenter_username, commenter_lat, commenter_lng, nr_of_times_commented FROM v_users_commenters WHERE poster_username = '" + username + "'"
    else:
       params = False
        
    # check that userid was provided and if not return error
    if params:
        #id = int(request.args['id'])  # TODO add logic to allow searching by username
        # pull records from database
        mycursor = cnx.cursor()
        mycursor.execute(sql)
        results = mycursor.fetchall()
          
        content = {}
        payload = []
        no_results = False
        for result in results: 
           no_results = True
           freq_comm = {"commenter_id": result[4], "commenter_username": result[5], "commenter_distance_lat": result[6], "commenter_distance_lon": result[7], "times_commented_on_user": result[8]}
           # build frequent commenters section e.g. {"commenter_id": 1, "commenter_username": "user1"},
           person_dict = {"user_id": result[0], "username": result[1], "user_address_lat": result[2], "user_address_lon": result[3],
           "frequent_commenters": [
           # build frequent_commenters section  
           # need to repeat commenter details for each commenter - TODO
           #{"commenter_id": result[4], "commenter_username": result[5], "commenter_distance_lat": result[6], "commenter_distance_lon": result[7], "times_commented_on_user": result[8]}
           freq_comm         
           ],
           }

        if no_results == True:
            payload.append(person_dict)
            return jsonify(payload)
        else:
            return "Poster doesn't have frequent commenters yet..."
    else:
        return "Error: No userid field provided. Please specify an userid."
   
app.run()