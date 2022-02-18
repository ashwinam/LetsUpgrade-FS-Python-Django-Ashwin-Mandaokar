# make a class CAR .give some atrtribute to it 

# make a class HONDA .inherite from CAR ..add extra feature which 
# is only in HONDA 


# make home class .

# make a class YourHome .Inherit from HONDA .add home feature from HOME class

class Car:
    def __init__(self,color,car_type):
        self.color=color
        self.car_type=car_type

    def carIntro(self):
        return f'This is {self.car_type} type and the color is {self.color}'
    def __repr__(self):
        return self.carIntro()

class Honda(Car):
    def __init__(self,color,car_type,model_name,door='open'):
        super().__init__(color,car_type)
        self.model_name=model_name

    def startCar():
        pass # i want when person enter the car & when the driver closes the door it start automatically & if car in the gear then it shows signal

    def newCarIntro(self):
        return f'the model is {self.model_name},and the color is {self.color}'

    def __repr__(self):
        return self.newCarIntro()

    @staticmethod
    def roadPrice(Baseprice,insurance,roadtax):
        return Baseprice+insurance+roadtax
    

