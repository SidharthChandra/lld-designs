# Low-Level Design (LLD) in Python

A collection of Low-Level Design (LLD) problems implemented in Python, focusing on clean code, SOLID principles, and real-world system design patterns.

## 🚀 Purpose
This repository serves as a learning resource for mastering object-oriented design and system architecture. Each implementation emphasizes:
- **SOLID Principles**: Ensuring code is maintainable, scalable, and decoupled.
- **Design Patterns**: Applying industry-standard patterns (Strategy, Factory, Singleton, etc.).
- **Thread Safety**: Handling concurrency in real-world scenarios.
- **Testability**: Designing components that are easy to unit test.

## 📂 Project Structure
Each directory contains a specific LLD problem with its implementation and explanation.

### 1. Rate Limiter (`/rate-limiter`)
A flexible, thread-safe rate-limiting system supporting multiple algorithms.
- **Algorithms**: Token Bucket, Leaky Bucket.
- **Key Features**:
  - Decoupled algorithm logic using the **Strategy Pattern**.
  - **Dependency Injection** for bucket creation via factories.
  - **Abstract Base Classes** to enforce contracts.
  - Per-user rate limiting with thread-safe bucket management.

## 🛠️ How to Run
Navigate to the specific design directory and run the implementation:

```bash
python3 rate-limiter/rate_limiter.py
```

## 📚 Principles Followed
- **S**ingle Responsibility Principle (SRP)
- **O**pen/Closed Principle (OCP)
- **L**iskov Substitution Principle (LSP)
- **I**nterface Segregation Principle (ISP)
- **D**ependency Inversion Principle (DIP)

---
*Maintained for educational purposes and system design interview preparation.*
