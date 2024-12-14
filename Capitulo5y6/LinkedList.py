class LinkedList(object):
    # ... (otras definiciones mostradas antes) ...

    def traverse(self, func=print):
        for data in self:
            func(data)

    def __len__(self):
        return sum(1 for _ in self)

    def __str__(self):
        result = "[" + " > ".join(str(data) for data in self) + "]"
        return result

    def __iter__(self):
        next = self.getFirst()
        while next is not None:
            yield next.getData()
            next = next.getNext()
