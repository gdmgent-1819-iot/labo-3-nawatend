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
cred = credentials.Certificate('./credentials.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://environment-pi.firebaseio.com/'
})


ref = db.reference('/ambilight/')



#Function to send colors to sensehat
def setColor(rgbColor):
	
	for x in range(0,8):
		for y in range(0,8):
			sense.set_pixel(x, y, rgbColor)
	
				
#hex color to rgb
hex2rgb = lambda hx: (int(hx[1:3],16),int(hx[3:5],16),int(hx[5:7],16))

			
# read color from firebase
def readAmbilightData():
    
    # get color 
    # set sense color to that color
    # eazy pizzy
    rgbColor = hex2rgb(ref.get()["color"])	
    print(rgbColor)
    setColor(rgbColor)


while True:    
	readAmbilightData()
 
if __name__ == '__main__':
    app.run(host='192.168.1.27', port=8082, debug=True)   

