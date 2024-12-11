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


# Simulando la atención en un banco
class Banco:
    def __init__(self):
        self.fila = Cola()  # Usamos una cola para representar la fila de clientes
    
    def llegar_cliente(self, cliente):
        """Un cliente llega al banco y se agrega a la cola."""
        print(f"Cliente {cliente} ha llegado al banco.")
        self.fila.enqueue(cliente)
    
    def atender_cliente(self):
        """Se atiende al primer cliente en la fila."""
        if not self.fila.is_empty():
            cliente = self.fila.dequeue()
            print(f"Atendiendo a {cliente}.")
        else:
            print("No hay clientes en la fila.")
    
    def mostrar_fila(self):
        """Muestra la fila actual de clientes."""
        print(f"Fila de clientes: {self.fila}")


# Ejemplo de uso
banco = Banco()

# Los clientes llegan al banco
banco.llegar_cliente("Cliente 1")
banco.llegar_cliente("Cliente 2")
banco.llegar_cliente("Cliente 3")

# Mostrar la fila
banco.mostrar_fila()

# Atender a los clientes en orden
banco.atender_cliente()  # Atendemos al Cliente 1
banco.mostrar_fila()

banco.atender_cliente()  # Atendemos al Cliente 2
banco.mostrar_fila()

banco.atender_cliente()  # Atendemos al Cliente 3
banco.mostrar_fila()

# Intentamos atender a alguien más, pero la fila está vacía
banco.atender_cliente()


