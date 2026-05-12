import time
from typing import List, Optional, Dict
from vehicles import Vehicle, VehicleType, Car, Bike
from fees import FeeStrategy, HourlyFeeStrategy, FlatFeeStrategy

class ParkingSlot:
    def __init__(self, slot_id: int, slot_type: VehicleType):
        self.slot_id = slot_id
        self.slot_type = slot_type
        self.is_occupied = False
        self.vehicle: Optional[Vehicle] = None

    def park(self, vehicle: Vehicle) -> bool:
        if not self.is_occupied and vehicle.vehicle_type == self.slot_type:
            self.vehicle = vehicle
            self.is_occupied = True
            return True
        return False

    def remove(self) -> Optional[Vehicle]:
        if self.is_occupied:
            vehicle = self.vehicle
            self.vehicle = None
            self.is_occupied = False
            return vehicle
        return None

class ParkingTicket:
    """SRP: Separates the parking session data from the slot itself."""
    def __init__(self, vehicle: Vehicle, slot: ParkingSlot, floor_number: int):
        self.vehicle = vehicle
        self.slot = slot
        self.floor_number = floor_number
        self.entry_time = time.time()

class Floor:
    def __init__(self, floor_number: int, num_of_cars: int, num_of_bikes: int):
        self.floor_number = floor_number
        self.slots: List[ParkingSlot] = []
        self._create_slots(num_of_cars, num_of_bikes)

    def _create_slots(self, num_of_cars: int, num_of_bikes: int):
        for i in range(num_of_cars):
            self.slots.append(ParkingSlot(slot_id=i + 1, slot_type=VehicleType.CAR))
        for i in range(num_of_bikes):
            self.slots.append(ParkingSlot(slot_id=num_of_cars + i + 1, slot_type=VehicleType.BIKE))

    def get_free_slot(self, vehicle_type: VehicleType) -> Optional[ParkingSlot]:
        for slot in self.slots:
            if not slot.is_occupied and slot.slot_type == vehicle_type:
                return slot
        return None

class ParkingLot:
    def __init__(self, name: str, fee_strategy: FeeStrategy):
        self.name = name
        self.floors: List[Floor] = []
        self.active_tickets: Dict[str, ParkingTicket] = {} # vehicle_number -> Ticket
        self.fee_strategy = fee_strategy

    def add_floor(self, car_slots: int, bike_slots: int):
        floor_number = len(self.floors) + 1
        self.floors.append(Floor(floor_number, car_slots, bike_slots))

    def park_vehicle(self, vehicle: Vehicle) -> bool:
        for floor in self.floors:
            slot = floor.get_free_slot(vehicle.vehicle_type)
            if slot and slot.park(vehicle):
                ticket = ParkingTicket(vehicle, slot, floor.floor_number)
                self.active_tickets[vehicle.vehicle_number] = ticket
                print(f"[PARKED] {vehicle} at Floor {floor.floor_number}, Slot {slot.slot_id}")
                return True
        
        print(f"[FULL] No available slot for {vehicle}")
        return False

    def exit_vehicle(self, vehicle_number: str) -> bool:
        ticket = self.active_tickets.pop(vehicle_number, None)
        if not ticket:
            print(f"[ERROR] Vehicle {vehicle_number} not found.")
            return False

        duration = time.time() - ticket.entry_time
        fee = self.fee_strategy.calculate(ticket.vehicle.vehicle_type, duration)
        
        ticket.slot.remove()
        print(f"[EXIT] {ticket.vehicle} from Floor {ticket.floor_number}, Slot {ticket.slot.slot_id}")
        print(f"Duration: {duration:.2f}s, Fee: {fee}")
        return True

    def display_status(self):
        print(f"\n--- {self.name} Parking Status ---")
        for floor in self.floors:
            car_occupied = sum(1 for s in floor.slots if s.is_occupied and s.slot_type == VehicleType.CAR)
            car_total = sum(1 for s in floor.slots if s.slot_type == VehicleType.CAR)
            bike_occupied = sum(1 for s in floor.slots if s.is_occupied and s.slot_type == VehicleType.BIKE)
            bike_total = sum(1 for s in floor.slots if s.slot_type == VehicleType.BIKE)
            
            print(f"Floor {floor.floor_number} -> Cars: {car_occupied}/{car_total}, Bikes: {bike_occupied}/{bike_total}")

if __name__ == "__main__":
    strategy = HourlyFeeStrategy()
    lot = ParkingLot("LuLu Mall", fee_strategy=strategy)
    lot.add_floor(car_slots=2, bike_slots=2)

    v1 = Car("KA-01-1234")
    v2 = Bike("KA-02-5678")
    
    lot.park_vehicle(v1)
    lot.park_vehicle(v2)
    lot.display_status()
    
    time.sleep(1) 
    
    lot.exit_vehicle("KA-01-1234")
    lot.display_status()
