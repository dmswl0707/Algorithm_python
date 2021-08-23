
# 노드 클래스 만들기

class Node:
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None

# BST 클래스 만들기

class BST_node:
    def __init__(self, head):
        self.head = head

    def insert(self, value):
        self.current_node = self.head
        while True:
            if value < self.current_node.value:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

    def search(self, value):
        self.current_node = self.head
        while self.current_node:
            if self.current_node.value == value:
                return True
            elif self.current_node.value > value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        return False

head = Node(1)
bst = BST_node(head)

bst.insert(2)
bst.insert(7)
bst.insert(8)
bst.insert(10)

print(bst.search(2)) # True
print(bst.search(5)) # False
print(bst.search(7)) # True
print(bst.search(8)) # True
print(bst.search(15)) # False









