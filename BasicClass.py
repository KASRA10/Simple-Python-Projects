# Class Definition
class Circle:
    def getRadius(self):  # Receive a Number
        self.radius = int(input("please enter the radius number here: ".title()))

    def calculateArea(self):  # Calculate Area
        self.area = round((3.14 * self.radius) ** 2)

    def display(self):  # Automatically Print The Result
        print(f"your radius is {self.radius} \nit's area is {self.area}".title())


# Create A Object
firstCircle = Circle()
# Use Class's Methods
firstCircle.getRadius()
firstCircle.calculateArea()
firstCircle.display()
