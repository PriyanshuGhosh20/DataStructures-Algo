#Traversing a Linked List
class Node:
    def __init__(self,dataval=None):
        self.dataval=dataval
        self.nextval=None

class LinkedList:
    def __init__(self):
        self.headval=None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    def AtBeginning(self,newdata):
        NewNode=Node(newdata)
        NewNode.nextval=self.headval
        self.headval=NewNode

    def AtEnd(self,newdata):
        NewNode=Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        last=self.headval
        while (last.nextval is not None):
            last=last.nextval
        last.nextval=NewNode

    def Inbetween(self,middle_node,newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return
        NewNode=Node(newdata)
        NewNode.nextval=middle_node.nextval
        middle_node.nextval=NewNode

list=LinkedList()
list.headval=Node("Mon")
e2=Node("Tue")
e3=Node("Wed")
list.headval.nextval=e2
e2.nextval=e3
list.AtBeginning("Sun")
list.Inbetween(e3,"Thu")
list.Inbetween(e3.nextval,"Fri")
list.Inbetween(e3.nextval.nextval,"Sat")
list.AtEnd("Doomsday")
list.listprint()


