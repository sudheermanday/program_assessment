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
 
def leafval(root):
    if root:
        if root.left or root.right:
            leafval(root.left)
            leafval(root.right)
        elif root:
            print(root.val)

a=input("Please enter the values:").split()
r=Node(int(a[0]))
s=r
for i in a[1:]:
    r=insert(r,int(i))
 
leafval(s)