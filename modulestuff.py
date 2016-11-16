age=21
weight=100
def printGoodbye():
    print('Goodbye!')
def dogYears(age):
    print(age*7)
class Car:
    def __init__(self):
        self.make=raw_input('What make is the car')
        self.model=raw_input('What model is the car?')
        self.price=raw_input('How much did this car cost?')
        
    def printdetails(self):
        
        print ('this car is a' + self.make + self.model)
        print ('this car cost'+self.price+'Dollars or Euros!')
