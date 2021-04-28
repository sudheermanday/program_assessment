class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        printval1 = self.headval
        while printval1 is not None:
            
            if printval1.nextval is not None:
                printval1=printval1.nextval
                printval1=printval1.nextval
            else:
                break
            printval = printval.nextval
        return printval.dataval
s=input("Please enter a string:")
list1 = SLinkedList()
list1.headval = Node(s[0])
e2 = Node(s[1])
list1.headval.nextval = e2
for i in s[2:]:
    e3 = Node(i)
    e2.nextval = e3
    e2=e3

print(list1.listprint())