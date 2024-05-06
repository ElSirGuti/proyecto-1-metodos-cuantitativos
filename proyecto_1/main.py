import flet as ft


def main(page: ft.Page):
        page
        page.add(ft.Column(controls=[
            ft.TextField(label="Numero de servidores"),
            ft.TextField(label="Clientes / unidad de tiempo"),
            ft.TextField(label="Clientes atendidos / unidad de tiempo"),
            ft.TextField(label="Clientes a simular"),
            ft.ElevatedButton(text="Iniciar")
        ]))


ft.app(main)
