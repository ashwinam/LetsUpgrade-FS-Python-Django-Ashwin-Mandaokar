from flask import Flask, config, request, render_template
import json
import pyrebase


app = Flask(__name__)
Config = {
    "apiKey": "AIzaSyDedOdPyemU-ZF6Ke3oJv7h7RIVxyavgPE",
    "authDomain": "myflaskapp-76812.firebaseapp.com",
    "databaseURL": "https://myflaskapp-76812-default-rtdb.firebaseio.com",
    "projectId": "myflaskapp-76812",
    "storageBucket": "myflaskapp-76812.appspot.com",
    "messagingSenderId": "658298615340",
    "appId": "1:658298615340:web:8b5247a9b37819e97a4389",
    "measurementId": "G-BCW81G2S7H"
}

# initializing firebase
firebase = pyrebase.initialize_app(Config)

# initializing the database
db = firebase.database()

# Post
# data = {
#     "Name": "preety",
#     "age": 25
# }


data={"details":{
    "Name":"Rahul",
    "age":24,
    "address":"Babupeth"
}}
db.child("User_data").set(data)
db.child("User_data").remove()
# db.remove()


@app.route("/")
def hello_world():
    return('Hello World!')


if __name__ == "__main__":
    app.run(debug=True, port=8080, host='Localhost')
