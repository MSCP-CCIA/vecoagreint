import flet as ft


def mainMenuView(page: ft.Page):
    """
    Creates and configures the main page with a title and sections for navigation.
    """
    page.title = "Main Page"
    page.window_full_screen = True
    page.bgcolor = "#1A1A1A"

    title = ft.Text(
        "VECOAGREINT S.A.S",
        color="white",
        size=100,
        weight="bold",
    )

    title_container = ft.Container(
        content=title,
        padding=20,
        alignment=ft.alignment.center,
    )

    def on_section_click(view_name):
        """
        Handles section button click event to navigate to the specified view.
        """
        page.go(view_name)

    button_style = ft.ButtonStyle(
        bgcolor="#FF7043",
        color="white",
        shape=ft.RoundedRectangleBorder(radius=8),
        padding=10,  # Disminuir el padding para hacer el botón más compacto
        elevation=3,
    )

    # Secciones
    certification_section = ft.Container(
        content=ft.ElevatedButton(
            text="Certification",
            icon=ft.icons.BOOKMARK,
            icon_color="white",
            width=200,  # Disminuir el ancho del botón
            height=70,  # Disminuir la altura del botón
            on_click=lambda e: page.go("/certificationView"),
            style=button_style,
        ),
        bgcolor="#333",
        border_radius=15,
        padding=10,
        margin=10,
        alignment=ft.alignment.center,
    )

    recepts_section = ft.Container(
        content=ft.ElevatedButton(
            text="Recepts",
            icon=ft.icons.RECEIPT,
            icon_color="white",
            width=200,
            height=70,
            on_click=lambda e: page.go("/receptsView"),
            style=button_style,
        ),
        bgcolor="#333",
        border_radius=15,
        padding=10,
        margin=10,
        alignment=ft.alignment.center,
    )

    departures_section = ft.Container(
        content=ft.ElevatedButton(
            text="Departures",
            icon=ft.icons.DIRECTIONS_CAR,
            icon_color="white",
            width=200,
            height=70,
            on_click=lambda e: page.go("/departuresView"),
            style=button_style,
        ),
        bgcolor="#333",
        border_radius=15,
        padding=10,
        margin=10,
        alignment=ft.alignment.center,
    )

    # Botones Customer y Driver
    customer_section = ft.Container(
        content=ft.ElevatedButton(
            text="Customer",
            icon=ft.icons.PERSON,
            icon_color="white",
            width=200,
            height=70,
            on_click=lambda e: page.go("/customerView"),
            style=button_style,
        ),
        bgcolor="#333",
        border_radius=15,
        padding=10,
        margin=10,
        alignment=ft.alignment.center,
    )

    driver_section = ft.Container(
        content=ft.ElevatedButton(
            text="Driver",
            icon=ft.icons.PERSON_PIN_CIRCLE,
            icon_color="white",
            width=200,
            height=70,
            on_click=lambda e: page.go("/driverView"),
            style=button_style,
        ),
        bgcolor="#333",
        border_radius=15,
        padding=10,
        margin=10,
        alignment=ft.alignment.center,
    )

    # Botón de Logout
    logout_button = ft.ElevatedButton(
        text="Logout",
        width=100,
        on_click=lambda e: page.go("/"),
        style=button_style,
    )

    logout_container = ft.Container(
        content=logout_button,
        alignment=ft.alignment.top_right,  # Colocar en la esquina superior derecha
        padding=20,
    )

    # Modificar el Row para incluir todos los botones
    main_view = ft.Column(
        controls=[
            title_container,
            ft.Row(
                controls=[
                    certification_section,
                    recepts_section,
                    departures_section,
                    customer_section,
                    driver_section,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=20,
            ),
            logout_container,  # Añade el contenedor del botón de logout
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20,
    )

    page.add(main_view)
