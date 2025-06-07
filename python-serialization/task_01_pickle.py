#!/usr/bin/python3
"""
seriailize and deserialize using pickle

this module has 2 functions
"""
import pickle


class Custom0bject:
    """
    this class contains the display
    serialize and deserialize methods
    """
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print("Name: {}\nAge: {}\nIs Student: {}".format
              (self.name, self.age, self.is_student))

    def serialize(self, filename):
        if not filename:
            return None
        try:
            with open(filename, "wb")as f:
                pickle.dump(self, f)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        if not filename:
            return None
        try:
            with open(filename, "rb")as f:
                return pickle.load(f)
        except Exception:
            return None
