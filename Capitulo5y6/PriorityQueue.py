class Node:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.next = None

    def getData(self):
        return self.data

    def getPriority(self):
        return self.priority

    def getNext(self):
        return self.next

    def setNext(self, next_node):
        self.next = next_node

class PriorityQueue:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head is None

    def insert(self, data, priority):
        new_node = Node(data, priority)
        if self.isEmpty() or self.head.getPriority() > priority:
            new_node.setNext(self.head)
            self.head = new_node
        else:
            current = self.head
            while current.getNext() is not None and current.getNext().getPriority() <= priority:
                current = current.getNext()
            new_node.setNext(current.getNext())
            current.setNext(new_node)

    def remove(self):
        if self.isEmpty():
            raise IndexError("Eliminar de la cola de prioridad vacía")
        removed_node = self.head
        self.head = self.head.getNext()
        return removed_node.getData()

    def peek(self):
        if self.isEmpty():
            raise IndexError("Echar un vistazo desde la cola de prioridad vacía")
        return self.head.getData()

    def __str__(self):
        result = []
        current = self.head
        while current is not None:
            result.append(f"({current.getData()}, {current.getPriority()})")
            current = current.getNext()
        return " -> ".join(result)

#uso
pq = PriorityQueue()
pq.insert("tarea1", 3)
pq.insert("tarea2", 1)
pq.insert("tarea3", 2)

print("Priority Queue:")
print(pq)  # Debería imprimir (tarea2, 1) -> (tarea3, 2) -> (tarea1, 3)

print("\nEliminar elemento de mayor prioridad:")
print(pq.remove())  # Debería imprimir tarea2

print("\nCola de prioridad después de la eliminación:")
print(pq)  # Debería imprimir (tarea3, 2) -> (tarea1, 3)
