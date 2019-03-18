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



# Create an instance of flask
app = Flask(__name__)

# Create an instance of the sensehat
sense = SenseHat()

# Define the root route
@app.route('/')
def index():
    return 'Look the flask server is running'
    
    
    
# Fetch the service account key JSON file contents
cred = credentials.Certificate('./credential.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://environment-pi.firebaseio.com/'
})


ref = db.reference('/ambilight/')



#Function to send colors to sensehat
def setColor(color_data):
	if color_data['state'] == 'on':
		color = color_data['value'].lstrip('#')
		rgb = tuple(int(color[i:i+2], 16) for i in (0, 2 ,4))
		for x in range(0,8):
			for y in range(0,8):
				sense.set_pixel(x, y, rgb)
	else:
		for x in range(0,8):
			for y in range(0,8):
				sense.set_pixel(x, y, [0, 0, 0])
				
				
# read color from firebase
def readAmbilightData():
    
    # get color 
    # set sense color to that color
    # eazy pizzy

    
    
if __name__ == '__main__':
    app.run(host='192.168.1.27', port=8082, debug=True)    

