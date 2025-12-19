'''
Prompt: Design a locker system like Amazon Locker where delivery drivers can deposit packages and customers can pick 
them up using a code.

Notes:
- Deposit packages
- Customers can pick them up using a code.

Understand:
- Packages same size? No, S/M/L compartments, match size exactly. How many of each (you define)
    - If full oor all full => error.
- What if the package never gets picked up?
    - It expires with a TTL.
- What happens once the customer picks up the package => compartment becomes available.
- Code => integer.
- Actions: Deposit Package, Pick Up Package.

Requirements:
- Packages get stored into compartments of a certain size. If it doesn't fit, return an error.
- If it does fit, return a code.
- A user wanting to retrieve their package enters a code => compartment => that compartment is freed and package is returned.
- After X amount of days, the package frees up. This probably should run as a background service. Secondary req imo.

Entities:
- Locker
- Compartment
- Package

Relationships and Responsibilities:
- Locker
    - Has a list of compartments.
    - Allows for deposit into a compartment
    - Pick up for a compartment.
    - Scan compartments and free them.
- Compartment
    - Has a specific size (S/M/L)
    - May have an access code, if so holds a package.
    - Has a TTL, set upon store
- Package
    - Has a specific size (S/M/L)

Class Design:


class Locker:
    - compartments : List[Compartment]
    - codeGenerator : CodeGenerator

    + deposit_package(package: Package) -> int?
    + retrieve_package(code: int) -> Package?
    + release_expired_compartments() -> None
    
class Compartment:
    - size : CompartmentSize
    - accessCode : int?
    - package : Package?
    - expires_at: dateTime?

    + store(package: Package, code: int, expires_at: dateTime) -> bool
    + release() -> Package?
    + can_fit(size : CompartmentSize) -> bool

class Package:
    - size : CompartmentSize

class CodeGenerator:
    + next() -> int

enum CompartmentSize : SMALL | MED | LARGE

'''

