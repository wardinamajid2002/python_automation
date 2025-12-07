
from flask import Flask, request, jsonify
# app = Flask(__name__)
acc = Flask(__name__)

AUTHORIZED_USERS = {"admin" : "secret"}

# @app.route('/')
# def hello_world():
#     return 'let me learn this'


def get_current_time():
    from datetime import datetime
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time


@acc.route('/secure-data')

def secure_data():
    auth = request.authorization
    
    return jsonify({"message" : " Welcome to the secure data !!!"}) , 401





def check_user(username, password) :
    return AUTHORIZED_USERS.get(username) == password





if __name__ == '__main__':
    #app.run(debug=True)
    acc.run(debug = True)
