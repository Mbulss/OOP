class House:
    def __init__(self, color, address):
        self.color = color
        self.address = address
        self.garage = None

    def paint(self, new_color):
        self.color = new_color
        print(f"The house is now {self.color}.")

    def add_garage(self):
        self.garage = "Garage added"
        print(self.garage)

    def set_address(self, new_address):
        self.address = new_address
        print(f"The house address is now {self.address}.")

# Create a house
my_house = House("red", "01 Menteng St")
print(f"Originally, the house was {my_house.color} at {my_house.address}.")

# Paint the house
my_house.paint("blue")

# Add a garage to the house
my_house.add_garage()

# Change the house address
my_house.set_address("56 Sudirman St")