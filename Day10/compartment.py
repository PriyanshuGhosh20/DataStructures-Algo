class Compartment:
    def __init__(self, name, total_seats, num_passengers):
        self.name = name
        self.total_seats = total_seats
        self.num_passengers = num_passengers
        self.next = None

class Train:
    def __init__(self, train_name, compartment_list):
        self.train_name = train_name
        self.head = None
        for compartment in compartment_list:
            if self.head is None:
                self.head = Compartment(compartment[0], compartment[1], compartment[2])
                current = self.head
            else:
                current.next = Compartment(compartment[0], compartment[1], compartment[2])
                current = current.next

    def get_train_name(self):
        return self.train_name

    def get_compartment_list(self):
        compartment_list = []
        current = self.head
        while current is not None:
            compartment_list.append([current.name, current.total_seats, current.num_passengers])
            current = current.next
        return compartment_list

    def count_compartments(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.next
        return count

    def check_vacancy(self):
        count = 0
        current = self.head
        while current is not None:
            if current.num_passengers < current.total_seats * 0.5:
                count += 1
            current = current.next
        return count

compartment_list = [    
    ["SL", 250, 400],
    ["2AC", 125, 280],
    ["3AC", 120, 300],
    ["FC", 160, 300],
    ["1AC", 100, 45]
]

train = Train("Rajdhani Express", compartment_list)
print("Name:",train.get_train_name())
print("Compartment list:",train.get_compartment_list())
print("No. of compartments:",train.count_compartments())
print("No. of vacant compartments:",train.check_vacancy())

