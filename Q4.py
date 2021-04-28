class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def listlength(self):
        printval = self.headval
        c=0
        while printval is not None:
            c+=1
            printval = printval.nextval
        return c
s=input("Please enter a string:")
list1 = SLinkedList()
list1.headval = Node(s[0])
e2 = Node(s[1])
list1.headval.nextval = e2
for i in s[2:]:
    e3 = Node(i)
    e2.nextval = e3
    e2=e3

print(list1.listlength())