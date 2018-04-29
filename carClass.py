class Car:
    def __init__(self, year, make, model, color, doors, engineType, fuelType, speed):
        self.year = year
        self.make = make
        self.model = model
        self.color = color
        self.doors = doors
        self.engineType = engineType
        self.fuelType = fuelType
        self.doors = doors
        self.speed = speed 
     
        
  ##setters

    def setYear(self, year):
        self.year = year

    def setMake(self, make):
        self.make = make
        
    def setModel(self, model):
        self.make = model
        
    def setDoors(self, doors):
        self.doors = doors
        
    def setEngineType(self, engineType):
        self.engineType = engineType
    
    def setFuelType(self, fuelType):
        self.fuelType = fuelType
        
    def setSpeed(self, speed):
        self.speed = speed
        
   ##getters 
    def getYear(self):
        return self.year

    def getMake(self):
        return self.make

    def getModel(self):
        return self.model
     
    def getDoors(self):
        return self.doors

    def getEngineType(self):
        return self.engineType
    
    def getFuelType(self):
        return self.fuelType
    
    def getSpeed(self):
        return self.speed

def main():

    year = input('Enter your car year: ')
    make = input('Enter your car make: ')
    model = input('Enter your car model: ')
    color = input('Enter your car color: ')
    doors = input('Enter how many doors your car has: ')
    engineType = input('Enter your car engineSize ect(v8,v4): ')
    fuelType = input('What type of fuel does your car take ect(unleaded, diesel, battery): ')
    speed = input( 'Enter top speed for your car ')

    mycar = Car(year, make, model, color, doors, engineType, fuelType, speed)
    #prints cars, make and model, year, and engine to check if works
    print('My car is a {}, and is made by {}, it has this size engine {}'.format(mycar.getMake(),mycar.getModel(),mycar.getEngineType()))
main()