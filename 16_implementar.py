class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar_al_final(self, valor):
        nuevo_nodo = Nodo(valor)
        if not self.cabeza:  # Si la lista está vacía
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:  # Recorrer hasta el último nodo
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo  # Agregar el nuevo nodo al final

    def eliminar(self, valor):
        if not self.cabeza:  # Si la lista está vacía
            print("La lista está vacía. No se puede eliminar.")
            return

        # Si el nodo a eliminar es la cabeza
        if self.cabeza.valor == valor:
            self.cabeza = self.cabeza.siguiente
            return

        # Buscar el nodo a eliminar
        actual = self.cabeza
        while actual.siguiente and actual.siguiente.valor != valor:
            actual = actual.siguiente

        if actual.siguiente:  # Si se encontró el nodo
            actual.siguiente = actual.siguiente.siguiente
        else:
            print(f"El valor {valor} no está en la lista.")

    def buscar(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                return True  # Valor encontrado
            actual = actual.siguiente
        return False  # Valor no encontrado

    def mostrar(self):
        actual = self.cabeza
        elementos = []
        while actual:
            elementos.append(actual.valor)
            actual = actual.siguiente
        print("Lista:", " -> ".join(map(str, elementos)))

# Ejemplo de uso
if __name__ == "__main__":
    lista = ListaEnlazada()
    
    # Agregar elementos
    lista.agregar_al_final(10)
    lista.agregar_al_final(20)
    lista.agregar_al_final(30)
    print("Después de agregar elementos:")
    lista.mostrar()
    
    # Buscar elementos
    print("Buscar 20:", lista.buscar(20))  # True
    print("Buscar 40:", lista.buscar(40))  # False
    
    # Eliminar elementos
    lista.eliminar(20)
    print("Después de eliminar 20:")
    lista.mostrar()
    
    lista.eliminar(40)  # No está en la lista
    lista.mostrar()
