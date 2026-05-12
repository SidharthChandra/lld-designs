# Rate Limiter Design

A flexible, thread-safe rate-limiting system designed with SOLID principles.

## 🛠️ Features
- **Multiple Algorithms**: Supports both `TokenBucket` and `LeakyBucket`.
- **Strategy Pattern**: Algorithms are decoupled from the manager, allowing easy switching.
- **Factory Pattern**: Uses dependency injection for bucket creation.
- **Thread Safety**: Uses Python's `threading.Lock` to ensure consistency in multi-threaded environments.

## 🏗️ Architecture
- `buckets.py`: Contains the `RateLimitBucket` abstract base class and concrete implementations.
- `rate_limiter.py`: The core management logic that maps users to their respective buckets.

## 🚀 How to Run
From the root directory:
```bash
python3 rate-limiter/rate_limiter.py
```

## 📚 SOLID Principles Applied
- **OCP (Open/Closed Principle)**: New algorithms can be added by implementing the `RateLimitBucket` interface without modifying the `RateLimiter` class.
- **DIP (Dependency Inversion Principle)**: The `RateLimiter` depends on the `RateLimitBucket` abstraction, not concrete classes.
- **SRP (Single Responsibility Principle)**: `RateLimiter` manages users, while `RateLimitBucket` handles the math of rate limiting.
