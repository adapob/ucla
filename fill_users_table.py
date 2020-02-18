import requests
import mysql.connector
import json

#api 
url = "https://jsonplaceholder.typicode.com/users"
headers = {
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Host': "jsonplaceholder.typicode.com",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

#mySQL connection
config = {
  'user': 'adriana',
  'password': 'abc123',
  'host': '127.0.0.1',
  'database': 'programming_assignment_db',
  'raise_on_warnings': True
}

# get users data from Json to update users table
# match user by email and update username, latitude, longitude
response = requests.request("GET", url, headers=headers)

cnx = mysql.connector.connect(**config)
mycursor = cnx.cursor()

# check that call was successful before extracting data from Json
# then update username, latitude, longitude for each user (match by email)
if response.status_code == 200:
#load json into object
    data = json.loads(response.text)
    for x in data:
        #print("Updating user: " + x['name'] + " - " + x['username'])
        sql = "UPDATE users SET username = %s, address__geo__lat = %s, address__geo__lng = %s WHERE email = %s"
        val = (x['username'], x['address']['geo']['lat'], x['address']['geo']['lng'], x['email'])
        mycursor.execute(sql, val)
        
        #user record has been updated, now update posts table for the same user since userid (from json) matches userid in posts
        #for e.g. "userId": 1 is id 21 in users table, but user 1 in posts table
        #there are two ways that this can be done, one call retriving all posts then finding posts for that specific user (https://jsonplaceholder.typicode.com/posts)
        #or calling api to get posts for specific user id (https://jsonplaceholder.typicode.com/posts?userId=1  (pass x['id']))
        
        #build list of posts id to be updated, for e.g. 1, 2, 6,
        #extract json-post:id and build where clause
        #update posts table set userid = (select id from users where email = x['email']) where id in (1,2,6)
        
        #get post ids from posts call
        url_posts = "https://jsonplaceholder.typicode.com/posts?userId=" + str(x['id'])
        response_posts = requests.request("GET", url_posts, headers=headers)
        data_posts = json.loads(response_posts.text)
        
        #build where in clause to include post ids.
        sql_posts = "UPDATE posts, (SELECT users.id FROM users WHERE email = '" + x['email'] + "') AS users"
        posts_id =  " SET userid = users.id WHERE posts.id in ( "
        for y in data_posts:
            posts_id += str(y['id']) + ","
            #print("Post for user: " + str(y['userId']) + '| post id: ' + str(y['id']) + '| post title: ' + y['title'])
        posts_id = (posts_id[:-1]) + ")"
        print("SQL " + sql_posts + " " + posts_id + "\n")
        #update posts for each user
        mycursor.execute(sql_posts + posts_id ) 
             
    #user, posts tables have been updated, save the changes           
    cnx.commit()
    cnx.close()
else:
# response other than 200 - call failed
    print("Api error occured. Error code: " + str(response.status_code))




