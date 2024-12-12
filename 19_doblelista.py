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

# Función para fusionar dos listas enlazadas ordenadas
def fusionar_listas(lista1, lista2):
    # Nodo temporal para construir la nueva lista
    nodo_dummy = Nodo(0)
    actual = nodo_dummy

    # Punteros para recorrer ambas listas
    actual1 = lista1.cabeza
    actual2 = lista2.cabeza

    # Fusionar mientras ambas listas tengan nodos
    while actual1 and actual2:
        if actual1.valor < actual2.valor:
            actual.siguiente = actual1
            actual1 = actual1.siguiente
        else:
            actual.siguiente = actual2
            actual2 = actual2.siguiente
        actual = actual.siguiente

    # Agregar los nodos restantes, si los hay
    if actual1:
        actual.siguiente = actual1
    if actual2:
        actual.siguiente = actual2

    # Crear una nueva lista enlazada para la fusión
    lista_fusionada = ListaEnlazada()
    lista_fusionada.cabeza = nodo_dummy.siguiente
    return lista_fusionada

# Ejemplo de uso
if __name__ == "__main__":
    lista1 = ListaEnlazada()
    lista2 = ListaEnlazada()

    # Agregar elementos a la primera lista
    lista1.agregar_al_final(1)
    lista1.agregar_al_final(3)
    lista1.agregar_al_final(5)

    # Agregar elementos a la segunda lista
    lista2.agregar_al_final(2)
    lista2.agregar_al_final(4)
    lista2.agregar_al_final(6)

    print("Lista 1:")
    lista1.mostrar()

    print("Lista 2:")
    lista2.mostrar()

    # Fusionar las listas
    lista_fusionada = fusionar_listas(lista1, lista2)
    print("Lista fusionada:")
    lista_fusionada.mostrar()
