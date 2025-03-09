# a = ['s','a','n','l','m']
#
# a = [ a if a != 20  else a.append('0') ]
#
# print(a)
# print('/'.join(a))
#
# if a == 4 :
#     print('hello')
#
# if a == 20 :
#     a.append('0')
#     for x in a : a.append('0')
#
# a = [x if x == '20' else x + '0' for x in a]

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def move(self):
        pass

class Car(Vehicle):

    def move(self):
        print("The car is driving.")

class Bicycle(Vehicle):
    def move(self):
        return "The bicycle is pedaling."

toy = Car()

toy.move()