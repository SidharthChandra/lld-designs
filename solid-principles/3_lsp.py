"""
Liskov Substitution Principle (LSP)
-----------------------------------
Objects of a superclass should be replaceable with objects of its subclasses 
without breaking the application.
"""

# VIOLATION: Ostrich is a Bird but cannot fly. 
# Replacing Bird with Ostrich in a function that calls fly() will break it.
class BirdViolation:
    def fly(self):
        print("Flying...")

class SparrowViolation(BirdViolation):
    pass

class OstrichViolation(BirdViolation):
    def fly(self):
        raise Exception("Ostriches cannot fly!")


# ADHERENCE: Refactor the hierarchy so that only birds that can fly have the fly method.
class Bird:
    def eat(self):
        print("Eating...")

class FlyingBird(Bird):
    def fly(self):
        print("Flying...")

class Sparrow(FlyingBird):
    pass

class Ostrich(Bird):
    # Ostrich only inherits 'eat', not 'fly'
    pass

def make_bird_fly(bird: FlyingBird):
    bird.fly()

if __name__ == "__main__":
    sparrow = Sparrow()
    make_bird_fly(sparrow)
    
    ostrich = Ostrich()
    ostrich.eat() # Safe
    # make_bird_fly(ostrich) # This would now be a type error, preventing the crash.
