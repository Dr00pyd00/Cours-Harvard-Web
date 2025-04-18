class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
        
    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True    

    def open_seats(self):
        return self.capacity - len(self.passengers)
        
flight =  Flight(3)


ppls = ['Hermione', 'Harry', 'Ron', 'Dumbledore']

for  ppl in ppls :
    success = flight.add_passenger(ppl)
    if success :
        print(f'we added {ppl} successfully')
    else:
        print(f'To many ppl :/ for {ppl}')
print(flight.passengers)