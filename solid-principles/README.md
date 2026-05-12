# SOLID Principles in Python

This folder contains clear, concise examples of the **SOLID** principles applied in Python. Each file includes a description of the principle, a "Violation" example (how not to do it), and an "Adherence" example (the correct way).

## 📝 Principles

### 1. [[S]ingle Responsibility Principle (SRP)](./1_srp.py)
> A class should have one, and only one, reason to change.
- Focuses on splitting responsibilities into separate classes to avoid "God Objects".

### 2. [[O]pen/Closed Principle (OCP)](./2_ocp.py)
> Software entities should be open for extension, but closed for modification.
- Focuses on using inheritance or interfaces to add new functionality without breaking existing code.

### 3. [[L]iskov Substitution Principle (LSP)](./3_lsp.py)
> Objects of a superclass should be replaceable with objects of its subclasses without breaking the application.
- Focuses on ensuring that subclasses truly "are-a" type of their superclass and don't break expectations.

### 4. [[I]nterface Segregation Principle (ISP)](./4_isp.py)
> No client should be forced to depend on methods it does not use.
- Focuses on splitting large, "fat" interfaces into smaller, more specific ones.

### 5. [[D]ependency Inversion Principle (DIP)](./5_dip.py)
> High-level modules should not depend on low-level modules. Both should depend on abstractions.
- Focuses on decoupling code by using Dependency Injection and interfaces.

---
*These examples are designed to be simple and easy to understand for educational purposes.*
