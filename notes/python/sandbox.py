class Base:
    def __init__(self):
        self.base_value = 1

class Child(Base):
    def __init__(self):
        super().__init__()
        self.child_value = 2
    
    def __str__(self):
        return f"Child {self.base_value=}, {self.child_value=}"

