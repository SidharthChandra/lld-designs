"""
Dependency Inversion Principle (DIP)
------------------------------------
1. High-level modules should not depend on low-level modules. Both should depend on abstractions.
2. Abstractions should not depend on details. Details should depend on abstractions.
"""

from abc import ABC, abstractmethod

# VIOLATION: NotificationService (high-level) depends directly on EmailService (low-level).
class EmailServiceViolation:
    def send(self, message):
        print(f"Sending Email: {message}")

class NotificationServiceViolation:
    def __init__(self):
        self.email_service = EmailServiceViolation() # Tight coupling
    
    def notify(self, message):
        self.email_service.send(message)


# ADHERENCE: Both depend on the MessageSender abstraction.
class MessageSender(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailService(MessageSender):
    def send(self, message):
        print(f"Sending Email: {message}")

class SMSService(MessageSender):
    def send(self, message):
        print(f"Sending SMS: {message}")

class NotificationService:
    def __init__(self, sender: MessageSender):
        self.sender = sender # Dependency Injection
    
    def notify(self, message):
        self.sender.send(message)

if __name__ == "__main__":
    # We can easily swap Email for SMS without changing NotificationService
    email_notifier = NotificationService(EmailService())
    email_notifier.notify("Hello via Email")
    
    sms_notifier = NotificationService(SMSService())
    sms_notifier.notify("Hello via SMS")
