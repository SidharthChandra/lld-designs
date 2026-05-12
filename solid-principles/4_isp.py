"""
Interface Segregation Principle (ISP)
-------------------------------------
No client should be forced to depend on methods it does not use.
"""

from abc import ABC, abstractmethod

# VIOLATION: A simple printer is forced to implement fax and scan.
class MultiFunctionDeviceViolation(ABC):
    @abstractmethod
    def print_doc(self): pass
    
    @abstractmethod
    def scan_doc(self): pass
    
    @abstractmethod
    def fax_doc(self): pass

class SimplePrinterViolation(MultiFunctionDeviceViolation):
    def print_doc(self):
        print("Printing...")
    
    def scan_doc(self):
        raise NotImplementedError("Scan not supported")
    
    def fax_doc(self):
        raise NotImplementedError("Fax not supported")


# ADHERENCE: Split the large interface into smaller, specific ones.
class Printer(ABC):
    @abstractmethod
    def print_doc(self): pass

class Scanner(ABC):
    @abstractmethod
    def scan_doc(self): pass

class Fax(ABC):
    @abstractmethod
    def fax_doc(self): pass

class SimplePrinter(Printer):
    def print_doc(self):
        print("Printing...")

class ModernSmartDevice(Printer, Scanner, Fax):
    def print_doc(self): print("Printing...")
    def scan_doc(self): print("Scanning...")
    def fax_doc(self): print("Faxing...")

if __name__ == "__main__":
    printer = SimplePrinter()
    printer.print_doc()
    
    smart_device = ModernSmartDevice()
    smart_device.scan_doc()
