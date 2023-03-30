class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None
    def reverse(self):
        prev=None
        curr=self.head
        while(curr is not None):
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        self.head=prev
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data,end=" ")
            temp=temp.next

list1=LinkedList()
list1.push("<<")
list1.push("<")
list1.push("PG")
list1.push(">")
list1.push(">>")
print("Given linked list: ")
list1.printList()
list1.reverse()
print("\nReversed linked list: ")
list1.printList()
