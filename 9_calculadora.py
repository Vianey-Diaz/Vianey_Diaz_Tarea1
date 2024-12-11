class Pila:
    def __init__(self):
        self.elementos = []

    def push(self, elemento):
        self.elementos.append(elemento)

    def pop(self):
        if not self.esta_vacia():
            return self.elementos.pop()
        return None

    def esta_vacia(self):
        return len(self.elementos) == 0


def calcular(lista):
    pila = Pila()

    for elemento in lista:
        if isinstance(elemento, (int, float)):  # Si es un número, apilarlo
            pila.push(elemento)
        elif elemento in '+-*/':  # Si es un operador, realizar la operación
            # Sacar los dos últimos números de la pila
            b = pila.pop()
            a = pila.pop()
            if a is None or b is None:
                raise ValueError("No hay suficientes operandos para la operación.")
            
            # Realizar la operación correspondiente
            if elemento == '+':
                resultado = a + b
            elif elemento == '-':
                resultado = a - b
            elif elemento == '*':
                resultado = a * b
            elif elemento == '/':
                if b == 0:
                    raise ZeroDivisionError("División entre cero.")
                resultado = a / b
            
            # Apilar el resultado
            pila.push(resultado)
        else:
            raise ValueError(f"Elemento no reconocido: {elemento}")

    # El resultado final debe estar en la cima de la pila
    if pila.esta_vacia() or len(pila.elementos) != 1:
        raise ValueError("La lista no está balanceada o hay operadores sobrantes.")
    return pila.pop()


# Ejemplo de uso
expresion = [3, 4, 2, '*', '+', 5, '/']  # (3 + (4 * 2)) / 5
resultado = calcular(expresion)
print("Resultado:", resultado)
