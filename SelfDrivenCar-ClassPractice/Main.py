# Definition of self-Driven Car by categorized class
class Driverless:
    enginStatus = False
    safeBeltStatus = False
    acceleratorStatus = False
    brakeStatus = False
    handBrakeStatus = False
    rightBlinkerStatus = False
    leftBlinkerStatus = False
    hornStatus = False
    # Definition Speed Variable for Car Speed
    speedometer = 0

    def __init__(self, carName, Year, gearType, color):
        self.carName = carName
        self.Year = Year
        self.gearType = gearType
        self.color = color

    def start(self):
        if self.enginStatus is False:
            print(f"your {self.carName} is started".title())
            self.enginStatus = True
        else:
            print(f"{self.carName} has been started already!".title())

    def turnOff(self):
        if self.enginStatus is True:
            print(f"{self.carName} is off now".title())
            self.enginStatus = False
        else:
            print(f'{self.carName} has already "off"'.title())

    def safeBeltOn(self):
        if self.safeBeltStatus is False:
            print(f"safe-belt is fastened now in {self.carName}".title())
            self.safeBeltStatus = True
        else:
            print("the safe-belt has fastened already!".title())

    def safeBeltOff(self):
        if self.safeBeltStatus is True:
            print(f"safe-belt is free now in {self.carName}".title())
            self.safeBeltStatus = False
        else:
            print("the safe-belt has been free already!".title())

    def Accelerator(self):
        if self.acceleratorStatus is False:
            self.speedometer += 10
            print(f"your speed is {self.speedometer} KM/H right Now".title())
            if self.speedometer == 100:
                print("your on maximum Speed!!".title())
                self.acceleratorStatus = True
        elif self.acceleratorStatus is True:
            print(
                f"be careful of your speed which is {self.speedometer} right now you should use a brake!!!".title()
            )

    def brake(self):
        if self.speedometer != 0 and self.brakeStatus is False:
            self.speedometer -= 10
            print(
                f"your car speed has lowed and it is {self.speedometer} KH/H right now".title()
            )
            if self.speedometer == 0:
                print(
                    f"your cre stopped and your car speed is {self.speedometer} KH/H".title()
                )
                self.brakeStatus = True
        elif self.brakeStatus is True or self.speedometer == 0:
            print(
                f"be careful your brake are pushed already and your speed is {self.speedometer} KM/H!!"
            )

    def handBrakeOn(self):
        if self.handBrakeStatus is False:
            print(f"handbrake is free now in {self.carName}".title())
            self.handBrakeStatus = True
        else:
            print("the handbrake has pushed down(Free) already!".title())

    def handBrakeOff(self):
        if self.handBrakeStatus is True:
            print(f"handbrake is pushed up now in {self.carName}".title())
            self.handBrakeStatus = False
        else:
            print("the handbrake has been up already!".title())

    def rightBlinkerOn(self):
        if self.rightBlinkerStatus is False:
            print("rightBlinker is lighted now".title())
            self.rightBlinkerStatus = True
        else:
            print("the rightBlinker has been lighted already!".title())

    def rightBlinkerOff(self):
        if self.rightBlinkerStatus is True:
            print("rightBlinker is Off now".title())
            self.rightBlinkerStatus = False
        else:
            print("the rightBlinker has been off already!".title())

    def leftBlinkerOn(self):
        if self.leftBlinkerStatus is False:
            print("leftBlinker is lighted now".title())
            self.leftBlinkerStatus = True
        else:
            print("the leftBlinker has been lighted already!".title())

    def leftBlinkerOff(self):
        if self.leftBlinkerStatus is True:
            print("leftBlinker is off now".title())
            self.leftBlinkerStatus = False
        else:
            print("the leftBlinker has been off already!".title())

    def hornOn(self):
        if self.hornStatus is False:
            print("the horn is boobing now!".title())
            self.hornStatus = True
        else:
            print("the horn is horning since some seconds ago!!!".title())

    def hornOff(self):
        if self.hornStatus is True:
            print("the horn is soundless now!".title())
            self.hornStatus = False
        else:
            print("the horn is off already!".title())


# Create a SelfDriven Car Object
myCar = Driverless("BMV", 2024, "Automatic", "BlueSky")
print(
    f"Car Name: {myCar.carName}\nCar Year: {myCar.Year}\ncar Gear level: {myCar.gearType}\nCar color: {myCar.color}".title()
)

# Test Example (Methods)
myCar.Accelerator()
myCar.Accelerator()
myCar.Accelerator()
myCar.Accelerator()
myCar.Accelerator()
myCar.Accelerator()
myCar.Accelerator()
myCar.Accelerator()
myCar.Accelerator()
myCar.Accelerator()
myCar.Accelerator()
myCar.brake()
myCar.brake()
myCar.brake()
myCar.brake()
myCar.brake()
myCar.brake()
myCar.brake()
myCar.brake()
myCar.brake()
myCar.brake()
myCar.brake()
