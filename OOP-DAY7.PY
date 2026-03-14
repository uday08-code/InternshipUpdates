from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass

    def brakes(self):
        print("Brakes are applied")

class Car(Vehicle):
    def start_engine(self):
        print("The car Engine started")

class Bike(Vehicle):
    def start_engine(self):
        print("The Bike Engine started")

class Bus(Vehicle):
    def start_engine(self):
        print("The Bus Engine started")

c = Car()
c.start_engine()
c.brakes()
