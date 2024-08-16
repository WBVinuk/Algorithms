class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    # If the tree is empty, assign the new node as the root
    if not root:
        return Node(key)
    
    # Use a queue to perform level-order traversal
    queue = []
    queue.append(root)

    while queue:
        # Get the front node in the queue
        temp = queue.pop(0)

        # Insert the new node as the left child if empty
        if not temp.left:
            temp.left = Node(key)
            break
        else:
            queue.append(temp.left)

        # Insert the new node as the right child if empty
        if not temp.right:
            temp.right = Node(key)
            break
        else:
            queue.append(temp.right)
    
    return root

def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.val, end=" ")
        in_order_traversal(root.right)



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("In-order traversal before insertion:")
in_order_traversal(root)

# Insert a new node with value 6
root = insert(root, 6)

print("\nIn-order traversal after insertion:")
in_order_traversal(root)
