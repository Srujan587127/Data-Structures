class Node:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = Node(10)

root.left = Node(5)
root.left.left = Node(15)

root.right = Node(20)
root.right.left = Node(25)
root.right.right = Node(30)


def Search(root, key):
    if root is None:
        return False

    if root.data == key:
        return True

    return Search(root.left, key) or Search(root.right, key)


result1 = Search(root, 25)
result2 = Search(root, 100)

print("Search 25:", result1)
print("Search 100:", result2)