#!/usr/bin/env python3
import pickle


class CustomObject:
    def __init__(self, name: str, age: int, is_student: bool):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        try:
            pickle_out = open(filename, "wb")
            pickle.dump(self, pickle_out)
            pickle_out.close()
        except pickle.PickleError:
            return None

    @classmethod
    def deserialize(cls, filename):
        try:
            pickle_in = open(filename, "rb")
            output = pickle.load(pickle_in)
            return output
        except pickle.UnpicklingError:
            return None
