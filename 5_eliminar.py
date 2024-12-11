def eliminar_duplicados(arreglo):
    return list(set(arreglo))  # Convertir el arreglo en un conjunto y luego de nuevo a lista

# Ejemplo de uso
arreglo = [1, 2, 2, 3, 4, 4, 5, 6, 6, 6]
nuevo_arreglo = eliminar_duplicados(arreglo)
print("Arreglo original:", arreglo)
print("Arreglo sin duplicados:", nuevo_arreglo)