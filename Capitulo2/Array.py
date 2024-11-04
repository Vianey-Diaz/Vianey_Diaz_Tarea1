class Array(object):
    def __init__(self, initialSize): 
        self._a = [None] * initialSize
        self._nItems = 0

    def __len__(self):    
        return self._nItems

    def get(self, n):
        if 0 <= n < self._nItems:
            return self._a[n]

    def set(self, n, value):
        if 0 <= n < self._nItems:
            self._a[n] = value

    def insert(self, item): 
        if self._nItems >= len(self._a):
            self._resize()
        self._a[self._nItems] = item 
        self._nItems += 1

    def _resize(self):
        new_size = len(self._a) * 2
        new_array = [None] * new_size
        for i in range(self._nItems):
            new_array[i] = self._a[i]
        self._a = new_array

    def find(self, item): 
        for j in range(self._nItems): 
            if self._a[j] == item: 
                return j 
        return -1

    def search(self, item): 
        return self.get(self.find(item))

    def delete(self, item): 
        for j in range(self._nItems): 
            if self._a[j] == item: 
                self._nItems -= 1 
                for k in range(j, self._nItems): 
                    self._a[k] = self._a[k+1] 
                self._a[self._nItems] = None  # Limpiar el último elemento
                return True
        return False

    def traverse(self, function=print): 
        for j in range(self._nItems):
            function(self._a[j])

    def getMaxNum(self):
        max_num = None
        for i in range(self._nItems):
            if isinstance(self._a[i], (int, float)):
                if max_num is None or self._a[i] > max_num:
                    max_num = self._a[i]
        return max_num

    def deleteMaxNum(self):
        max_num = None
        max_index = -1
        for i in range(self._nItems):
            if isinstance(self._a[i], (int, float)):
                if max_num is None or self._a[i] > max_num:
                    max_num = self._a[i]
                    max_index = i

        if max_index != -1:
            for j in range(max_index, self._nItems - 1):
                self._a[j] = self._a[j + 1]
            self._nItems -= 1
            self._a[self._nItems] = None  # Limpiar el último elemento
        return max_num

    def removeDupes(self):
        unique_items = []
        for i in range(self._nItems):
            if self._a[i] not in unique_items:
                unique_items.append(self._a[i])
        self._a = unique_items + [None] * (len(self._a) - len(unique_items))
        self._nItems = len(unique_items)

    def get_nItems(self):
        return self._nItems
    
    def calcular_promedio(self):
        suma = 0
        contador = 0
        for i in range(self._nItems):
            if isinstance(self._a[i], (int, float)):  # Verifica si el elemento es un número
                suma += self._a[i]
                contador += 1
        if contador == 0:
            return 0  # Evita la división por cero si no hay números en el arreglo
        return suma / contador
    
    def cuenta(self, item):
        par = 0
        impar = 0
        if item == 0:
            for i in range(self._nItems):
                if isinstance(self._a[i], (int, float)) and self._a[i] % 2 == 0:
                    par += 1
            if par == self._nItems:
                return 0
            return par
        elif item == 1:
            for i in range(self._nItems):
                if isinstance(self._a[i], (int, float)) and self._a[i] % 2 != 0:
                    impar += 1
            return impar
        return 0


class OrderedRecordArray(object):
    def __init__(self, initialSize, resize_strategy='fixed', increment=10, multiple=2):
        self._a = [None] * initialSize
        self._nItems = 0
        self._maxSize = initialSize
        self._resize_strategy = resize_strategy
        self._increment = increment
        self._multiple = multiple

    def __len__(self):
        return self._nItems

    def insert(self, item):
        if self._nItems >= self._maxSize:
            self._resize()
        j = self._nItems
        while j > 0 and self._a[j-1] > item:
            self._a[j] = self._a[j-1]
            j -= 1
        self._a[j] = item
        self._nItems += 1

    def _resize(self):
        if self._resize_strategy == 'fixed':
            new_size = self._maxSize + self._increment
        elif self._resize_strategy == 'multiple':
            new_size = self._maxSize * self._multiple
        else:
            raise ValueError("Invalid resize strategy")
        
        new_array = [None] * new_size
        for i in range(self._nItems):
            new_array[i] = self._a[i]
        self._a = new_array
        self._maxSize = new_size

    def traverse(self, function=print):
        for j in range(self._nItems):
            function(self._a[j])

    def merge(self, other):
        new_size = self._nItems + other._nItems
        new_array = [None] * new_size
        i = j = k = 0

        while i < self._nItems and j < other._nItems:
            if self._a[i] <= other._a[j]:
                new_array[k] = self._a[i]
                i += 1
            else:
                new_array[k] = other._a[j]
                j += 1
            k += 1

        while i < self._nItems:
            new_array[k] = self._a[i]
            i += 1
            k += 1

        while j < other._nItems:
            new_array[k] = other._a[j]
            j += 1
            k += 1

        self._a = new_array
        self._nItems = new_size

    def delete(self, key):
        i = 0
        while i < self._nItems:
            if self._a[i] == key:
                for j in range(i, self._nItems - 1):
                    self._a[j] = self._a[j + 1]
                self._nItems -= 1
                self._a[self._nItems] = None  # Limpiar el último elemento
            else:
                i += 1






    
