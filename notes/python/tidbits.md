# Tidbits

## Setup

- We're using venv, created by `python3 -m venv .venv`
- Activate it with `source .venv/bin/activate`
- Install packages with `pip3 install <package-name>`
- Install requirements with `pip3 install -r requirements.txt`
- Add `# !/usr/bin/env python3` at the top of python scripts to make them directly executable with `./script.py`. `/usr/bin/env python3` finds the python3 interpreter in your PATH, which will be the one in your virtual environment if it's activated.
- Deactivate the virtual environment with `deactivate`

## General
``` python
# Switch statements:
response_code = 201
match response_code:
    case 200:
        print("OK")
    case 201:
        print("Created")
    case 300:
        print("Multiple Choices")
    case 307:
        print("Temporary Redirect")
    case 404:
        print("404 Not Found")
    case 500:
        print("Internal Server Error")
    case 502:
        print("502 Bad Gateway")
    case _:
        print("Unknown Response Code")

# Exit a program
import sys
sys.exit(0)

# You can use pop() to remove and return elements from lists and dictionaries
# I kinda like this better than using del
my_list = [1, 2, 3, 4, 5]
first_element = my_list.pop(0)  # Removes and returns the first element (1)

my_dict = {'a': 1, 'b': 2, 'c': 3}
removed_value = my_dict.pop('a')  # Removes and returns the value for key 'a' (1)

# Check where packages are installed

>>> import collections
>>> import requests
>>> print(collections.__file__)
/usr/lib/python3.12/collections/__init__.py
>>> print(requests.__file__)
/usr/lib/python3/dist-packages/requests/__init__.py

>>> import sys
>>> print(sys.path)
['', '/usr/lib/python312.zip', '/usr/lib/python3.12', '/usr/lib/python3.12/lib-dynload', '/usr/local/lib/python3.12/dist-packages', '/usr/lib/python3/dist-packages']

# Multi Line Strings
print(
"""Dear Alice,

Eve's cat has been arrested for catnapping,
cat burglary, and extortion.

Sincerely,
Bob"""
)

# f-strings
>>> name = "Shad"
>>> f"Hello {name}"
'Hello Shad'
>>> f"Hello {name=}"
"Hello name='Shad'"

# Multi-line f-strings
name = 'Robert'
messages = 12
(
f'Hi, {name}. '
f'You have {messages} unread messages'
)

# Exception Handling

try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))
    result = numerator / denominator
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter integers only.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print(f"The result is: {result}")
finally:
    print("Execution completed.")

# Raising Exceptions
raise Exception("This is an error message.")

# Common Python setup

# Advantage: Python files can act as either reusable modules, or as standalone programs.
def main():
    print("This script is being run directly.")

# __name__ == "__main__": check if script is run directly (not imported)
if __name__ == "__main__":  # True when run as script, False when imported
    # execute only if run as a script
    main()
```
    

## Reading and Writing Files

## Reading Files
``` python
# strip removes leading and trailing whitespace (including newlines and tabs)
>>> s = "hi \n\t"
>>> s.strip()
'hi'
'hi'

# Read file using 'with' statement: automatically closes file when done
with open('/home/labex/project/hi.txt', 'r') as hello_file:
    hello_content = hello_file.read()  # Read entire file content

hello_content # 'Hello World!'

# readlines() method: returns list of strings, one per line
with open('sonnet29.txt', 'r') as sonnet_file:
    print(sonnet_file.readlines())  # Returns list with each line as a string

['When, in disgrace with fortune and men\'s eyes,\n',
 'I all alone beweep my outcast state,\n',
 'And trouble deaf heaven with my bootless cries,\n',
 'And look upon myself and curse my fate']

# Iterate through file line by line (memory efficient for large files)
with open('sonnet29.txt', 'r') as sonnet_file:
    for line in sonnet_file:  # File object is iterable
        print(line, end='')  # Print without extra newline

'''
When, in disgrace with fortune and men's eyes,
I all alone beweep my outcast state,
And trouble deaf heaven with my bootless cries,
And look upon myself and curse my fate
'''

# splitlines() method: splits string at line breaks, returns list of lines without \n
```

