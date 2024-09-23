import functools
import logging
import time

# Configuración básica del registro (logging)
logging.basicConfig(
    level=logging.INFO,  # Corregido de 'nivel' a 'level'
    format='%(asctime)s - %(levelname)s - %(message)s',  # Corregido 'nivel' y 'mensaje' a 'levelname' y 'message'
    handlers=[
        logging.StreamHandler()
    ]
)

class DecoradorAvanzado:
    def __init__(self, funcion):
        """
        Inicializa el decorador con la función a decorar.
        """
        self.funcion = funcion
        self.contador_llamadas = 0
        functools.update_wrapper(self, funcion)  # Preserva la metadata de la función original

    def __call__(self, *args, **kwargs):
        """
        Método que se ejecuta cuando se llama a la función decorada.
        """
        self.contador_llamadas += 1
        nombre_funcion = self.funcion.__name__
        argumentos = f"args: {args}, kwargs: {kwargs}"

        logging.info(f"Se llamó a la función '{nombre_funcion}' con {argumentos}")

        inicio_tiempo = time.time()
        resultado = self.funcion(*args, **kwargs)
        fin_tiempo = time.time()

        tiempo_ejecucion = fin_tiempo - inicio_tiempo
        logging.info(f"La función '{nombre_funcion}' retornó {resultado} en {tiempo_ejecucion:.4f} segundos")
        logging.info(f"La función '{nombre_funcion}' ha sido llamada {self.contador_llamadas} veces")

        return resultado

# Decorador de clase
def decorador_avanzado(funcion):
    """
    Función que aplica el decorador basado en clase a una función dada.
    """
    return DecoradorAvanzado(funcion)

@decorador_avanzado
def calcular_suma(*numeros):
    """
    Calcula la suma de una lista de números.
    """
    time.sleep(1)  # Simula una operación que tarda 1 segundo
    return sum(numeros)

@decorador_avanzado
def saludar(nombre, saludo="Hola"):
    """
    Saluda a una persona con un saludo personalizado.
    """
    time.sleep(0.5)  # Simula una operación que tarda 0.5 segundos
    return f"{saludo}, {nombre}!"

if __name__ == "__main__":
    # Llamadas a la función 'calcular_suma'
    print(calcular_suma(1, 2, 3, 4, 5))
    print(calcular_suma(10, 20, 30))

    # Llamadas a la función 'saludar'
    print(saludar("Juan"))
    print(saludar("María", saludo="Buenos días"))
