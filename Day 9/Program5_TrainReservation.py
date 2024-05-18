"""
Create a Base class Train containing members as Train_no, Train_Name.
Derive a class Route (Route_id, Source, Destination) from Train class. 
Derive a class Reservation(Number_Of_Seats, Train_Class, Fare, Travel_Date) from Route.
Write a menu driven program to perform the following functions
1) Enter  details of reservations 
2) Display details of all reservations with total fare
3) Display reservation details of a specified Train class
"""
class Train:
    def __init__(self, Train_no, Train_Name):
        self.Train_no = Train_no
        self.Train_Name = Train_Name

class Route(Train):
    def __init__(self, Train_no, Train_Name, Route_id, Source, Destination):
        super().__init__(Train_no, Train_Name)
        self.Route_id = Route_id
        self.Source = Source
        self.Destination = Destination

class Reservation(Route):
    def __init__(self, Train_no, Train_Name, Route_id, Source, Destination, Number_Of_Seats, Train_Class, Fare, Travel_Date):
        super().__init__(Train_no, Train_Name, Route_id, Source, Destination)
        self.Number_Of_Seats = Number_Of_Seats
        self.Train_Class = Train_Class
        self.Fare = Fare
        self.Travel_Date = Travel_Date

    def display(self):
        print(f"Train_no = {self.Train_no}, Train_Name = {self.Train_Name}, Route_id = {self.Route_id}, Source = {self.Source}, Destination = {self.Destination}, Number_Of_Seats = {self.Number_Of_Seats}, Train_Class = {self.Train_Class}, Fare = {self.Fare}, Travel_Date = {self.Travel_Date}")

    def total_fare(self):
        print(f"Total Fare is: {int(self.Number_Of_Seats) * int(self.Fare)}")
    
ReservationDetails = []
while True:
    print("---------------------------------------------------------------------------")
    print("(1) Enter  details of reservations ")
    print("(2) Display details of all reservations with total fare")
    print("(3) Display reservation details of a specified Train class")
    print("(4) Exit")
    ch = int(input("Enter Your Choice: "))
    print("---------------------------------------------------------------------------")
    match ch:
        case 1:
            print("Enter  details of reservations ")
            Train_no = input("Enter Train_no: ")
            Train_Name = input("Enter Train_Name: ")
            Route_id = input("Enter Route_id: ")
            Source = input("Enter Source: ")
            Destination = input("Enter Destination: ")
            Number_Of_Seats = input("Enter Number_Of_Seats: ")
            Train_Class = input("Enter Train_Class: ")
            Fare = input("Enter Fare: ")
            Travel_Date = input("Enter Travel_Date: ")
            obj = Reservation(Train_no, Train_Name, Route_id, Source, Destination, Number_Of_Seats, Train_Class, Fare, Travel_Date)
            ReservationDetails.append(obj)
        case 2:
            print("Display details of all reservations with total fare")
            for i in ReservationDetails:
                i.display()
                i.total_fare()
        case 3:
            print("Display reservation details of a specified Train class")
            tClass = input("Enter Class Name: ")
            for i in ReservationDetails:
                if i.Train_Class == tClass:
                    i.display()
        case 4:
            break
        case _:
            print("Invalid Choice")
    input("\nPress Enter to go to menu")

