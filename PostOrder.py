class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def post_order_traversal(root):
    if root:
        # Recursively traverse the left subtree
        post_order_traversal(root.left)
        
        # Recursively traverse the right subtree
        post_order_traversal(root.right)
        
        # Print the data of the node
        print(root.val, end=" ")


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Post-order traversal of the binary tree:")
post_order_traversal(root)
