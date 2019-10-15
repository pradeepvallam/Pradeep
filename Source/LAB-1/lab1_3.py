class Person:
    def __init__(self, name, status):
        self.name = name
        self.status = status

    # displays info about status of person
    def personinfo(self):
        print(self.name + " is a " + self.status)


class Flight:
    def __init__(self, destination, origin):
        self.destination = destination
        self.origin = origin

# creating employee class from both person and flight classes
class Employee(Person, Flight):
    def __init__(self, name, status, destination, origin):
        Person.__init__(self, name, status)
        Flight.__init__(self, destination, origin)

    def employeeinfo(self):
        print("Their homebase is " + self.origin + " and they are working on the flight to " + self.destination)


# creating passenger from person + flight
class Passenger(Person, Flight):
    def __init__(self, name, status, destination, origin):
        Person.__init__(self, name, status)
        Flight.__init__(self, destination, origin)

    def passengerinfo(self):
        print("They are leaving from " + self.origin + " to go to " + self.destination)


p1 = Passenger("Alice Smith", "Passenger", "Los Angeles", "Las Vegas")
p1.personinfo()
p1.passengerinfo()
p2 = Employee("Bob Burr", "Employee", "Washington DC", "Los Angeles")
p2.personinfo()
p2.employeeinfo()