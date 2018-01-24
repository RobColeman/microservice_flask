# users-service/project/__init__.py

from flask import Flask, jsonify

# instantiate the app

app = Flask(__name__)

@app.route('/users/ping', methods=['GET'])
def ping_pong():
    response = jsonify({
        'status': 'success',
        'message': 'pong!'
        })
    return response