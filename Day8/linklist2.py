class Node:
    def __init__(self,data):
        self.item=data
        self.ref=None

class LinkedList:
    def __init__(self):
        self.start_node = None
    
    def traverse_list(self):
        if self.start_node is None:
            print("List has no element.")
            return
        else:
            n=self.start_node
            while n is not None:
                print(n.item," ")
                n=n.ref

    def insert_at_start(self,data):
        new_node=Node(data)
        new_node.ref=self.start_node
        self.start_node=new_node


    def insert_at_end(self,data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node=new_node
            return
        n=self.start_node
        while n.ref is not None:
            n=n.ref
        n.ref=new_node

    def delete_at_start(self):
        if self.start_node is None:
            print("The list has no element to delete.")
            return
        self.start_node=self.start_node.ref
    
    def delete_at_end(self):
        if self.start_node is None:
            print("The list has no element to delete.")
            return
        n=self.start_node
        while n.ref.ref is not None:
            n=n.ref
        n.ref=None

    def insert_at_index(self, index, data):
        if index <= 0:
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node = new_node
        else:
            i = 1
            n = self.start_node
            while i < index and n is not None:
                n = n.ref
                i += 1
            if n is None:
                print("Index out of bound")
            else:
                new_node = Node(data)
                new_node.ref = n.ref
                n.ref = new_node

    def delete_element_by_value(self,x):
        if self.start_node is None:
            print("The list has no element to delete")
            return
        if self.start_node.item==x:
            self.start_node=self.start_node.ref
            return
        n=self.start_node
        while n.ref is not None:
            if n.ref.item==x:
                break
            n=n.ref
        if n.ref is None:
            print("Item not found in the list.")
        else:
            n.ref=n.ref.ref

    def search_item(self,x):
        if self.start_node is None:
            print("List has no element.")
            return
        n=self.start_node
        while n is not None:
            if n.item==x:
                print("Item found:",x)
                return True
            n=n.ref
        print("Item not found")
        return False

    def get_count(self):
        if self.start_node is None:
            print("The list has no element.")
            return
        n=self.start_node
        count=0
        while n is not None:
            count=count+1
            n=n.ref
        return count

new_linked_list=LinkedList()
new_linked_list.insert_at_start(5)
new_linked_list.insert_at_start(10)
new_linked_list.insert_at_end(15)
new_linked_list.insert_at_end(20)
print("Original list:")
new_linked_list.traverse_list()
new_linked_list.delete_at_start()
print("After deletion at beginning:")
new_linked_list.traverse_list()
new_linked_list.delete_at_end()
print("After deletion at end:")
new_linked_list.traverse_list()
new_linked_list.insert_at_index(1,25)
print("After inserting: ")
new_linked_list.traverse_list()
new_linked_list.search_item(15)
new_linked_list.delete_element_by_value(15)
print("After deletion:")
new_linked_list.traverse_list()
print("No. of node in the list:")
print(new_linked_list.get_count())
