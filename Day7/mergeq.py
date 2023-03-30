class Queue:
    def __init__(self, size):
        self.__size = size
        self.__elements = [None] * self.__size
        self.__rear = -1
        self.__front = 0

    def is_full(self):
        if self.__rear == self.__size - 1:
            return True
        return False

    def is_empty(self):
        if self.__front > self.__rear:
            return True
        return False

    def enqueue(self, data):
        if self.is_full():
            print("Queue is Full!!")
        else:
            self.__rear += 1
            self.__elements[self.__rear] = data

    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty!!")
        else:
            data = self.__elements[self.__front]
            self.__front += 1
            return data

    def display(self):
        for index in range(self.__front, self.__rear + 1):
            print(self.__elements[index],end=' ')

    def get_max_size(self):
        return self.__size


def merge_queues(q1, q2):
    size1 = q1.get_max_size()
    size2 = q2.get_max_size()
    max_size = size1 + size2

    q3 = Queue(max_size)

    for i in range(min(size1, size2)):
        q3.enqueue(q1.dequeue())
        q3.enqueue(q2.dequeue())

    if size1 > size2:
        for i in range(size2, size1):
            q3.enqueue(q1.dequeue())
    elif size2 > size1:
        for i in range(size1, size2):
            q3.enqueue(q2.dequeue())

    return q3

queue1 = Queue(3)
queue1.enqueue(3)
queue1.enqueue(6)
queue1.enqueue(8)
queue1.display()
print()

queue2 = Queue(6)
queue2.enqueue('b')
queue2.enqueue('y')
queue2.enqueue('u')
queue2.enqueue('t')
queue2.enqueue('r')
queue2.enqueue('o')
queue2.display()
print()

queue3 = merge_queues(queue1, queue2)
queue3.display()
