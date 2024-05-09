import flet as ft
from algoritmo import simulador

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
            ft.Row(controls=[s, l, mu, n]),
            ft.Row(controls=[ft.ElevatedButton(text="Iniciar", color="green", on_click=lambda: simulador(int(s.value), float(l.value), float(mu.value), int(n.value)))]),
            ft.Text(value="Resultado de la Simulación", size=24),
            ft.Text(value="Tiempo Promedio en el Sistema: "),
            ft.Text(value="Utilización de los Servidores: "),
        )

        # page.add(ft.Row(controls=[
        #     ft.ElevatedButton(text="Iniciar", color="green", on_click= lambda: simulador(int(s.value), float(l.value), float(mu.value), int(n.value), )),
        #     ft.Text(value="Resultado de la Simulación", size=24),
        #     ft.Text(value="Tiempo Promedio en el Sistema: "),
        #     ft.Text(value="0.00"),  # Valor inicial
        #     ft.Text(value="Utilización de los Servidores: ")
        # ]))

    #     page.add(
    #         ft.Text(value="Resultado de la Simulación", size=24),
    #         ft.Text(value="Tiempo Promedio en el Sistema: "),
    #         ft.Text(value=1),
    #         ft.Text(value="Tiempo Ocupado de los Servidores: "),
    #         ft.Text(value=1)
    #     )

        # page.add(
        #     ft.Text(value="Simulación de Colas", size=24),
        #     ft.Row(controls=[s, l, mu, n]),
        # )

        


ft.app(main)
