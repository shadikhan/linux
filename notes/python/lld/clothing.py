#!/usr/bin/env python3

'''
Requirements

Cloting Searching system.

We'd like to filter clothing by their attributes (S/M/L), (Black, Brown, Red)

certain clothing might have their own attributes (pants: waist size)

we can have many types of clothing: Ex: shirts, pants

Encapsulation, Abstraction, Inheritance, Polymorphism


filter(List<Clothing> clothing, Filter f)s

for c in clothing:
    if clothing.match(filter): return true
'''

from abc import ABC, abstractmethod
from enum import Enum

class Color(Enum):
    RED = 1
    BLUE = 2
    GREEN = 3

class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Continent(Enum):
    NORTHAMERICA = 1
    ASIA = 2

class Clothing:
    def __init__(self, color: Color, size : Size, country: str) -> None:
        self.color = color
        self.size = size
        self.country = country
    
    def __repr__(self) -> str:
        return f"{self.color=} {self.size=} {self.country=}"
    
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Clothing):
            return NotImplemented
        
        return (self.color, self.size, self.country) == (other.color, other.size, other.country)
    
    def __hash__(self) -> int:
        return hash((self.color, self.size, self.country))
    
    @classmethod
    def from_dict(cls, d: dict) -> 'Clothing':
        return cls(d['color'], d['size'], d['country'])
        
class Filter(ABC):
    @abstractmethod
    def apply(self, clothing: Clothing) -> bool:
        pass

class ColorFilter(Filter):
    def __init__(self, color: Color) -> None:
        self.color = color

    def apply(self, clothing: Clothing) -> bool:
        return clothing.color == self.color

class SizeFilter(Filter):
    def __init__(self, size: Size) -> None:
        self.size = size

    def apply(self, clothing: Clothing) -> bool:
        return clothing.size == self.size
        
        
class ContinentFilter(Filter):
    def __init__(self, continent: Continent) -> None:
        self.continent = continent
    
    def apply(self, clothing: Clothing) -> bool:
        countries_list = None

        match self.continent:
            case Continent.NORTHAMERICA:
                countries_list = ['USA', 'Mexico']
            case Continent.ASIA:
                countries_list = ['Bangladesh']
            case _:
                countries_list = []
        
        return clothing.country in countries_list

results = set()

def apply_filters(clothing: Clothing, filter_list: list[Filter]) -> None:
    for f in filter_list:
        if f.apply(clothing):
            results.add(clothing)

def filter_clothing(clothing_list : list[Clothing], filter_list: list[Filter]) -> None:
    for clothing in clothing_list:
        apply_filters(clothing, filter_list)


if __name__ == "__main__": 
    filter_clothing(
        [Clothing(Color.RED, Size.SMALL, 'Bangladesh'), Clothing(Color.GREEN, Size.LARGE, 'USA'), Clothing(Color.BLUE, Size.MEDIUM, 'Bangladesh')],
        [ColorFilter(Color.RED), SizeFilter(Size.MEDIUM), ContinentFilter(Continent.NORTHAMERICA)]
    )

    print(results)
    print(Clothing.from_dict({'color': Color.BLUE, 'size': Size.LARGE, 'country': 'Bangladesh'}))
