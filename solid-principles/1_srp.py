"""
Single Responsibility Principle (SRP)
------------------------------------
A class should have one, and only one, reason to change.
In other words, every class should have only one responsibility.
"""

# VIOLATION: This class handles both user data and email notification logic.
class UserViolation:
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email

    def save_to_db(self):
        print(f"Saving {self.username} to database...")

    def send_welcome_email(self):
        print(f"Sending welcome email to {self.email}...")


# ADHERENCE: Responsibilities are split into separate classes.
class User:
    def __init__(self, username: str, email: str):
        self.username = username
        self.email = email

class UserRepository:
    def save(self, user: User):
        print(f"Saving {user.username} to database...")

class EmailService:
    def send_welcome_email(self, user: User):
        print(f"Sending welcome email to {user.email}...")

if __name__ == "__main__":
    user = User("john_doe", "john@example.com")
    
    repo = UserRepository()
    repo.save(user)
    
    email_service = EmailService()
    email_service.send_welcome_email(user)
