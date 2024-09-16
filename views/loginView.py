import flet as ft

def login_page(page):
    """
    Creates and configures the login page for the authentication system.

    Args:
        page (ft.Page): The Flet page object to configure and display the login interface.

    This function sets up the layout and components for the login page, including:
    - A left panel with the company name.
    - A right panel with the login form, including email/username and password fields,
      login button, forgot password link, SSO button, and Google sign-in button.

    The page layout includes:
    - A left panel with a centered text for the company name.
    - A right panel with a form consisting of text fields and buttons, centered on the page.
    """
    # Set page properties
    page.title = "Authentication System"
    page.window_full_screen = True  # Set to False to avoid full screen
    page.vertical_alignment = ft.MainAxisAlignment.CENTER  # Center content vertically
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  # Center content horizontally
    page.bgcolor = "black"

    # Left panel with company information
    left_panel = ft.Container(
        content=ft.Stack(
            [
                ft.Row(
                    [
                        ft.Text(
                            "VECOAGREINT S.A.S",
                            color="white",
                            size=80,
                            weight="bold",
                        )
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                ),
            ],
            expand=True,  # Allows the Stack to take up all available space
        ),
        bgcolor="black",
        width=500,  # Fixed width of the container
        expand=True,  # Allows the container to occupy all available space
        alignment=ft.alignment.center_left,
    )

    # Right panel with the login form (without authentication functionality)
    email_input = ft.TextField(label="Email or Username", width=350)
    password_input = ft.TextField(label="Password", password=True, can_reveal_password=True, width=350)

    form_column = ft.Column(
        controls=[
            email_input,
            password_input,
            ft.ElevatedButton(
                text="Log In",
                width=350,
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

    right_panel = ft.Container(
        content=form_column,
        bgcolor="white",
        padding=40,
        width=500,
        alignment=ft.alignment.center,
    )

    # Main structure with two columns
    main_view = ft.Row(
        controls=[left_panel, right_panel],
        alignment="center",
        expand=True,
    )

    # Add the main view to the page
    page.add(main_view)
