import flet as ft

def customerFormView(page: ft.Page):
    """
    Creates and configures the customer form page.
    """
    page.title = "Customer Form"
    page.bgcolor = "#1A1A1A"

    title = ft.Text(
        "Customer Information",
        color="white",
        size=90,
        weight="bold",
    )

    title_container = ft.Container(
        content=title,
        padding=20,
        alignment=ft.alignment.center,
    )

    # Input fields for customer data
    cedula_input = ft.TextField(
        label="Cédula de Ciudadanía",
        hint_text="Ingrese el ID o cédula",
        bgcolor="#333",
        color="white",
        border_color="#FF7043",
        width=700,  # Ajusta el ancho según tus necesidades
    )

    nombre_input = ft.TextField(
        label="Nombre",
        hint_text="Ingrese el nombre",
        bgcolor="#333",
        color="white",
        border_color="#FF7043",
        width=700,
    )

    apellidos_input = ft.TextField(
        label="Apellidos",
        hint_text="Ingrese los apellidos",
        bgcolor="#333",
        color="white",
        border_color="#FF7043",
        width=700,
    )

    telefono_input = ft.TextField(
        label="Número de Teléfono",
        hint_text="Ingrese el número de teléfono",
        bgcolor="#333",
        color="white",
        border_color="#FF7043",
        width=700,
    )

    # Buttons to search and save
    search_button = ft.ElevatedButton(
        text="Buscar",
        on_click=lambda e: search_customer(cedula_input.value),
        style=ft.ButtonStyle(
            bgcolor="#FF7043",
            color="white",
            shape=ft.RoundedRectangleBorder(radius=8),
            padding=15,
            elevation=5,
        ),
        width=150,  # Ancho del botón
        height=60,  # Altura del botón
    )

    save_button = ft.ElevatedButton(
        text="Guardar",
        on_click=lambda e: save_customer(
            cedula_input.value,
            nombre_input.value,
            apellidos_input.value,
            telefono_input.value,
        ),
        style=ft.ButtonStyle(
            bgcolor="#FF7043",
            color="white",
            shape=ft.RoundedRectangleBorder(radius=8),
            padding=15,
            elevation=5,
        ),
        width=150,  # Ancho del botón
        height=60,  # Altura del botón
    )

    # Home button
    home_button = ft.ElevatedButton(
        text="Home",
        on_click=lambda e: page.go('/'),  # Cambia '/' al path de tu página principal
        style=ft.ButtonStyle(
            bgcolor="#FF7043",
            color="white",
            shape=ft.RoundedRectangleBorder(radius=8),
            padding=15,
            elevation=5,
        ),
        width=150,  # Ancho del botón
        height=60,  # Altura del botón
    )

    # Layout for the input fields and buttons
    input_container = ft.Row(
        controls=[
            ft.Column(
                controls=[
                    cedula_input,
                    nombre_input,
                    apellidos_input,
                    telefono_input,
                ],
                alignment=ft.MainAxisAlignment.START,
                spacing=10,
            ),
            ft.Column(
                controls=[
                    search_button,
                    save_button,
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=10,
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20,
    )

    # Main layout with title and input container
    main_view = ft.Column(
        controls=[
            title_container,
            input_container,
            # Add the home button at the bottom right
            ft.Row(
                controls=[home_button],
                alignment=ft.MainAxisAlignment.END,
                spacing=10,
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20,
    )

    page.add(main_view)

def search_customer(cedula):
    """
    Function to handle customer search.
    """
    # Aquí puedes implementar la lógica para buscar al cliente por cédula
    print(f"Buscando cliente con cédula: {cedula}")

def save_customer(cedula, nombre, apellidos, telefono):
    """
    Function to handle saving customer data.
    """
    # Aquí puedes implementar la lógica para guardar los datos del cliente
    print(f"Guardando cliente: {cedula}, {nombre} {apellidos}, {telefono}")
