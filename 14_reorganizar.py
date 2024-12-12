from collections import deque

class Cola:
    def __init__(self):
        self.cola = deque()
    
    def enqueue(self, item):
        self.cola.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.cola.popleft()
        return None
    
    def is_empty(self):
        return len(self.cola) == 0
    
    def mostrar(self):
        return list(self.cola)

# Reorganizar la cola
def reorganizar_cola(cola):
    pares = deque()
    impares = deque()
    
    # Separar pares e impares
    while not cola.is_empty():
        num = cola.dequeue()
        if num % 2 == 0:
            pares.append(num)
        else:
            impares.append(num)
    
    # Reunir los pares al principio y los impares al final
    while pares:
        cola.enqueue(pares.popleft())
    
    while impares:
        cola.enqueue(impares.popleft())

# Ejemplo de uso
cola = Cola()
cola.enqueue(1)
cola.enqueue(2)
cola.enqueue(3)
cola.enqueue(4)
cola.enqueue(5)

print("Cola original:", cola.mostrar())
reorganizar_cola(cola)
print("Cola reorganizada:", cola.mostrar())
