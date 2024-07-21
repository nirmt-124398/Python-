# Add a static method in problem 2, to greet the user with hello

class Calculator:
    sq=0
    cube=0
    sqroot=0
    def __init__(self,n):
        self.sq=n**2
        self.cube=n**3
        self.sqroot=n**1/2
    def print(self):
        print(f"Square: {self.sq}\nCube: {self.cube}\nSquareroot: {self.sqroot}")
    @staticmethod
    def greet():
        name=input("Enter your Name: ")
        print(f"Hello, {name}")

c=Calculator(4)
c.greet()
c.print()