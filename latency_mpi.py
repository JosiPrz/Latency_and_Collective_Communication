from mpi4py import MPI
import numpy as np
import time

def main():
    # Inicializar el comunicador
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()

    # Número de repeticiones
    N = 10000
    message_size = 1  # Mensaje de 1 byte
    message = np.zeros(message_size, dtype='b')  # Crear un mensaje de 1 byte

    if rank == 0:
        # Proceso 0
        start_time = time.time()  # Iniciar el temporizador

        for _ in range(N):
            comm.send(message, dest=1)  # Enviar mensaje a proceso 1
            comm.recv(source=1)  # Recibir el mensaje de vuelta

        end_time = time.time()  # Finalizar el temporizador

        # Calcular el tiempo total y la latencia promedio
        total_time = end_time - start_time
        average_latency = (total_time / N) * 1e6  # Convertir a microsegundos
        estimated_unidirectional_latency = average_latency / 2  # Latencia unidireccional

        # Imprimir resultados
        print(f"Mensaje de {message_size} byte transmitido {N} veces.")
        print(f"Latencia promedio por mensaje (ida y vuelta): {average_latency:.2f} microsegundos")
        print(f"Latencia estimada unidireccional: {estimated_unidirectional_latency:.2f} microsegundos")

    elif rank == 1:
        # Proceso 1
        for _ in range(N):
            comm.recv(source=0)  # Recibir el mensaje del proceso 0
            comm.send(message, dest=0)  # Retornar el mensaje al proceso 0

if __name__ == "__main__":
    main()