"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start = 0):
        """Return number incremented each time it is called starting at start"""

        self.start = self.next = start
    
    def __repr__(self):
        """Show representation of Generator"""

        return f"Serial Generator: Start = {self.start} Next = {self.next}"

    def generate(self):
        """Return the serial number"""

        self.next += 1
        return self.next - 1
    
    def reset(self):
        """Reset function back to original start"""

        self.next = self.start
    

