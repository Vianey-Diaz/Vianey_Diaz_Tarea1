class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_al_final(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def mostrar(self):
        actual = self.cabeza
        elementos = []
        while actual:
            elementos.append(actual.valor)
            actual = actual.siguiente
        print("Lista:", " -> ".join(map(str, elementos)))

    # Método para invertir la lista enlazada
    def invertir(self):
        anterior = None
        actual = self.cabeza
        while actual:
            siguiente = actual.siguiente  # Guardar el siguiente nodo
            actual.siguiente = anterior  # Revertir el enlace
            anterior = actual  # Avanzar el puntero anterior
            actual = siguiente  # Avanzar el puntero actual
        self.cabeza = anterior  # Actualizar la cabeza al nuevo primer nodo

# Ejemplo de uso
if __name__ == "__main__":
    lista = ListaEnlazada()
    
    # Agregar elementos
    lista.agregar_al_final(1)
    lista.agregar_al_final(2)
    lista.agregar_al_final(3)
    lista.agregar_al_final(4)
    print("Lista original:")
    lista.mostrar()
    
    # Invertir la lista
    lista.invertir()
    print("Lista invertida:")
    lista.mostrar()
