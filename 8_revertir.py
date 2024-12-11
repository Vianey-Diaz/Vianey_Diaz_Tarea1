class Pila:
    def __init__(self):
        self.elementos = []  # Lista para almacenar elementos de la pila

    def push(self, elemento):
        self.elementos.append(elemento)

    def pop(self):
        if not self.esta_vacia():
            return self.elementos.pop()
        return None

    def esta_vacia(self):
        return len(self.elementos) == 0


def invertir_cadena(cadena):
    pila = Pila()

    # Apilar cada carácter de la cadena
    for char in cadena:
        pila.push(char)

    # Desapilar los caracteres y construir la cadena invertida
    cadena_invertida = ""
    while not pila.esta_vacia():
        cadena_invertida += pila.pop()

    return cadena_invertida


# Ejemplo de uso
cadena_original = "Hola, mundo!"
cadena_invertida = invertir_cadena(cadena_original)
print("Cadena original:", cadena_original)
print("Cadena invertida:", cadena_invertida)
