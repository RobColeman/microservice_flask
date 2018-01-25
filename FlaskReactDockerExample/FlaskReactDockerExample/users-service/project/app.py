# users-service/project/app.py

from flask import Flask, jsonify
import os, sys

# instantiate the app

app = Flask(__name__)

#app.config.from_object('project.config.DevelopmentConfig')
# set config
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)
#print(app.config, file=sys.stderr)

@app.route('/users/ping', methods=['GET'])
def ping_pong():
    response = jsonify({
        'status': 'success',
        'message': 'pong!'
        })
    return response
