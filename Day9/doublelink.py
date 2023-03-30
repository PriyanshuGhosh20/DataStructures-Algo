class Node:
    def __init__(self,value=None):
        self.prev=None
        self.data=value
        self.next=None

class DoubleLinkedList:
    def __init__(self):
        self.head=None
    def isEmpty(self):
        if self.head is None:
            return True
        return False

    def length(self):
        temp=self.head
        count=0
        while temp is not None:
            temp=temp.next
            count+=1
        return count

    def insertAtBeginning(self,value):
        new_node=Node(value)
        if self.isEmpty():
            self.head=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node

    def insertAtEnd(self,value):
        new_node=Node(value)
        if self.isEmpty():
            self.insertAtBeginning(value)
        else:
            temp=self.head
            while temp.next is not None:
                temp = temp.next
            temp.next=new_node
            new_node.prev=temp

    def insertAtPosition(self,value,position):
        temp=self.head
        count=1
        while temp is not None:
            if count == position-1:
                break
            count+=1
            temp=temp.next
        if position==1:
            self.insertAtBeginning(value)
        elif temp is None:
            print("There are less than {}-1 elements in the linked list. Cannot insert at {} position.".format(position,position))
        elif temp.next is None:
            self.insertAtEnd(value)
        else:
            new_node=Node(value)
            new_node.next=temp.next
            new_node.prev=temp
            temp.next.prev=new_node
            temp.next=new_node

    def deleteFromLast(self):
        if self.isEmpty():
            print("Linked list is empty. Cannot delete elements.")
        elif self.head.next is None:
            self.head=None
        else:
            temp=self.head
            while temp.next is not None:
                temp=temp.next
            temp.prev.next=None
            temp.prev=None

    def deleteFromBeginning(self):
        if self.isEmpty():
            print("Linked List is empty. Cannot delete elements.")
        elif self.head.next is None:
            self.head=None
        else:
            self.head=self.head.next
            self.head.prev=None

    def deleteFromPosition(self,position):
        if self.isEmpty():
            print("Linked list is empty. Cannot delete elements.")
        elif position==1:
            self.deleteFromBeginning()
        else:
            temp=self.head
            count=1
            while temp is not None:
                if count==position:
                    break
                temp=temp.next
                count=count+1
            if temp is None:
                print("There are less than {} elements in linked list. Cannot delete element.".format(position))
                return
            elif temp.next is None:
                self.deleteFromLast()
                return
            temp.prev.next=temp.next
            temp.next.prev=temp.prev
            temp.next=None
            temp.prev=None

    def printLinkedList(self):
        temp=self.head
        while temp is not None:
            print(temp.data,end=" ")
            temp=temp.next

x=DoubleLinkedList()
print("Is Empty?",x.isEmpty())
x.insertAtBeginning(5)
x.insertAtBeginning(15)
x.insertAtEnd(25)
x.insertAtEnd(35)
x.printLinkedList()
print("\nNo. of Nodes:",x.length())
x.insertAtPosition(8,5)
x.printLinkedList()
print("\nDeleted from Beginning:")
x.deleteFromBeginning()
x.printLinkedList()
print("\nDeleted from Last:")
x.deleteFromLast()
x.printLinkedList()
print("\nDeleted from Position:")
x.deleteFromPosition(2)
x.printLinkedList()
