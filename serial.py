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

    def __init__(self, start):
        """
        Initialze the serial generator
        @param start: int, first number of the initializer
        """

        self.start = start
        self.counter = start - 1

    def __repr__(self):
        return f'<SerialGenerator start={self.start} next={self.counter + 1}'
    def generate(self):
        """
        Increment the counter by one
        @return: int, current serial number
        """
        self.counter += 1
        return self.counter

    def reset(self):
        """
        Reset the counter to original start value
        """
        self.counter = self.start - 1

