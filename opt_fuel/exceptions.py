"""
Exceptions module for handling custom exceptions in the opt_fuel package.

This module defines custom exceptions used in the opt_fuel package to handle
specific error conditions related to physical parameters.
"""

class InvalidPhysicalParameterError(Exception):
    """
    Exception raised for invalid physical parameters.

    Attributes:
    parameter -- the name of the invalid parameter
    message -- explanation of the error
    """

    def __init__(self, parameter, message="Invalid physical parameter provided"):
        self.parameter = parameter
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.parameter}: {self.message}'
