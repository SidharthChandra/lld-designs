# Parking Lot Design

A clean, modular, and scalable Parking Lot system implemented in Python, adhering to SOLID principles.

## 🛠️ Features
- **Multi-floor Support**: Manage parking across multiple floors.
- **Vehicle Types**: Supports different vehicle types (Cars, Bikes) with specific slot requirements.
- **Dynamic Fee Calculation**: Uses the **Strategy Pattern** to allow different pricing models (Hourly, Flat, etc.).
- **Efficient Lookups**: Uses a ticket-based system for $O(1)$ vehicle retrieval and exit.
- **Modular Architecture**: Decoupled components for vehicles, fees, and core logic.

## 🏗️ Architecture
- `vehicles.py`: Defines vehicle types and classes.
- `fees.py`: Implements various fee calculation strategies.
- `parking_lot.py`: Core logic for managing slots, floors, and the overall parking process.

## 🚀 How to Run
From the root directory:
```bash
python3 parking-lot/parking_lot.py
```

## 📚 SOLID Principles Applied
- **SRP (Single Responsibility Principle)**: 
    - `ParkingSlot` manages occupancy.
    - `ParkingTicket` tracks session data.
    - `FeeStrategy` handles pricing.
- **OCP (Open/Closed Principle)**: 
    - New vehicle types can be added in `vehicles.py`.
    - New pricing models can be added in `fees.py` without changing the core `ParkingLot` logic.
- **LSP (Liskov Substitution Principle)**: All vehicle types (`Car`, `Bike`) can be used wherever a `Vehicle` is expected.
- **ISP (Interface Segregation Principle)**: Small, focused interfaces for fee calculation and vehicle management.
- **DIP (Dependency Inversion Principle)**: `ParkingLot` depends on the `FeeStrategy` abstraction rather than concrete pricing implementations.
