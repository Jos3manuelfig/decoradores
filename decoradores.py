# def decorador(func):
#
#     def envoltura():
#          print("antes d ela funcion")
#          func()
#          print("despues de la fucnion")
#
#     return envoltura
#
#
# @decorador
# def saludar():
#     print("Hola")
#
import time
import functools

# Versión con caché
@functools.lru_cache(maxsize=128)
def fibonacci_cached(n):
    """Calcula el n-ésimo número de Fibonacci de forma recursiva con caché."""
    if n < 2:
        return n
    return fibonacci_cached(n-1) + fibonacci_cached(n-2)

# Versión sin caché
def fibonacci_no_cache(n):
    """Calcula el n-ésimo número de Fibonacci de forma recursiva sin caché."""
    if n < 2:
        return n
    return fibonacci_no_cache(n-1) + fibonacci_no_cache(n-2)

# Medir el tiempo de la versión con caché
inicio = time.time()
print(fibonacci_cached(25))  # Calcula y almacena en caché
fin = time.time()
print(f"Tiempo con caché: {fin - inicio:.6f} segundos")

# Limpiar la caché
fibonacci_cached.cache_clear()

# Medir el tiempo de la versión sin caché
inicio = time.time()
print(fibonacci_no_cache(25))  # Calcula sin caché
fin = time.time()
print(f"Tiempo sin caché: {fin - inicio:.6f} segundos")
