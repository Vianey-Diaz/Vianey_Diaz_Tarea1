class Pila:
    def __init__(self):
        self.elementos = []  # Lista para almacenar los elementos de la pila

    def push(self, elemento):
        """Agrega un elemento a la pila."""
        self.elementos.append(elemento)

    def pop(self):
        """Elimina y devuelve el último elemento de la pila. 
        Si la pila está vacía, devuelve None."""
        if not self.esta_vacia():
            return self.elementos.pop()
        return None

    def peek(self):
        """Devuelve el último elemento de la pila sin eliminarlo.
        Si la pila está vacía, devuelve None."""
        if not self.esta_vacia():
            return self.elementos[-1]
        return None

    def esta_vacia(self):
        """Devuelve True si la pila está vacía, de lo contrario False."""
        return len(self.elementos) == 0

# Pruebas
pila = Pila()

# Agregar elementos
pila.push(10)
pila.push(20)
pila.push(30)
print("Pila después de agregar elementos:", pila.elementos)

# Ver el último elemento
print("Elemento en la cima (peek):", pila.peek())

# Eliminar elementos
print("Elemento eliminado (pop):", pila.pop())
print("Pila después de eliminar un elemento:", pila.elementos)

# Verificar si está vacía
print("¿La pila está vacía?", pila.esta_vacia())

# Eliminar todos los elementos
pila.pop()
pila.pop()
print("¿La pila está vacía después de eliminar todo?", pila.esta_vacia())
