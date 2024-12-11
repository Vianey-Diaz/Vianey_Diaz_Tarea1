class ColaCircular:
    def __init__(self, tamaño):
        self.tamaño = tamaño  # Tamaño máximo de la cola
        self.cola = [None] * tamaño  # Lista que representa la cola
        self.front = -1  # Índice del primer elemento
        self.rear = -1   # Índice del último elemento
    
    def is_empty(self):
        return self.front == -1  # La cola está vacía si el front es -1
    
    def is_full(self):
        # La cola está llena si el siguiente espacio de rear es igual a front
        return (self.rear + 1) % self.tamaño == self.front
    
    def enqueue(self, item):
        if self.is_full():
            print("La cola está llena. No se puede agregar el elemento.")
        else:
            # Si la cola está vacía, inicializamos front y rear
            if self.front == -1:
                self.front = 0
            self.rear = (self.rear + 1) % self.tamaño  # Mueve rear circularmente
            self.cola[self.rear] = item
            print(f"Elemento {item} agregado.")
    
    def dequeue(self):
        if self.is_empty():
            print("La cola está vacía. No se puede eliminar ningún elemento.")
        else:
            item = self.cola[self.front]
            # Si hay un solo elemento, reiniciamos la cola
            if self.front == self.rear:
                self.front = self.rear = -1
            else:
                self.front = (self.front + 1) % self.tamaño  # Mueve front circularmente
            print(f"Elemento {item} eliminado.")
            return item
    
    def peek(self):
        if self.is_empty():
            print("La cola está vacía.")
        else:
            return self.cola[self.front]  # Devuelve el primer elemento sin eliminarlo
    
    def mostrar_cola(self):
        if self.is_empty():
            print("La cola está vacía.")
        else:
            # Mostrar los elementos de la cola en orden
            i = self.front
            while i != self.rear:
                print(self.cola[i], end=" -> ")
                i = (i + 1) % self.tamaño
            print(self.cola[self.rear])

# Ejemplo de uso
cola_circular = ColaCircular(5)

# Agregar elementos
cola_circular.enqueue(10)
cola_circular.enqueue(20)
cola_circular.enqueue(30)
cola_circular.enqueue(40)
cola_circular.enqueue(50)

# Intentar agregar un elemento cuando la cola está llena
cola_circular.enqueue(60)

# Mostrar la cola
cola_circular.mostrar_cola()

# Eliminar elementos
cola_circular.dequeue()
cola_circular.dequeue()

# Mostrar la cola después de eliminar algunos elementos
cola_circular.mostrar_cola()

# Agregar más elementos
cola_circular.enqueue(60)
cola_circular.enqueue(70)

# Mostrar la cola final
cola_circular.mostrar_cola()
