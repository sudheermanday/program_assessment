class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key
def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val == key:
            return root
        elif root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root
 

def inorder(root):
    if root :
        inorder(root.left)
        print(root.val)
        inorder(root.right)


def preorder(root):
    if root :
        print(root.val)
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root :
        postorder(root.right)
        postorder(root.left)
        print(root.val)
        
a=input("Please enter the elements:").split()
r=Node(int(a[0]))
for i in a[1:]:
    r=insert(r,int(i))
print("Inorder Traversal:") 
inorder(r)
print("Preorder Traversal:") 
preorder(r)
print("Postorder Traversal:") 
postorder(r)