import firebase_admin
from firebase_admin import credentials


def initialize_firebase():
    """
    Initializes the Firebase application using the provided credentials.

    The function checks if Firebase has already been initialized before
    attempting to initialize it. If Firebase is already initialized, it
    returns the existing instance; otherwise, it initializes Firebase
    with the provided credentials and returns the initialized app instance.

    Returns:
        firebase_admin.App: The initialized Firebase app instance.

    Raises:
        FileNotFoundError: If the credentials file is not found at the specified path.
        ValueError: If there is an error loading the credentials.
    """
    # Path to the downloaded JSON credentials file
    cred_path = "../firebaseCredentials/vecoagreint-12842-firebase-adminsdk-tz90k-c010403cfa.json"

    try:
        cred = credentials.Certificate(cred_path)
    except FileNotFoundError as e:
        print(f"Error: Credentials file not found at the specified path: {cred_path}")
        raise e
    except ValueError as e:
        print(f"Error loading credentials file: {e}")
        raise e

    try:
        # Initialize Firebase only if it has not been initialized already
        if not firebase_admin._apps:
            app = firebase_admin.initialize_app(cred)
            print("Firebase successfully initialized")
            return app
        else:
            print("Firebase was already initialized")
            return firebase_admin.get_app()
    except Exception as e:
        print(f"Error initializing Firebase: {e}")
        raise e


if __name__ == "__main__":
    # Run the initialization function only if the script is executed directly
    initialize_firebase()
