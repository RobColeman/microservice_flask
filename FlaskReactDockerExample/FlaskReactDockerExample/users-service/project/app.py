# users-service/project/app.py

from flask import Flask, jsonify

# instantiate the app

app = Flask(__name__)

app.config.from_object('project.config.DevelopmentConfig')

@app.route('/users/ping', methods=['GET'])
def ping_pong():
    response = jsonify({
        'status': 'success',
        'message': 'pong!'
        })
    return response
