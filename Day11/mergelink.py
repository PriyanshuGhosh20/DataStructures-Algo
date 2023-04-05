class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge_lists(list1, list2, n):
    if not list1:
        return list2

    if not list2:
        return list1

    count = 1
    curr = list1
    while curr and count < n:
        curr = curr.next
        count += 1

    temp = curr.next
    curr.next = list2
    while list2.next:
        list2 = list2.next
    list2.next = temp

    return list1

list1 = Node(1)
list1.next = Node(2)
list1.next.next = Node(3)
list1.next.next.next = Node(4)
list1.next.next.next.next = Node(5)

list2 = Node(6)
list2.next = Node(7)
list2.next.next = Node(8)
list2.next.next.next = Node(9)

head1 = merge_lists(list1, list2, 2)

current = head1
while current:
    print(current.val, end=' ')
    current = current.next

