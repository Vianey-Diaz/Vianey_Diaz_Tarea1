class NodoArbol:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        nuevo_nodo = NodoArbol(valor)
        if not self.raiz:
            self.raiz = nuevo_nodo
        else:
            self._insertar_recursivo(self.raiz, nuevo_nodo)

    def _insertar_recursivo(self, actual, nuevo_nodo):
        if nuevo_nodo.valor < actual.valor:
            if actual.izquierdo is None:
                actual.izquierdo = nuevo_nodo
            else:
                self._insertar_recursivo(actual.izquierdo, nuevo_nodo)
        else:
            if actual.derecho is None:
                actual.derecho = nuevo_nodo
            else:
                self._insertar_recursivo(actual.derecho, nuevo_nodo)

    def inorder(self):
        resultado = []
        self._inorder_recursivo(self.raiz, resultado)
        return resultado

    def _inorder_recursivo(self, nodo, resultado):
        if nodo is not None:
            self._inorder_recursivo(nodo.izquierdo, resultado)
            resultado.append(nodo.valor)
            self._inorder_recursivo(nodo.derecho, resultado)

    def buscar(self, valor):
        return self._buscar_recursivo(self.raiz, valor)

    def _buscar_recursivo(self, actual, valor):
        if actual is None:
            return False
        if actual.valor == valor:
            return True
        elif valor < actual.valor:
            return self._buscar_recursivo(actual.izquierdo, valor)
        else:
            return self._buscar_recursivo(actual.derecho, valor)

# Ejemplo de uso
if __name__ == "__main__":
    arbol = ArbolBinario()
    
    # Insertar elementos
    arbol.insertar(50)
    arbol.insertar(30)
    arbol.insertar(70)
    arbol.insertar(20)
    arbol.insertar(40)
    arbol.insertar(60)
    arbol.insertar(80)
    
    # Recorrer el árbol en orden
    print("Recorrido Inorder:", arbol.inorder())
    
    # Buscar elementos
    print("Buscar 40:", arbol.buscar(40))  # Debe devolver True
    print("Buscar 90:", arbol.buscar(90))  # Debe devolver False
