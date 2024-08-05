import requests
from flask import Flask, jsonify

app = Flask(__name__)

mockDatabase = {}

@app.route("/", methods=["GET"])
def homePage():
    return "Welcome to the Lichess API"

@app.route("/users", methods=["GET"])
def getAllUser():
    return jsonify({"users": mockDatabase})

@app.route("/user/<username>", methods=["GET"])
def getUserStat(username):
    if username in mockDatabase:
        return mockDatabase[username]
    else:
        return jsonify({"error": " Could not retrieve user: " + username, "Status Code": 404})


@app.route("/user/<username>", methods=["POST"])
def createUser(username):
    url = f'https://lichess.org/api/user/{username}'
    response = requests.get(url)
    if response.status_code == 200:
        mockDatabase[username] = response.json()
        return jsonify({"message": " Successfully created the user", "User": username})
    else:
        return jsonify({"error": " Could not create user", "Status Code": 404})


@app.route("/user/<username>", methods=["DELETE"])
def deleteUser(username):
    if username in mockDatabase:
        del mockDatabase[username]
        return jsonify({"message": " Successfully deleted the user", "User": username})
    else:
        return jsonify({"error": " Could not find user", "Status Code": 404})

@app.route("/user/<username>/<updateUser>/", methods=["PUT"])
def updateUser(username, updateUser):
    if username in mockDatabase:
        mockDatabase[username] = updateUser
        return jsonify({"message": " Successfully updated the user", "User": username})
    else:
        return jsonify({"error": " Could not update user", "Status Code": 404})


@app.route("/user/<username>/<field>/<value>", methods=["PATCH"])
def updateUserField(username, field, value):
    if username in mockDatabase:
        mockDatabase[username][field] = value
        return jsonify({"message": " Successfully partially updated the user", "User": username})
    else:
        return jsonify({"error": " Could not partially update user", "Status Code": 404})