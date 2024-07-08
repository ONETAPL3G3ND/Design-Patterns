from abc import ABC, abstractmethod


class LivingSpace(ABC):
    def __init__(self, Square: int):
        self.Square = Square

    @abstractmethod
    def GetSquare(self):
        ...


class House(LivingSpace):
    def __init__(self, Square: int, Floors: int):
        self.Square = Square
        self.Floors = Floors

    def GetSquare(self):
        return self.Square * self.Floors


class Apartment(LivingSpace):
    def GetSquare(self):
        return self.Square


def get_square(Item: LivingSpace):
    print(Item.GetSquare())

if __name__ == "__main__":
    house = House(Square=100, Floors=3)
    apartament = Apartment(Square=134)

    get_square(house)
    get_square(apartament)

