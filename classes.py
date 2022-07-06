class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def open_seats(self):
        return self.capacity - len(self.passengers)


    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True


flight = Flight(3)

people = ["Mohammad", "Ali", "Abbas", "Karrar"]

for person in people:
    if flight.add_passenger(person):
        print(f"{person} added to the flight Successfully!")
    else:
        print(f"Sorry! There is No enough Seats for {person}")
        
