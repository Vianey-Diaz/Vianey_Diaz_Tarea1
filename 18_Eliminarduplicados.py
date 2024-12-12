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

    # Método para eliminar nodos duplicados
    def eliminar_duplicados(self):
        if not self.cabeza:
            return  # Lista vacía, nada que hacer
        
        valores = set()  # Usaremos un conjunto para rastrear valores únicos
        actual = self.cabeza
        valores.add(actual.valor)  # Agregar el primer valor al conjunto
        
        while actual.siguiente:
            if actual.siguiente.valor in valores:
                # Si el valor ya está en el conjunto, eliminar el nodo duplicado
                actual.siguiente = actual.siguiente.siguiente
            else:
                # Si es un valor único, agregar al conjunto
                valores.add(actual.siguiente.valor)
                actual = actual.siguiente

# Ejemplo de uso
if __name__ == "__main__":
    lista = ListaEnlazada()
    
    # Agregar elementos con duplicados
    lista.agregar_al_final(1)
    lista.agregar_al_final(2)
    lista.agregar_al_final(3)
    lista.agregar_al_final(2)
    lista.agregar_al_final(4)
    lista.agregar_al_final(3)
    print("Lista original:")
    lista.mostrar()
    
    # Eliminar duplicados
    lista.eliminar_duplicados()
    print("Lista después de eliminar duplicados:")
    lista.mostrar()
