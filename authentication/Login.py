import requests


def authenticate_user(email, password):
    """
    Authenticates a user with Firebase using email and password.

    Args:
        email (str): The user's email address.
        password (str): The user's password.

    Returns:
        tuple: A tuple with three elements:
            - bool: Indicates whether the authentication was successful.
            - str: The user's ID token if authentication was successful, otherwise None.
            - str: The user's refresh token if authentication was successful, otherwise None.
    """
    api_key = (
        "AIzaSyCeNt6Za0MM37AwxUKtJGdV9JcXqDvRs0w"  # Replace with your Firebase API key
    )
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={api_key}"
    payload = {"email": email, "password": password, "returnSecureToken": True}

    try:
        response = requests.post(url, json=payload)
        response.raise_for_status()  # Raises an exception for HTTP 4xx/5xx status codes

        response_data = response.json()
        if response_data.get("error"):
            # Handle Firebase-specific errors
            error_message = response_data["error"].get("message", "Unknown error")
            print(f"Authentication error: {error_message}")
            return False, None, None

        id_token = response_data.get("idToken")
        refresh_token = response_data.get("refreshToken")
        print("Authentication successful")
        return True, id_token, refresh_token

    except requests.exceptions.RequestException as e:
        # Handle request errors
        print(f"Error during request: {e}")
        return False, None, None
