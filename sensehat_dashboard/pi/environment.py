'''
Sensehat Dashboard
=========================================
Author: The Great Nawang Tendar
Modified: 17-03-2019
-----------------------------------------
Installation:
sudo pip install -U Flask (python2)
sudo pip3 install -U Flask (python3)
-----------------------------------------
Docs: http://flask.pocoo.org/docs/1.0/
=========================================
'''
# Import the libraries
from flask import Flask, jsonify, render_template, request
from sense_hat import SenseHat
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import time
import sys

# Create an instance of flask
app = Flask(__name__)

# Create an instance of the sensehat
sense = SenseHat()

# Define the root route
@app.route('/')
def index():
    return 'Look the flask server is running'
    
    
    
# Fetch the service account key JSON file contents
cred = credentials.Certificate('./credentials.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://environment-pi.firebaseio.com/'
})


ref = db.reference('/environment/')

def updateEnvironmentData():
    environment_obj = {
        'temperature': {
            'value': round(sense.get_temperature()),
            'unit': u'C'
        },
        'humidity': {
            'value': round(sense.get_humidity()),
            'unit': u'%'
        },
        'pressure': {
            'value': round(sense.get_pressure()),
            'unit': u'mbar'
        }
    }
    ref.set(environment_obj)

try:
    while True:
        #every 60 seconds, new data pass to firebase
        updateEnvironmentData()
        
        time.sleep(60)
    
except (KeyboardInterrupt, SystemExit):
    sys.exit(0)
    
    
if __name__ == '__main__':
    app.run(host='192.168.1.27', port=8081, debug=True)   
