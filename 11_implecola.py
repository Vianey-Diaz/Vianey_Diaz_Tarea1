class Cola:
    def __init__(self):
        self.items = []  # Usaremos una lista para guardar los elementos
    
    def enqueue(self, item):
        self.items.append(item)  # Agrega el elemento al final de la lista
    
    def dequeue(self):
        if not self.is_empty():  # Verificar si la cola no está vacía
            return self.items.pop(0)  # Quitar y devolver el primer elemento
        else:
            raise IndexError("La cola está vacía.")  # Error si no hay elementos
    
    def peek(self):
        if not self.is_empty():  # Verificar si la cola no está vacía
            return self.items[0]  # Devolver el primer elemento sin quitarlo
        else:
            raise IndexError("La cola está vacía.")  # Error si no hay elementos
    
    def is_empty(self):
        return len(self.items) == 0  # Devuelve True si la cola no tiene elementos
    
    def __str__(self):
        return " -> ".join(map(str, self.items))  # Representación en cadena


# Ejemplo de uso
cola = Cola()

# Agregar elementos a la cola
cola.enqueue(10)
cola.enqueue(20)
cola.enqueue(30)

print("Cola después de agregar elementos:", cola)

# Ver el primer elemento
print("Primer elemento:", cola.peek())

# Remover elementos de la cola
print("Elemento removido:", cola.dequeue())
print("Cola después de remover un elemento:", cola)

# Verificar si la cola está vacía
print("¿La cola está vacía?", cola.is_empty())


