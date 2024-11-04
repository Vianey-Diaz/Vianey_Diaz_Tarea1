class Stack(object):
    def __init__(self, max):  # Constructor
        self.__stackList = [None] * max  # The stack stored as a list
        self.__top = -1  # No items initially

    def push(self, item):  # Insert item at top of stack
        if self.isFull():
            raise Exception("Desbordamiento de pila: no se puede empujar a una pila completa")
        self.__top += 1  # Advance the pointer
        self.__stackList[self.__top] = item  # Store item

    def pop(self):  # Remove top item from stack
        if self.isEmpty():
            raise Exception("Desbordamiento de pila: no se puede extraer de una pila vacía")
        top = self.__stackList[self.__top]  # Top item
        self.__stackList[self.__top] = None  # Remove item reference
        self.__top -= 1  # Decrease the pointer
        return top  # Return top item

    def peek(self):  # Return top item
        if not self.isEmpty():  # If stack is not empty
            return self.__stackList[self.__top]  # Return the top item

    def isEmpty(self):  # Check if stack is empty
        return self.__top < 0

    def isFull(self):  # Check if stack is full
        return self.__top >= len(self.__stackList) - 1

    def __len__(self):  # Return # of items on stack
        return self.__top + 1

    def __str__(self):  # Convert stack to string
        ans = "["  # Start with left bracket
        for i in range(self.__top + 1):  # Loop through current items
            if len(ans) > 1:  # Except next to left bracket,
                ans += ", "  # separate items with comma
            ans += str(self.__stackList[i])  # Add string form of item
        ans += "]"  # Close with right bracket
        return ans

def test_stack():
    stack_size = 6
    stack = Stack(stack_size)

    # Llenar la pila
    try:
        for i in range(stack_size + 1 ):
            stack.push(i)
        print("Pila después de llenarla:", stack)
    except Exception as e:
        print("Error al llenar la pila:", e)

    # Intentar agregar un elemento adicional
    try:
        stack.push(99)
    except Exception as e:
        print("Excepción esperada al intentar agregar a una pila llena:", e)

    # Vaciar la pila
    try:
        while not stack.isEmpty():
            print("Elemento eliminado:", stack.pop())
        print("Pila después de vaciarla:", stack)
    except Exception as e:
        print("Error al vaciar la pila:", e)

    # Intentar quitar un elemento de una pila vacía
    try:
        stack.pop()
    except Exception as e:
        print("Excepción esperada al intentar quitar de una pila vacía:", e)

print("\nEjercicio 1 del capitulo 4, excepciones")
test_stack()



def is_palindrome(input_string):
    # Crear una pila para contener caracteres
    stack = Stack(len(input_string))
    
    # Normalizar la cadena de entrada: eliminar los caracteres no alfabéticos y convertirlos a minúsculas
    normalized_string = ''.join(char.lower() for char in input_string if char.isalpha())
    
    # Empuje todos los caracteres de la cadena normalizada a la pila
    for char in normalized_string:
        stack.push(char)
    
    # Construya la versión invertida haciendo estallar la pila
    reversed_string = ''
    while not stack.isEmpty():
        reversed_string += stack.pop()
    
    # Comprueba si la cadena normalizada es igual a su versión invertida
    return normalized_string == reversed_string


# Test de funcionamiento
print("\nEjercicio 2 capitulo 4, palindromo")
test_string = "A man, a plan, a canal, Panama."
if is_palindrome(test_string):
    print(f'"{test_string}" es un palíndromo.')
else:
    print(f'"{test_string}" no es un palíndromo.')


class Deque:
    def __init__(self, max_size):
        self.__deque = [None] * max_size
        self.__max_size = max_size
        self.__front = 0
        self.__rear = -1
        self.__size = 0

    def insertLeft(self, item):
        if self.isFull():
            raise Exception("Desbordamiento de deque: no se puede insertar en un deque completo")
        self.__front = (self.__front - 1) % self.__max_size
        self.__deque[self.__front] = item
        self.__size += 1

    def insertRight(self, item):
        if self.isFull():
            raise Exception("Desbordamiento de deque: no se puede insertar en un deque completo")
        self.__rear = (self.__rear + 1) % self.__max_size
        self.__deque[self.__rear] = item
        self.__size += 1

    def removeLeft(self):
        if self.isEmpty():
            raise Exception("Desbordamiento de deque: no se puede quitar de un deque vacío")
        item = self.__deque[self.__front]
        self.__deque[self.__front] = None
        self.__front = (self.__front + 1) % self.__max_size
        self.__size -= 1
        return item

    def removeRight(self):
        if self.isEmpty():
            raise Exception("Desbordamiento de deque: no se puede quitar de un deque vacío")
        item = self.__deque[self.__rear]
        self.__deque[self.__rear] = None
        self.__rear = (self.__rear - 1) % self.__max_size
        self.__size -= 1
        return item

    def peekLeft(self):
        if self.isEmpty():
            raise Exception("Deque está vacío: no se puede asomar")
        return self.__deque[self.__front]

    def peekRight(self):
        if self.isEmpty():
            raise Exception("Deque está vacío: no se puede asomar")
        return self.__deque[self.__rear]

    def isEmpty(self):
        return self.__size == 0

    def isFull(self):
        return self.__size == self.__max_size

    def __str__(self):
        return str(self.__deque)

# uso 
print("\nEjercicio 3 capitulo 4")
deque = Deque(5)
deque.insertRight(1)
deque.insertRight(2)
deque.insertLeft(3)
deque.insertLeft(4)
deque.insertRight(5)

print("Deque después de inserciones:", deque)

print("Elemento removido desde la izquierda:", deque.removeLeft())
print("Elemento removido desde la derecha:", deque.removeRight())

print("Elemento en el frente:", deque.peekLeft())
print("Elemento en la parte trasera:", deque.peekRight())

print("Deque final:", deque)

class DequeStack:
    def __init__(self, max_size):
        self.__deque = Deque(max_size)

    def push(self, item):
        if self.__deque.isFull():
            raise Exception("Desbordamiento de pila: no se puede empujar a una pila completa")
        self.__deque.insertRight(item)

    def pop(self):
        if self.__deque.isEmpty():
            raise Exception("Desbordamiento de pila: no se puede extraer de una pila vacía")
        return self.__deque.removeRight()

    def peek(self):
        if self.__deque.isEmpty():
            raise Exception("La pila está vacía: no se puede mirar")
        return self.__deque.peekRight()

    def isEmpty(self):
        return self.__deque.isEmpty()

    def isFull(self):
        return self.__deque.isFull()

    def __len__(self):
        return self.__deque.__size

    def __str__(self):
        return str(self.__deque)

def test_deque_stack():
    stack_size = 6
    stack = DequeStack(stack_size)

    # Llenar la pila
    try:
        for i in range(stack_size + 1):
            stack.push(i)
        print("Pila después de llenarla:", stack)
    except Exception as e:
        print("Error al llenar la pila:", e)

    # Intentar agregar un elemento adicional
    try:
        stack.push(99)
    except Exception as e:
        print("Excepción esperada al intentar agregar a una pila llena:", e)

    # Vaciar la pila
    try:
        while not stack.isEmpty():
            print("Elemento eliminado:", stack.pop())
        print("Pila después de vaciarla:", stack)
    except Exception as e:
        print("Error al vaciar la pila:", e)

    # Intentar quitar un elemento de una pila vacía
    try:
        stack.pop()
    except Exception as e:
        print("Excepción esperada al intentar quitar de una pila vacía:", e)

print("\nEjercicio 4 capitulo 4")
test_deque_stack()
