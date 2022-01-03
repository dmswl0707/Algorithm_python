

class Heap:
    def __init__(self, data):
        self.heap_array=list()
        self.heap_array.append(None)
        self.heap_array.append(data)

    def move_up(self, node_idx): # 순서 바꿔주기
        if node_idx <= 1:
            return False
        parent_idx = node_idx // 2

        if self.heap_array[node_idx] > self.heap_array[parent_idx]:
            return True
        else:
            return False

    def insert(self, data):
        if len(self.heap_array)==1:
            self.heap_array.append(data)
            return True

        self.heap_array.append(data)
        node_idx = len(self.heap_array) - 1 # 왜지?

        while self.move_up(node_idx):
            parent_idx = node_idx // 2
            self.heap_array[node_idx], self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[node_idx]
            node_idx = parent_idx

        return True

new_heap = Heap(15)
new_heap.insert(10)
new_heap.insert(8)
new_heap.insert(5)
new_heap.insert(4)
new_heap.insert(20)

print(new_heap.heap_array)

