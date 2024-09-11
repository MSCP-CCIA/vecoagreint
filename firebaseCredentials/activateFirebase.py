import firebase_admin
from firebase_admin import credentials


def FirebaseCredentials():
    cred = credentials.Certificate("../firebaseCredentials/credentials.json")
    return firebase_admin.initialize_app(cred)
