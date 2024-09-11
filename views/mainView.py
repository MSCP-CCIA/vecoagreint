import flet as ft
from loginView import login_page  # Importa la función login_page desde login.py

# Simulación del objeto auth
class AuthSimulator:
    def sign_in_with_email_and_password(self, email, password):
        # Lógica simulada de inicio de sesión
        if email == "test@example.com" and password == "password":
            return {"email": email}
        else:
            raise Exception("Invalid credentials")

def main(page: ft.Page):
    auth = AuthSimulator()  # Crea una instancia del simulador de autenticación
    login_page(page, auth)  # Llama a la página de inicio de sesión

ft.app(target=main)



