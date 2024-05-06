import flet as ft
import simular


def main(page: ft.Page):
        page.title = "Simulacion de Colas"
        

        s = ft.TextField(
            label="Numero de Servidores",
            value="0", 
            text_align="right", 
            width="300",
            )

        l = ft.TextField(
            label="Clientes / Unidad de Tiempo",
            value="0", 
            text_align="right", 
            width="300"
            )
        
        mu = ft.TextField(
            label="Clientes Atendidos / Unidad de Tiempo",
            value="0", 
            text_align="right", 
            width="300"
            )
        
        n = ft.TextField(
            label="Clientes a Simular",
            value="0", 
            text_align="right", 
            width="300"
            )

        page.add(
            ft.Text(value="Simulacion de Colas", size=24),
            ft.Row(controls=[
                s,
                l,
                mu,
                n
            ]),        
        )

        page.add(ft.Row(controls=[
            ft.ElevatedButton(text="Iniciar", color="green", on_click= algoritmo.simular(s,l,mu,n))
        ]))

        page.add(
            ft.Text(value="Resultado de la Simulación", size=24),
            ft.Text(value="Tiempo Promedio en el Sistema: "),
            ft.Text(value=1),
            ft.Text(value="Tiempo Ocupado de los Servidores: "),
            ft.Text(value=1)
        )


ft.app(main)
