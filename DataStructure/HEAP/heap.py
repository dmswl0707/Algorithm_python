
class Heap:
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(data)

new_heap = Heap(1)
print(new_heap.heap_array)