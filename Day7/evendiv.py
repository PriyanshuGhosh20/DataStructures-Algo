class Queue:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0

    def is_full(self):
        if (self.__rear==self.__max_size-1):
            return True
        return False

    def is_empty(self):
        if(self.__front>self.__rear):
            return True
        return False

    def enqueue(self,data):
        if(self.is_full()):
            print("Queue is Full!!")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data
    
    def dequeue(self):
        if (self.is_empty()):
            print("Queue is Empty!!")
        else:
            data=self.__elements[self.__front]
            self.__front+=1
            return data

    def display(self):
        for index in range(self.__front,self.__rear+1):
             print(self.__elements[index])

    def get_max_size(self):
        return self.__max_size

    def div(self):
        for e in self.__elements[self.__front:self.__rear+1]:            
            flag=0
            for i in range(1,11):
                if e%i==0:
                    flag+=1
            if flag==10:
                 print(e) 
                    
queue1=Queue(5)
print("Is it full?",queue1.is_full())
print("Is it empty?",queue1.is_empty())
queue1.enqueue(13983)
queue1.enqueue(10080)
queue1.enqueue(7113)
queue1.enqueue(2520)
queue1.enqueue(2500)
queue1.display()
print("The Evenly Divisible Elements are:  ")
queue1.div()
