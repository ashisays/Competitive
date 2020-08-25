"""
Builder Pattern is a unique design pattern which helps in building complex object using simple objects and uses an algorithmic approach. This design pattern comes under the category of creational pattern. In this design pattern, a builder class builds the final object in step-by-step procedure. This builder is independent of other objects.

Advantages of Builder Pattern
It provides clear separation and a unique layer between construction and representation of a specified object created by class.

It provides better control over construction process of the pattern created.

It gives the perfect scenario to change the internal representation of objects.
"""

class Director:

    __builder = None

    def set_builder(self,builder):
        self.__builder = builder

    def get_car(self):
        car = Car()
        # First goes the body
        body = self.__builder.get_body()
        car.set_body(body)

        #engine
        engine = self.__builder.get_engine()
        car.set_engine(engine)

        #Add wheels
        i = 0
        while i < 4:
            wheel = self.__builder.get_wheel()
            car.attach_wheel(wheel)
            i +=1
        return car

class Car:
    def __init__(self):
        self.__wheels = list()
        self.__engine = None
        self.__body = None

    def set_body(self,body):
        self.__body = body

    def attach_wheel(self,wheel):
        self.__wheels.append(wheel)

    def set_engine(self,engine):
        self.__engine = engine

    def specification(self):
        print(f"Body : {self.__body.shape}")
        print(f'Engine hoserpower : {self.__engine.horsepower}')
        print(f'Tire size : {self.__wheels[0].size}')

class Builder:
    def get_wheel(self):pass

    def get_engine(self): pass

    def get_body(self):pass

class JeepBuilder(Builder):

    def get_wheel(self):
        wheel = Wheel()
        wheel.size = 22
        return wheel

    def get_engine(self):
        engine = Engine()
        engine.horsepower = 1000
        return engine

    def get_body(self):
        body = Body()
        body.shape = "SUV"
        return body

#Car parts
class Wheel:
    size = None

class Engine:
    horsepower = None

class Body:
    shape = None

def main():
    jeepBuilder = JeepBuilder()
    director = Director()

    print("Build Jeep !!")
    director.set_builder(jeepBuilder)
    jeep = director.get_car()
    jeep.specification()
    print("")

if __name__ == "__main__":
    main()
