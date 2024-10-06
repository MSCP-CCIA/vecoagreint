import flet as ft
from dataBaseFirebase.fireStoreCrud import *


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
        on_click=lambda e: search_customer(
            cedula_input.value, nombre_input, apellidos_input, telefono_input
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
        on_click=lambda e: save_customer(
            cedula_input,
            nombre_input,
            apellidos_input,
            telefono_input,
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
            ),
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20,
    )

    page.add(main_view)


def search_customer(cedula, nombre_input, apellidos_input, telefono_input):
    """
    Function to handle customer search.
    Updates the input fields with customer data if found.
    """
    # Busca el documento en la colección 'customers' usando la función de lectura del CRUD
    customer_data = read_document("customers", cedula)

    if customer_data:
        # Si se encuentra, actualiza las cajas de texto
        nombre_input.value = customer_data.get("first_name")
        apellidos_input.value = customer_data.get("last_name")
        telefono_input.value = customer_data.get("phone")

        # Refresca la página para mostrar los nuevos valores
        nombre_input.update()
        apellidos_input.update()
        telefono_input.update()

        print(f"Cliente encontrado: {customer_data}")
    else:
        # Si no se encuentra, puedes vaciar los campos o mostrar un mensaje de error
        print(f"No se encontró un cliente con la cédula: {cedula}")
        nombre_input.value = ""
        apellidos_input.value = ""
        telefono_input.value = ""

        nombre_input.update()
        apellidos_input.update()
        telefono_input.update()


def save_customer(cedula, nombre, apellidos, telefono):
    """
    Function to handle saving customer data.
    """
    customer_data = {
        "nombre": nombre.value,
        "apellidos": apellidos.value,
        "telefono": telefono.value,
    }

    try:
        # Check if the customer exists to decide between creating or updating
        existing_customer = read_document("customers", cedula.value)

        if existing_customer:
            update_document("customers", cedula, customer_data)
            print(f"Cliente {cedula} actualizado correctamente.")
        else:
            create_document(customer_data, "customer", cedula)
            print(f"Cliente {cedula} creado correctamente.")
    except Exception as e:
        print(f"Error al guardar cliente: {e}")
