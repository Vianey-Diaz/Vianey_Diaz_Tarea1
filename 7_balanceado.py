class Pila:
    def __init__(self):
        self.elementos = []

    def push(self, elemento):
        self.elementos.append(elemento)

    def pop(self):
        if not self.esta_vacia():
            return self.elementos.pop()
        return None

    def peek(self):
        if not self.esta_vacia():
            return self.elementos[-1]
        return None

    def esta_vacia(self):
        return len(self.elementos) == 0


def verificar_parentesis_balanceados(cadena):
    pila = Pila()
    pares = {')': '(', '}': '{', ']': '['}  # Mapa de paréntesis de cierre y apertura

    for char in cadena:
        if char in '({[':  # Si es un paréntesis de apertura, se apila
            pila.push(char)
        elif char in ')}]':  # Si es un paréntesis de cierre
            if pila.esta_vacia() or pila.pop() != pares[char]:
                return False  # No hay un paréntesis de apertura correspondiente

    return pila.esta_vacia()  # Si la pila está vacía, los paréntesis están balanceados


# Ejemplos de prueba
cadenas = [
    "()",      # Balanceado
    "([])",    # Balanceado
    "{[()]}",  # Balanceado
    "(",       # No balanceado
    "([)]",    # No balanceado
    "{[}"      # No balanceado
]

for cadena in cadenas:
    print(f"'{cadena}':", "Balanceado" if verificar_parentesis_balanceados(cadena) else "No balanceado")
