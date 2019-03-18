import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Fetch the service account key JSON file contents
cred = credentials.Certificate('./credential.json')

# Initialize the app with a service account, granting admin privileges
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://environment-pi.firebaseio.com/'
})


ref = db.reference('/')


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
