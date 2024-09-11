import flet as ft
from firebase_admin import auth

def login_page(page):
    page.title = "Authentication System"
    page.window_full_screen = True  # Para abrir la aplicación en pantalla completa
    page.vertical_alignment = ft.MainAxisAlignment.CENTER  # Centrar el contenido verticalmente
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  # Centrar el contenido horizontalmente
    page.bgcolor = "black"

    def sign_in(e):
        email = email_input.value
        password = password_input.value
        try:
            user = auth.sign_in_with_email_and_password(email, password)
            print(f"User {user['email']} signed in successfully!")
            page.views.clear()
            home_page(page, user)
        except Exception as ex:
            error_label.value = str(ex)
            error_label.visible = True
            page.update()

    def sign_in_with_google(e):
        # Aquí deberías implementar la lógica para autenticación con Google
        pass

    # Panel izquierdo con la información
    left_panel = ft.Container(
        content=ft.Stack(
            [
                ft.Image(
                    src="assets/excavator-2195330_1280.jpg",  # Ruta a tu imagen
                    expand=True,  # Permite que la imagen ocupe todo el espacio del contenedor
                    opacity=0.3,
                    fit=ft.ImageFit.FILL,  # Asegura que la imagen cubra todo el espacio
                ),
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
            expand=True,  # Permite que el Stack ocupe todo el espacio del contenedor
        ),
        bgcolor="black",
        width=500,  # Ancho fijo del contenedor
        expand=True,  # Permite que el contenedor ocupe todo el espacio disponible
        alignment=ft.alignment.center_left,
    )

    # Panel derecho con el formulario de inicio de sesión
    email_input = ft.TextField(label="Email or Username", width=350 )
    password_input = ft.TextField(label="Password", password=True, can_reveal_password=True, width=350)

    sign_in_button = ft.ElevatedButton(
        text="Log In",
        on_click=sign_in,
        width=350,
        style=ft.ButtonStyle(
            bgcolor={"": "#FF7043"},
            color={"": "white"},
            shape={"": ft.RoundedRectangleBorder(radius=8)},
            padding={"": 15},
        ),
    )

    google_sign_in_button = ft.ElevatedButton(
        text="Continue with Google",
        on_click=sign_in_with_google,
        width=350,
        style=ft.ButtonStyle(
            bgcolor={"": "white"},
            color={"": "black"},
            shape={"": ft.RoundedRectangleBorder(radius=8)},
            padding={"": 15},
        ),
    )

    sso_button = ft.ElevatedButton(
        text="Continue with SSO",
        width=350,
        style=ft.ButtonStyle(
            bgcolor={"": "white"},
            color={"": "black"},
            shape={"": ft.RoundedRectangleBorder(radius=8)},
            padding={"": 15},
        ),
    )

    error_label = ft.Text(color="red", visible=False)

    form_column = ft.Column(
        controls=[
            email_input,
            password_input,
            sign_in_button,
            ft.Text("Forgot password?", color="orange"),
            sso_button,
            google_sign_in_button,
            error_label,
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

    # Estructura principal con dos columnas
    main_view = ft.Row(
        controls=[left_panel, right_panel],
        alignment="center",
        expand=True,
    )

    page.add(main_view)

def home_page(page, user):
    page.add(ft.Text(f"Welcome, {user['email']}!", size=24, weight="bold"))

def main(page: ft.Page):
    page.title = "Authentication System"
    page.bgcolor = "white"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.padding = 0
    login_page(page)

ft.app(target=main)