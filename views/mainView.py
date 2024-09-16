import flet as ft
from loginView import login_page  # Import the login_page function from loginView.py

def main(page: ft.Page):
    """
    Main entry point for the Flet application. Sets up and displays the login page.

    Args:
        page (ft.Page): The Flet page object to configure and display the login interface.

    This function initializes the login page by calling the `login_page` function
    and passing the Flet page object. This setup will be used when the application starts.
    """
    # Create an instance of the authentication simulator
    login_page(page)  # Call the login page function

# Run the Flet app with the `main` function as the entry point
ft.app(target=main)



