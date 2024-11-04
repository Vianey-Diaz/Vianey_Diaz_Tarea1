class Array:
    def __init__(self, a):
        self.__a = a
        self.__nItems = len(a)

    def swap(self, i, j):
        self.__a[i], self.__a[j] = self.__a[j], self.__a[i]

    def bidirectionalBubbleSort(self):
        left = 0
        right = self.__nItems - 1

        while left < right:
            # coloca el elemento mas grande a la derecha 
            for inner in range(left, right):
                if self.__a[inner] > self.__a[inner + 1]:
                    self.swap(inner, inner + 1)

            right -= 1

            # Coloca el elemento más pequeño a la izquierda
            for inner in range(right, left, -1):
                if self.__a[inner] < self.__a[inner - 1]:
                    self.swap(inner, inner - 1)

            left += 1

    def display(self):
        print(self.__a)

# Ejemplo de uso
arr = [5, 1, 4, 2, 8, 0, 2]
array_instance = Array(arr)
print("Array original:", arr)
array_instance.bidirectionalBubbleSort()
print("Array ordenado:", end=" ")
array_instance.display()