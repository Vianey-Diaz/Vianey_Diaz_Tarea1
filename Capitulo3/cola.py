from collections import deque

def crear_cola():
    return deque(range(1, 101))  # Crear una cola con los números del 1 al 100

def procesar_cola(cola):
    pares = [num for num in cola if num % 2 == 0]
    impares = [num for num in cola if num % 2 != 0]

    # Calcular cantidad, suma y promedio de pares
    cantidad_pares = len(pares)
    suma_pares = sum(pares)
    promedio_pares = suma_pares / cantidad_pares if cantidad_pares > 0 else 0

    # Calcular cantidad, suma y promedio de impares
    cantidad_impares = len(impares)
    suma_impares = sum(impares)
    promedio_impares = suma_impares / cantidad_impares if cantidad_impares > 0 else 0

    # Mostrar resultados
    print("Pares:")
    print(f"Cantidad: {cantidad_pares}, Suma: {suma_pares}, Promedio: {promedio_pares:.2f}")
    print("Impares:")
    print(f"Cantidad: {cantidad_impares}, Suma: {suma_impares}, Promedio: {promedio_impares:.2f}")

cola=crear_cola()
procesar_cola(cola)
