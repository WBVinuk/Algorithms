class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def pre_order_traversal(root):
    if root:
        # Print the data of the node
        print(root.val, end=" ")
        
        # Recursively traverse the left subtree
        pre_order_traversal(root.left)
        
        # Recursively traverse the right subtree
        pre_order_traversal(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Pre-order traversal of the binary tree:")
pre_order_traversal(root)
