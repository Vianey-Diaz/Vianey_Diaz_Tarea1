def quicksort(arr):  
    if len(arr) <= 1:  
        return arr  # Base case: arrays with 0 or 1 element are already sorted  
    else:  
        pivot = arr[len(arr) // 2]  # Elegir el pivote (en este caso, el elemento del medio)  
        left = [x for x in arr if x < pivot]  # Sublista de elementos menores que el pivote  
        middle = [x for x in arr if x == pivot]  # Sublista de elementos iguales al pivote  
        right = [x for x in arr if x > pivot]  # Sublista de elementos mayores que el pivote  
        return quicksort(left) + middle + quicksort(right)  # Recursión y combinación de resultados  

# Ejemplo de uso  
data = [38, 27, 43, 3, 9, 82, 10]  
sorted_data = quicksort(data)  
print("Arreglo ordenado es:", sorted_data)