import flet
import flet as ft
from loginView import login_page
from mainMenuView import mainMenuView
from customerView import customerFormView
from driverView import driverFormView


def main(page: ft.Page):
    """
    Main entry point for the Flet application. Sets up and displays the login page.
    """
    page.title = "Navigation App"
    page.window_full_screen = True
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    # Setup routes for navigation
    def route_change(route):
        page.clean()
        if page.route == "/":
            mainMenuView(page)
        elif page.route == "/mainMenuView":
            login_page(page)
        elif page.route == "/customerView":
            customerFormView(page)
        elif page.route == "/driverView":
            driverFormView(page)
        page.update()

    # Route initialization
    page.on_route_change = route_change
    page.go("/")


ft.app(target=main)
