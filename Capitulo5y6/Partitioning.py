# Ejemplo de uso del método partition con números en Python

# Cadena de ejemplo
cadena_numeros = "123456789"

# Usar el método partition
partes = cadena_numeros.partition("4")

# Mostrar los resultados
print("Antes del separador:", partes[0])
print("Separador:", partes[1])
print("Después del separador:", partes[2])

# Lista de ejemplo
mi_lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Definir el pivote
pivote = 5

# Encontrar el índice del pivote
indice_pivote = mi_lista.index(pivote)

# Dividir la lista en dos partes usando el índice del pivote
parte1 = mi_lista[:indice_pivote]
parte2 = mi_lista[indice_pivote+1:]

# Mostrar los resultados
print("Parte 1:", parte1)
print("Pivote:", pivote)
print("Parte 2:", parte2)

# Crear listas de números pares e impares usando particiones (list comprehension)
pares = [num for num in range(1, 101) if num % 2 == 0]  # Almacenará los números pares
impares = [num for num in range(1, 101) if num % 2 != 0]  # Almacenará los números impares

# Calcular la suma de pares e impares
suma_pares = sum(pares)  # Suma de los números pares
suma_impares = sum(impares)  # Suma de los números impares

# Calcular el promedio de pares e impares
promedio_pares = suma_pares / len(pares)  # Promedio de los números pares
promedio_impares = suma_impares / len(impares)  # Promedio de los números impares

# Calcular el porcentaje de pares e impares
porcentaje_pares = (len(pares) / 100) * 100  # Porcentaje de números pares
porcentaje_impares = (len(impares) / 100) * 100  # Porcentaje de números impares

# Imprimir resultados
print(f"Números pares: {pares}")  # Mostrar la lista de números pares
print(f"Suma de números pares: {suma_pares}")  # Mostrar la suma de números pares
print(f"Promedio de números pares: {promedio_pares:.2f}")  # Mostrar el promedio de números pares
print(f"Porcentaje de números pares: {porcentaje_pares}%")  # Mostrar el porcentaje de números pares

print(f"Números impares: {impares}")  # Mostrar la lista de números impares
print(f"Suma de números impares: {suma_impares}")  # Mostrar la suma de números impares
print(f"Promedio de números impares: {promedio_impares:.2f}")  # Mostrar el promedio de números impares
print(f"Porcentaje de números impares: {porcentaje_impares}%")  # Mostrar el porcentaje de números impares