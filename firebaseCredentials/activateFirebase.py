import firebase_admin
from firebase_admin import credentials, firestore


# Function to initialize Firebase
def initialize_firebase():
    """
    Initializes the Firebase app if it has not been initialized previously.
    Checks if the credentials are valid and if the app is already initialized.
    """
    if not firebase_admin._apps:  # Check if it has already been initialized
        try:
            cred = credentials.Certificate(
                "../firebaseCredentials/vecoagreint-12842-firebase-adminsdk-tz90k-dec062fbc3.json"
            )
            firebase_admin.initialize_app(cred)
            print("Firebase has been initialized successfully.")
        except Exception as e:
            print(f"Error initializing Firebase: {e}")
            raise e
    else:
        print("Firebase was already initialized.")


# Function to get a reference to Firestore
def get_firestore_client():
    """
    Returns a reference to the Firestore client.
    Make sure Firebase is initialized before obtaining the client.
    """
    try:
        initialize_firebase()
        return firestore.client()
    except Exception as e:
        print(f"Error getting Firestore client: {e}")
        raise e