### Writing Files
``` python

# Write to file: 'w' mode overwrites existing file
with open('bacon.txt', 'w') as bacon_file:  # 'w' = write mode
    bacon_file.write('Hello world!\n')  # Returns number of characters written

# Append to file: 'a' mode appends to existing file
with open('bacon.txt', 'a') as bacon_file:  # 'a' = append mode
    bacon_file.write('Bacon is not a vegetable.')
```

## OOP

### Encapsulation

``` python
# Define a class named MyClass
class MyClass:

    # Constructor method that initializes the class object
    def __init__(self):

        # Define a protected variable with an initial value of 10
        # The variable name starts with a single underscore, which indicates protected access
        # This means that the attribute can be accessed within the class and its subclasses but not outside the class.
        self._protected_var = 10

        # Define a private variable with an initial value of 20
        # The variable name starts with two underscores, which indicates private access
        # This means that the attribute can only be accessed within the class and not outside the class, not even in its subclasses.
        self.__private_var = 20

# Create an object of MyClass class
obj = MyClass()

# Access the protected variable using the object name and print its value
# The protected variable can be accessed outside the class but
# it is intended to be used within the class or its subclasses
print(obj._protected_var)   # output: 1

```

### Inheritance / Polymorphism / Abstraction

``` python
# Import the abc module to define abstract classes and methods
from abc import ABC, abstractmethod

# Define an abstract class called Shape that has an abstract method called area
class Shape(ABC):
    def __init__(self):
        self.name = "Shape"

    @abstractmethod
    def area(self):
        pass

# Define a Rectangle class that inherits from Shape
class Rectangle(Shape):
    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    # Implement the area method for Rectangles
    def area(self):
        return self.width * self.height

    def __str__(self):
        return f"Rectangle({self.name=}, {self.width=}, {self.height=})"

# Define a Circle class that also inherits from Shape
class Circle(Shape):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    # Implement the area method for Circles
    def area(self):
        return 3.14 * self.radius ** 2

    def __str__(self):
        return f"Circle({self.name=}, {self.radius=})"

# Create a list of shapes that includes both Rectangles and Circles
shapes = [Rectangle(4, 5), Circle(7)]

# Loop through each shape in the list and print its area
for shape in shapes:
    print(shape.area())

>> from (file) import Rectangle
>> rect = Rectangle(4, 5)
>> print(rect) # Output: Rectangle(self.name='Shape', self.width=4, self.height=5)

```

## Design Patterns

### Strategy Pattern

``` python
from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def execute(self, x):
        pass

class Add(Strategy):
    def execute(self, x):
        return x + 10

class Multiply(Strategy):
    def execute(self, x):
        return x * 10

class Processor:
    def __init__(self, strategy: Strategy):
        self.strategy = strategy

    def process(self, x):
        return self.strategy.execute(x)

# use
p = Processor(Add())
print(p.process(5))       # 15

p.strategy = Multiply()
print(p.process(5))       # 50
```

### Factory Pattern

``` python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return 3.14 * self.r * self.r

class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):
        return self.w * self.h

class ShapeFactory:
    @staticmethod
    def create(kind):
        if kind == "circle":
            return Circle(10)
        elif kind == "rect":
            return Rectangle(3, 4)
        else:
            raise ValueError("unknown shape")

# use
shape = ShapeFactory.create("circle")
print(shape.area())
```

### Singleton Pattern

``` python
# config.py
class Config:
    def __init__(self):
        self.value = 42

instance = Config()

# main.py
from config import instance
```

## Useful imports

``` python
from datetime import datetime, timezone
from pathlib import Path

import json 
import random
import time

# subprocess.run(['du', '-h', logs_path], capture_output = True, text = True)
import subprocess
import sys

from abc import ABC, abstractmethod
from enum import Enum
```

## Walk a directory tree template

``` python
from pathlib import Path

for curr_dir, dirs, files in Path(logs_path).walk():
    # So that processing for dirs and files are lexicographically ordered
    dirs.sort()
    files.sort()

    for file in files:
        with open(curr_dir / file, 'r') as f:
            # content = f.read()
            # lines = f.readlines() or f.splitlines()
            # for line in f: pass
```
