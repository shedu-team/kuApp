class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.enough_seats():
            return False
        self.passengers.append(name)
        return True
    def enough_seats(self):
        return self.capacity - len(self.passengers)

people = ["A", "B", "C", "D"]
f = Flight(3)

for person in people:
    if f.add_passenger(person):
        print(f"{person} added to Flight Seccussfully!")
    else:
        print(f"There is No Seat for {person}")
