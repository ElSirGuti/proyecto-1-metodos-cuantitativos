import simpy
import random

class Servidor:
    def __init__(self, env):
        self.env = env
        self.servidor = simpy.Resource(env, capacity=1)

    def atender_cliente(self, cliente):
        yield self.env.timeout(random.expovariate(1.0 / tasa_servicio))

def llegada_clientes(env, num_servidores, tasa_llegada, tasa_servicio):
    servidor = Servidor(env)
    for _ in range(num_servidores):
        env.process(servidor.atender_cliente(_))

    while True:
        yield env.timeout(random.expovariate(1.0 / tasa_llegada))
        with servidor.servidor.request() as req:
            yield req
            env.process(servidor.atender_cliente(_))

# Configuración del sistema
num_servidores = 3
tasa_llegada = 5  # clientes por unidad de tiempo
tasa_servicio = 2  # clientes atendidos por unidad de tiempo

env = simpy.Environment()
env.process(llegada_clientes(env, num_servidores, tasa_llegada, tasa_servicio))
env.run(until=100)  # Simulamos hasta el tiempo 100

# Cálculo de métricas
tiempo_promedio_sistema = env.now / num_servidores
utilizacion_servidores = (env.now / num_servidores) / env.now

print(f"Tiempo promedio en el sistema: {tiempo_promedio_sistema:.2f} unidades de tiempo")
print(f"Utilización de los servidores: {utilizacion_servidores:.2f}")
