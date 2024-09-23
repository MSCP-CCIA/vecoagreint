import flet as ft
from authentication.Login import authenticate_user

def login_page(page: ft.Page):
    """
    Creates and configures the login page for the authentication system.
    Args:
        page (ft.Page): The Flet page object to configure and display the login interface.
    """
    page.title = "Authentication System"
    page.window_full_screen = True
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.bgcolor = "black"

    # Ensure that the image path is correct
    image_path = "path_to_your_image.png"  # Change this to your actual image path

    # Left panel with the company name and image
    left_panel = ft.Container(
        content=ft.Stack(
            [
                ft.Image(
                    src=image_path,  # Add your image path here
                    fit=ft.ImageFit.CONTAIN,
                    width=300,  # Adjust the width based on your design
                    height=300,  # Adjust the height based on your design
                ),
                ft.Text(
                    "VECOAGREINT S.A.S",
                    color="white",
                    size=80,
                    weight="bold",
                )
            ],
            expand=True,
        ),
        bgcolor="black",
        width=500,
        expand=True,
        alignment=ft.alignment.center,
    )

    # Inputs for email and password
    email_input = ft.TextField(label="Email or Username", width=350)
    password_input = ft.TextField(label="Password", password=True, can_reveal_password=True, width=350)

    def on_login_click(e):
        email = email_input.value
        password = password_input.value

        # Call authenticate_user
        is_authenticated, id_token, refresh_token = authenticate_user(email, password)

        if is_authenticated:

            # Navigate to the main menu view if authentication is successful
            page.go("/mainMenuView")
        else:
            # Show snack bar with error message
            page.snack_bar("Authentication failed. Please check your email and password.")
            page.update()

    # Form content
    form_column = ft.Column(
        controls=[
            email_input,
            password_input,
            ft.ElevatedButton(
                text="Log In",
                width=350,
                on_click=on_login_click,
                style=ft.ButtonStyle(
                    bgcolor={"": "#FF7043"},
                    color={"": "white"},
                    shape={"": ft.RoundedRectangleBorder(radius=8)},
                    padding={"": 15},
                ),
            ),
            ft.Text("Forgot password?", color="orange"),
            ft.ElevatedButton(
                text="Continue with SSO",
                width=350,
                style=ft.ButtonStyle(
                    bgcolor={"": "white"},
                    color={"": "black"},
                    shape={"": ft.RoundedRectangleBorder(radius=8)},
                    padding={"": 15},
                ),
            ),
            ft.ElevatedButton(
                text="Continue with Google",
                width=350,
                style=ft.ButtonStyle(
                    bgcolor={"": "white"},
                    color={"": "black"},
                    shape={"": ft.RoundedRectangleBorder(radius=8)},
                    padding={"": 15},
                ),
            ),
        ],
        spacing=10,
        alignment="start",
    )

    # Right panel with the form
    right_panel = ft.Container(
        content=form_column,
        bgcolor="white",
        padding=40,
        width=500,
        alignment=ft.alignment.center,
    )

    # Combine panels in a row
    main_view = ft.Row(
        controls=[left_panel, right_panel],
        alignment="center",
        expand=True,
    )

    # Add the main view to the page
    page.add(main_view)
