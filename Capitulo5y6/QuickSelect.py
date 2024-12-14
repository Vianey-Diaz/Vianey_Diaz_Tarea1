import random  

def quickselect(arr, k):  
    if len(arr) == 1:  # Caso base  
        return arr[0]  

    pivot = random.choice(arr)  # Elegir un pivote al azar  
    lows = [x for x in arr if x < pivot]  # Elementos menores que el pivote  
    highs = [x for x in arr if x > pivot]  # Elementos mayores que el pivote  
    pivots = [x for x in arr if x == pivot]  # Elementos iguales al pivote  

    k_index = len(lows)  # Índice del pivote en el arreglo ordenado  

    if k < k_index:  # Está en la parte izquierda  
        return quickselect(lows, k)  # Buscar en menores  
    elif k < k_index + len(pivots):  # Corresponde a uno de los pivotes  
        return pivots[0]  # Devolver el pivote  
    else:  # Está en la parte derecha  
        return quickselect(highs, k - k_index - len(pivots))  # Ajustar k y buscar en mayores  

# Ejemplo de uso  
data = [38, 27, 43, 3, 9, 82, 10]  
k = 3  # Queremos encontrar el 4to elemento más pequeño (índice 3)  
result = quickselect(data, k)  
print(f"El {k + 1}º elemento más pequeño es: {result}")