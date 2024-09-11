# Developer: Steve Baker
# Program: Module 3 Lab - Case Study: Lists, Functions, and Classes
# Description: This program will take input for the details of a car and output those details. 

# Super class of Vehicle
class Vehicle:
    def __init__(self, vehicle_type):
        self.vehicle_type = vehicle_type

# Class called Automobile which will inherit the attributes from Vehicle
class Automobile(Vehicle):
    def __init__(self, vehicle_type, year, make, model, doors, roof):
        super().__init__(vehicle_type)
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

# Main function to ask for user input and print it when use is done
def main():
    # Ask for user input
    vehicle_type = "car"
    year = input("Enter the year: ")
    make = input("Enter the make: ")
    model = input("Enter the model: ")
    doors = input("Enter the number of doors (2 or 4): ")
    roof = input("Enter the type of roof (solid or sun roof): ")

    # Set the final details of the car from user input
    car = Automobile(vehicle_type, year, make, model, doors, roof)

    # Print the car details 
    print("\nVehicle Information:")
    print(f"Vehicle type: {car.vehicle_type}")
    print(f"Year: {car.year}")
    print(f"Make: {car.make}")
    print(f"Model: {car.model}")
    print(f"Number of doors: {car.doors}")
    print(f"Type of roof: {car.roof}")

if __name__ == "__main__":
    main()