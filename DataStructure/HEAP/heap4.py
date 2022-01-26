

class Heap:

    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None)
        self.heap_array.append(data)

    def pop(self):
        if len(self.heap_array) <= 1:
            return None

        returned_data = self.heap_array[1] # 삭제할 떄, 최상단 노드를 삭제한다.
        return returned_data




