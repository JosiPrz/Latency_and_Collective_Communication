from mpi4py import MPI
import numpy as np
import sys

def main():
    # Inicializar el comunicador
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()

    # Inicializar N
    N = 0

    # El proceso raíz (rank 0) inicializa el arreglo
    if rank == 0:
        N = int(sys.argv[1])  # Tamaño del arreglo
        if N % size != 0:
            raise ValueError("N debe ser divisible por el número de procesos.")
        
        # Generar un arreglo aleatorio de N números entre 0 y 100
        data = np.random.randint(0, 101, size=N, dtype=np.int32)
    else:
        data = None

    # Paso 1: Enviar el tamaño del arreglo a todos los procesos
    N = comm.bcast(N, root=0)

    # Paso 2: Distribuir partes del arreglo entre los procesos
    local_data = np.zeros(N // size, dtype=np.int32)
    comm.Scatter(data, local_data, root=0)

    # Comprobar si local_data tiene elementos
    if len(local_data) > 0:
        # Cada proceso calcula el mínimo, máximo y promedio de su subarreglo
        local_min = np.min(local_data)
        local_max = np.max(local_data)
        local_avg = np.mean(local_data)
    else:
        local_min = float('inf')
        local_max = float('-inf')
        local_avg = 0

    # Paso 3: Usar MPI_Reduce para calcular el mínimo, máximo y promedio global
    global_min = comm.reduce(local_min, op=MPI.MIN, root=0)
    global_max = comm.reduce(local_max, op=MPI.MAX, root=0)
    
    # Calcular la suma de los promedios locales y contar el número de elementos
    local_count = len(local_data)
    global_sum_avg = comm.reduce(local_avg * local_count, op=MPI.SUM, root=0)
    total_count = comm.reduce(local_count, op=MPI.SUM, root=0)

    # Paso 4: Calcular el promedio global en el proceso raíz
    if rank == 0:
        global_avg = global_sum_avg / total_count  # Calcular el promedio global
        print(f"Estadísticas Globales:")
        print(f"Mínimo Global: {global_min}")
        print(f"Máximo Global: {global_max}")
        print(f"Promedio Global: {global_avg}")

if __name__ == "__main__":
    main()