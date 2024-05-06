import numpy as np

class Cliente:
    def __init__(self, tiempo_llegada, tiempo_servicio):
        self.tiempo_llegada = tiempo_llegada
        self.tiempo_servicio = tiempo_servicio
        self.tiempo_espera = 0

class Servidor:
    def __init__(self):
        self.ocupado = False

class Simulador:
    def __init__(self, numero_servidores, tasa_llegada, tasa_servicio, numero_clientes):
        self.numero_servidores = numero_servidores
        self.tasa_llegada = tasa_llegada
        self.tasa_servicio = tasa_servicio
        self.numero_clientes = numero_clientes

        # Crear lista de clientes
        self.clientes = []
        for i in range(self.numero_clientes):
            tiempo_llegada = np.log(np.random.rand()) / self.tasa_llegada
            tiempo_servicio = np.log(np.random.rand()) / self.tasa_servicio
            cliente = Cliente(tiempo_llegada, tiempo_servicio)
            self.clientes.append(cliente)

        # Crear lista de servidores
        self.servidores = [Servidor() for i in range(self.numero_servidores)]

        # Variables para métricas
        self.tiempo_promedio_sistema = 0
        self.utilizacion_servidores = 0

    def simular(self):
        tiempo_actual = 0
        tiempo_ocupado_servidores = 0

        for cliente in self.clientes:
            # Simulación de la atención del cliente
            servidor_libre = False
            for servidor in self.servidores:
                if not servidor.ocupado:
                    servidor.ocupado = True
                    tiempo_ocupado_servidores += cliente.tiempo_servicio
                    cliente.tiempo_espera = cliente.tiempo_llegada - tiempo_actual
                    break

            if not servidor_libre:
                cliente.tiempo_espera = cliente.tiempo_llegada - tiempo_actual

            # Actualización del tiempo actual
            tiempo_actual += cliente.tiempo_servicio

            # Liberar servidor
            if servidor_libre:
                servidor.ocupado = False

        # Cálculo de métricas
        self.tiempo_promedio_sistema = sum([cliente.tiempo_espera for cliente in self.clientes]) / self.numero_clientes
        self.utilizacion_servidores = tiempo_ocupado_servidores / tiempo_actual

    def mostrar_resultados(self):
        print("Parámetros del sistema:")
        print("  Número de servidores:", self.numero_servidores)
        print("  Tasa de llegada:", self.tasa_llegada)
        print("  Tasa de servicio:", self.tasa_servicio)
        print("  Número de clientes:", self.numero_clientes)
        print("\n")

        print("Métricas:")
        print("  Tiempo promedio en el sistema:", self.tiempo_promedio_sistema)
        print("  Utilización de los servidores:", self.utilizacion_servidores)

# Ejemplo de uso
simulador = Simulador(2, 5, 3, 1000)
simulador.simular()
simulador.mostrar_resultados()
