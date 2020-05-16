"""Python serial number generator."""

class SerialGenerator:
    
    def __init__(self, start=0):
        self.start = start
        self.next = start
    
    def generate(self):
        next = self.next
        self.next += 1
        return next

    def reset(self):
        self.next = self.start

