class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setNext(self, next_node):
        self.next = next_node

class LinkedList:
    def __init__(self):
        self.head = None

    def getFirst(self):
        return self.head

    def add(self, data):
        new_node = Node(data)
        new_node.setNext(self.head)
        self.head = new_node

    def __iter__(self):
        next = self.getFirst()
        while next is not None:
            yield next.getData()
            next = next.getNext()

    def traverse(self, func=print):
        for data in self:
            func(data)

    def __len__(self):
        return sum(1 for _ in self)

    def __str__(self):
        result = "[" + " > ".join(str(data) for data in self) + "]"
        return result

# Crear una lista enlazada y añadir algunos elementos
ll = LinkedList()
ll.add(10)
ll.add(20)
ll.add(30)

# Probar los métodos
print("Traverse:")
ll.traverse()  # Debería imprimir 30, 20, 10

print("\nLongitud de la lista:", len(ll))  # Debería imprimir 3

print("\nRepresentación de cadenas", str(ll))  # Debería imprimir [30 > 20 > 10]
