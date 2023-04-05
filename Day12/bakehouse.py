class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove_node(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next

class BakeHouse:
    def __init__(self):
        self.occupied_tables = LinkedList()

    def get_occupied_table_list(self):
        current = self.occupied_tables.head
        occupied_table_list = []
        while current:
            occupied_table_list.append(current.data)
            current = current.next
        return occupied_table_list

    def allocate_table(self):
        if self.occupied_tables.head is None:
            self.occupied_tables.add_node(1)
            return 1
        current = self.occupied_tables.head
        while current.next:
            if current.next.data - current.data > 1:
                new_table = current.data + 1
                self.occupied_tables.add_node(new_table)
                return new_table
            current = current.next
        if current.data < 10:
            new_table = current.data + 1
            self.occupied_tables.add_node(new_table)
            return new_table
        return None

    def deallocate_table(self, table_number):
        self.occupied_tables.remove_node(table_number)

bh = BakeHouse()
print(bh.allocate_table())
print(bh.allocate_table())
print(bh.allocate_table())
print(bh.get_occupied_table_list())
bh.deallocate_table(1)
print(bh.get_occupied_table_list())
print(bh.allocate_table())
print(bh.get_occupied_table_list())