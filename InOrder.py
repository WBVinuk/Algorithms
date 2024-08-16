class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def in_order_traversal(root):
    if root:
        # Recursively traverse the left subtree
        in_order_traversal(root.left)
        
        # Print the data of the node
        print(root.val, end=" ")
        
        # Recursively traverse the right subtree
        in_order_traversal(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("In-order traversal of the binary tree:")
in_order_traversal(root)
