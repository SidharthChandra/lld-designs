from abc import ABC, abstractmethod
from vehicles import VehicleType

class FeeStrategy(ABC):
    """Strategy Pattern: Interface for different fee calculation methods."""
    @abstractmethod
    def calculate(self, vehicle_type: VehicleType, duration_seconds: float) -> int:
        pass

class HourlyFeeStrategy(FeeStrategy):
    """Standard hourly pricing with free initial hours."""
    RATES = {
        VehicleType.CAR: 30,
        VehicleType.BIKE: 10
    }
    FREE_HOURS = 2

    def calculate(self, vehicle_type: VehicleType, duration_seconds: float) -> int:
        hours_parked = duration_seconds / 3600
        if hours_parked <= self.FREE_HOURS:
            return 0
        chargeable_hours = hours_parked - self.FREE_HOURS
        rate = self.RATES.get(vehicle_type, 0)
        return int(chargeable_hours * rate)

class FlatFeeStrategy(FeeStrategy):
    """Simple flat fee regardless of duration."""
    FEES = {
        VehicleType.CAR: 50,
        VehicleType.BIKE: 20
    }

    def calculate(self, vehicle_type: VehicleType, duration_seconds: float) -> int:
        return self.FEES.get(vehicle_type, 0)
