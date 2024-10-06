import flet as ft
from dataBaseFirebase.fireStoreCrud import *


def driverFormView(page: ft.Page):
    """
    Creates and configures the driver form page.
    """
    page.title = "Driver Form"
    page.bgcolor = "#1A1A1A"

    title = ft.Text(
        "Driver Information",
        color="white",
        size=90,
        weight="bold",
    )

    title_container = ft.Container(
        content=title,
        padding=20,
        alignment=ft.alignment.center,
    )

    # Input fields for driver data
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

    tipo_vehiculo_input = ft.TextField(
        label="Tipo de Vehículo",
        hint_text="Ingrese el tipo de vehículo",
        bgcolor="#333",
        color="white",
        border_color="#FF7043",
        width=700,
    )

    placa_input = ft.TextField(
        label="Placa del Vehículo",
        hint_text="Ingrese la placa del vehículo",
        bgcolor="#333",
        color="white",
        border_color="#FF7043",
        width=700,
    )

    # Buttons to search and save
    search_button = ft.ElevatedButton(
        text="Buscar",
        on_click=lambda e: search_driver(
            cedula_input.value,
            nombre_input,
            apellidos_input,
            tipo_vehiculo_input,
            placa_input,
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

    save_button = ft.ElevatedButton(
        text="Guardar",
        on_click=lambda e: save_driver(
            cedula_input,
            nombre_input,
            apellidos_input,
            tipo_vehiculo_input,
            placa_input,
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
        on_click=lambda e: page.go(
            "/"
        ),  # Cambia '/' al path de tu página principal
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
                    tipo_vehiculo_input,
                    placa_input,
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
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20,
    )

    page.add(main_view)


def search_driver(
    cedula, nombre_input, apellidos_input, tipo_vehiculo_input, placa_input
):
    print("toco boton")
    """
    Function to handle driver search.
    Updates the input fields with driver data if found.
    """
    driver_data = read_document("drivers", cedula)
    if driver_data:
        # Actualiza los campos con los datos del conductor
        nombre_input.value = driver_data.get("first_name")
        apellidos_input.value = driver_data.get("last_name")
        tipo_vehiculo_input.value = driver_data.get("type_vehicle")
        placa_input.value = driver_data.get("plate")

        # Llama a update() para reflejar los cambios en la interfaz
        nombre_input.update()
        apellidos_input.update()
        tipo_vehiculo_input.update()
        placa_input.update()

        print(f"Conductor encontrado: {driver_data}")
    else:
        print(f"No se encontró un conductor con la cédula: {cedula}")
        # Si no se encuentra el conductor, vacía los campos
        nombre_input.value = ""
        apellidos_input.value = ""
        tipo_vehiculo_input.value = ""
        placa_input.value = ""
        nombre_input.update()
        apellidos_input.update()
        tipo_vehiculo_input.update()
        placa_input.update()


def save_driver(cedula, nombre, apellidos, tipo_vehiculo, placa):
    """
    Function to handle saving driver data.
    """
    driver_data = {
        "first_name": nombre.value,
        "last_name": apellidos.value,
        "type_vehicle": tipo_vehiculo.value,
        "plate": placa.value,
    }

    # Usa la función de creación/actualización del CRUD para guardar los datos
    create_document(driver_data, "drivers", cedula.value)
    print(
        f"Conductor guardado: {cedula.value}, {nombre.value} {apellidos.value}, {tipo_vehiculo.value}, {placa.value}"
    )
    nombre.value = ""
    apellidos.value = ""
    tipo_vehiculo.value = ""
    placa.value = ""
    nombre.update()
    apellidos.update()
    tipo_vehiculo.update()
    placa.update()
