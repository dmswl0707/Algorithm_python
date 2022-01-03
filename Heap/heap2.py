
class Heap:
    def __init__(self, data):
        self.heap_array=list()
        self.heap_array.append(None) # 인덱스번호 1번부터 설정
        self.heap_array.append(data)

    def insert(self, data): # 데이터 삽입
        if len(self.heap_array)==1:
            self.heap_array.append(data)
            return True

        self.heap_array.append(data)
        return True


new_heap = Heap(1)
new_heap.insert(8)
new_heap.insert(5)
new_heap.insert(7)

print(new_heap.heap_array)