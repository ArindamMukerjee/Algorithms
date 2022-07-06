# creating a binary search tree
class Node():
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)

    if key == root.val:
        return root
    elif key > root.val:
        print('right', root.val, key)
        root.right = insert(root.right, key)
    else:
        print('left', root.val, key)
        root.left = insert(root.left, key)
    return root

r = Node(50)
r = insert(r, 50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)

# search a given BST
def search(root, key):
    if root.val == key:
        return root
    elif root.left is None and root.right is None:
        return 'Not Found'

    if key > root.val:
        return search(root.right, key)
    else:
        return search(root.left, key)
search(r, 100)

# inorder traversal
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)
inorder(r)

# preorder traversal
def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)
preorder(r)

# postorder traversal
def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)
postorder(r)