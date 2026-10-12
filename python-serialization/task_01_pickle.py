#!/usr/bin/env python3
import pickle

"""Documentation for how to use pickle moduel"""


class CustomObject:
    """Class to represent and define behaviors for pickling"""

    def __init__(self, name, age, is_student):
        """Initialisation of attributes"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Method for displaying data"""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """saving object information into pickle file, none if failure"""
        try:
            pickle_out = open(filename, "wb")
            pickle.dump(self, pickle_out)
            pickle_out.close()
        except (OSError, pickle.PicklingError):
            return None

    @classmethod
    def deserialize(cls, filename):
        """unpacking and loading the pickle file's information"""
        try:
            pickle_in = open(filename, "rb")
            output = pickle.load(pickle_in)
            return output
        except (OSError, pickle.UnpicklingError, EOFError):
            return None
