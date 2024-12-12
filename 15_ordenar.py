from collections import deque

# Función para encontrar el mínimo en la cola actual
def find_and_remove_min(queue):
    min_val = float('inf')
    size = len(queue)
    
    # Encontrar el mínimo y mover elementos de vuelta
    for _ in range(size):
        val = queue.popleft()
        if val < min_val:
            min_val = val
        queue.append(val)
    
    # Remover una instancia del mínimo encontrado
    for _ in range(size):
        val = queue.popleft()
        if val != min_val:
            queue.append(val)
        else:
            break  # Remover solo una instancia del mínimo
    
    return min_val

# Función para ordenar la cola usando solo operaciones de cola
def sort_queue(queue):
    sorted_queue = deque()
    
    while queue:
        # Encontrar el mínimo y añadirlo a la cola ordenada
        min_val = find_and_remove_min(queue)
        sorted_queue.append(min_val)
    
    # Transferir los elementos de vuelta a la cola original
    while sorted_queue:
        queue.append(sorted_queue.popleft())

# Ejemplo de uso
if __name__ == "__main__":
    # Crear una cola
    q = deque([3, 1, 4, 1, 5, 9, 2, 6, 5])
    print("Cola original:", list(q))
    
    # Ordenar la cola
    sort_queue(q)
    print("Cola ordenada:", list(q))
