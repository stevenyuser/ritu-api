import os, json
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# SECRETS_PATH = 'service_account.json'

class Firebase:
    def __init__(self):
        cred = credentials.Certificate(json.loads(os.environ["FIREBASE_ADMIN"]))
        firebase_admin.initialize_app(cred)
        db = firestore.client()   
        self.db = firestore.client()

    def get_db(self):
        return self.db

def start_firebase():
    firebase = Firebase()
    return firebase.get_db()