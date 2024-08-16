def minValueNode(node):
    current = node
    while current.left is not None:
        current = current.left
    return current

def deleteNode(root, key):
    if root is None:
        return root
    
    if key < root.value:
        root.left = deleteNode(root.left, key)
    elif key > root.value:
        root.right = deleteNode(root.right, key)
    else:
        # Node with only one child or no child
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        
        # Node with two children
        temp = minValueNode(root.right)
        root.value = temp.value
        root.right = deleteNode(root.right, temp.value)
    
    return root
