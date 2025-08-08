# Tarea 3: Latencia y Comunicación Colectiva
**Autor:** Josimark Pérez

## Descripción del Repositorio
Este repositorio contiene dos archivos principales que implementan experimentos relacionados con la latencia y comunicación colectiva utilizando MPI en Python:

1. **statistics_mpi.py**  
   - **Descripción**: Genera un arreglo de números aleatorios (0 a 100) y calcula estadísticas globales (mínimo, máximo y promedio) usando operaciones colectivas de MPI.
   - **Ejecución**:  
     1. Activa el entorno virtual desde PowerShell:  
        ```powershell
        .\venv\Scripts\Activate
        ```
     2. Ejecuta el script con:  
        ```powershell
        mpiexec -n 4 python c:\ruta\al\archivo\statistics_mpi.py 1000000
        ```

2. **latency_mpi.py**  
   - **Descripción**: Mide la latencia de comunicación entre dos procesos enviando y recibiendo un mensaje de 1 byte 10,000 veces.  
   - **Ejecución**:  
     1. Activa el entorno virtual desde PowerShell:  
        ```powershell
        .\venv\Scripts\Activate
        ```
     2. Ejecuta el script con:  
        ```powershell
        mpiexec -n 2 python c:\ruta\al\archivo\latency_mpi.py
        ```

## Requisitos
- **Bibliotecas**: Instala las dependencias listadas en `requirements.txt` con el comando:  
  ```bash
  pip install -r requirements.txt
  ```
- **MPI**: Asegúrate de tener Windows MPI instalado para ejecutar los scripts desde PowerShell.

## Informe de Resultados

### 1. Descripción de los Experimentos
Se realizaron dos experimentos utilizando la biblioteca `mpi4py` en Python para analizar la latencia en comunicaciones MPI:

#### Experimento 1: Cálculo de Estadísticas Globales
- **Objetivo**: Generar un arreglo de números aleatorios (0 a 100) y calcular estadísticas globales (mínimo, máximo y promedio) usando operaciones colectivas de MPI.
- **Metodología**: Los procesos generan datos localmente y calculan estadísticas globales mediante comunicación colectiva.

#### Experimento 2: Medición de Latencia Punto a Punto
- **Objetivo**: Medir la latencia de comunicación entre dos procesos enviando y recibiendo un mensaje de 1 byte 10,000 veces.
- **Metodología**: Se cronometra el tiempo de envío y recepción para estimar la latencia promedio.

### 2. Resultados Observados

#### Experimento 1: Estadísticas Globales
- **Mínimo Global**: 0  
- **Máximo Global**: 100  
- **Promedio Global**: 50.06  

#### Experimento 2: Latencia Punto a Punto
- **Mensaje Transmitido**: 1 byte  
- **Latencia Promedio (ida y vuelta)**: 35.58 µs  
- **Latencia Unidireccional Estimada**: 17.79 µs  

### 3. Tiempos Observados
El segundo experimento mostró una latencia promedio de 35.58 µs por mensaje, valor típico para comunicaciones rápidas en memoria compartida o redes de baja latencia.

### 4. Causas de Variabilidad
Los resultados pueden variar debido a:

- **Carga del Sistema**: Competencia por recursos de CPU o red puede aumentar los tiempos de latencia.
- **Configuración de Hardware**: La velocidad del bus, tipo de red o arquitectura del procesador influyen en el rendimiento.
- **Tamaño de los Datos**: En el Experimento 1, el tamaño del arreglo afecta el tiempo de ejecución. En el Experimento 2, el mensaje pequeño asegura latencias predecibles.
- **Método de Comunicación**: Las comunicaciones colectivas pueden introducir sobrecarga por sincronización, mientras que las punto a punto son más rápidas.
- **Variaciones en la Red**: En entornos distribuidos, la congestión o distancia física entre nodos puede incrementar la latencia.


