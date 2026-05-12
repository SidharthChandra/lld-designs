from abc import ABC
from enum import Enum

class VehicleType(Enum):
    BIKE = "bike"
    CAR = "car"

class Vehicle(ABC):
    def __init__(self, vehicle_number: str, vehicle_type: VehicleType):
        self.vehicle_number = vehicle_number
        self.vehicle_type = vehicle_type

    def __str__(self):
        return f"{self.vehicle_type.value} {self.vehicle_number}"

class Bike(Vehicle):
    def __init__(self, vehicle_number: str):
        super().__init__(vehicle_number, VehicleType.BIKE)

class Car(Vehicle):
    def __init__(self, vehicle_number: str):
        super().__init__(vehicle_number, VehicleType.CAR)
