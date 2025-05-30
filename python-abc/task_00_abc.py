#!/usr/bin/python3
"""
task_00_abc

this file contains 3 class's:
Animal, Dog, Cat
"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    this is a class animal with abstractmethod
    sound, with no body
    """
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"
